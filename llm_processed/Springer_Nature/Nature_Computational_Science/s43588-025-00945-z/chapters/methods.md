# Methods

## Training and Evaluation Datasets

The dataset used in this study originates from the same filtered subset of the CELLxGENE census (v.2023-05-15)[3] that was curated for the scTab study[11]. This subset was constructed by applying strict inclusion criteria to the full census: only primary human cells profiled with 10x Genomics technologies were retained and the feature space was limited to 19,331 human protein-coding genes. Cell types were required to appear in at least 5,000 cells drawn from a minimum of 30 donors. All gene expression profiles were size-factor normalized to 10,000 counts per cell and log-transformed with a pseudocount of 1 (that is, *f*(*x*) = log(*x* + 1)). The resulting dataset included 22,189,056 cells annotated with 164 distinct cell types, spanning 5,052 donors and 56 tissues. For the ID task, we adopted the same donor-partitioned data split as used by Fischer et al.[11]—that is, 15,240,192 cells for training, 3,500,032 for validation and 3,448,832 for testing.

The OOD test dataset consisted of all newly added human cells in a subsequent release of the CELLxGENE census (v.2023-12-15). These cells were also profiled using 10x Genomics platforms and annotated with one of the 164 labels observed during training. This resulted in approximately 2.6 million cells drawn from 21 studies, covering 80 of the 164 training cell types.

## Cell Ontology

We used the cell ontology obtained from the Ontology Lookup Service at EMBL-EBI as the hierarchical scaffold for all analyses[10]. The ontology was represented as a DAG, where nodes correspond to cell types and directed edges correspond to is_a subtype relationships. We restricted the ontology to the 164 distinct cell types observed in the training set ('Training and evaluation datasets'). In CELLxGENE, which is the atlas used in our study, cell types are annotated by the original data contributors and then harmonized by mapping each label to the closest cell ontology term as specified by the portal's data schema. While the cell ontology offers a valuable scaffold for representing hierarchical relationships among cell types, it is important to note that its structure is continuously being revised where certain definitions and mappings between cell types remain under active refinement.

Because each cell type corresponds to a node in the DAG, we can further classify them on the basis of the type of node they represent. A node was defined as a leaf if it had no children in the pruned ontology and as an internal node if it had at least one child. We also distinguished between connected nodes, which had at least one parent or child present in the curated training set, and isolated nodes, which had none of their ancestors or descendants represented in the training data. These definitions were used to assess how the hierarchical loss propagates information across the ontology (Supplementary Fig. 6).

## Evaluation Protocol

Classification performance was evaluated using the macro *F*1 score, which computes the unweighted average of the *F*1 scores across all cell types. This metric ensures that each cell type contributes equally to the overall score, regardless of class imbalance or prevalence in the dataset. For *C* cell types, the macro *F*1 score is computed as:

$$macro F_1 score = \frac{1}{C} \sum_{i=1}^{C} \frac{2 \times \operatorname{precision}_i \times \operatorname{recall}_i}{\operatorname{precision}_i + \operatorname{recall}_i}$$

where precision<sup>i</sup> and recall<sup>i</sup> are defined for the *i*th class as:

$$precision_i = \frac{TP_i}{TP_i + FP_i}, \quad recall_i = \frac{TP_i}{TP_i + FN_i}.$$

Here, the terms TP<sup>i</sup>, FP<sup>i</sup> and FN<sup>i</sup> denote the number of true positives, false positives and false negatives for the *i*th cell type, respectively. We followed the evaluation framework introduced by Fischer et al.[11] in the scTab study, particularly because of the way those authors handled differences in the granularity of annotations that can occur across different studies: namely, a predicted label is considered correct if it exactly matches the ground-truth label or if it corresponds to a descendant of the ground-truth label in the cell ontology (that is, the prediction is a more specific subtype). This accounts for the fact that some datasets provide coarse-grained annotations (for example, T cell) while others include more detailed subtypes (for example, 'CD4-positive, α–β T cell'). In such cases, predicting a valid subtype is treated as correct, as it remains consistent with the original label. Any other prediction, including a coarser label (such as a parent node) or an unrelated class, is considered incorrect.

## Model Details

We evaluated three model architectures of increasing complexity: a linear classifier, an MLP and the TabNet transformer model. Each model takes as input the full set of 19,331 human protein-coding genes. To ensure a fair comparison across models and with previous work, we adopted the architecture configurations and hyperparameters used in the scTab benchmarking study from Fischer et al.[11] (Supplementary Tables 1–3). The models using CE versus HCE share identical architecture and hyperparameter settings; the loss term is the only difference between them. Specifically, for the models with CE, we used the best hyperparameters available according to the original scTab study. For the models using the HCE loss, we did not perform additional hyperparameter tuning and instead kept the (possibly suboptimal) hyperparameters used for the models with CE. Note that, while recent efforts have explored large-scale foundation models to learn transferable embeddings for single-cell data, such approaches have not yet demonstrated clear advantages over simpler, task-specific approaches for cell-type annotation[11],[22]. We therefore focused on methods where we could easily isolate and study the direct effects of implementing the HCE strategy.

## HCE Loss Function

The HCE loss function extends the standard CE loss by explicitly encoding the structural relationships across the cell ontology. With the standard CE, the loss is computed directly from raw model predictions, treating all cell types as independent classes. Let **p** = (*p*1, …, *pC*) denote the raw predicted probabilities for *C* different cell types. The standard CE loss is given by:

$$\mathcal{L}_{CE} = -\sum_{i=1}^{C} \mathbb{1}\{|abe| = i\} \log p_i$$

where {*label* = *i*} is an indicator function that is equal to 1 if the true class label is the *i*th cell type and 0 otherwise. The HCE adjusts these predictions to reflect hierarchical dependences encoded in the ontology's DAG. The adjusted score *si* for the *i*th cell type is computed as the sum of the predicted probability for its label and the predicted probabilities of all its descendant subtypes:

$$S_i = p_i + \sum_{j \in \mathcal{D}(i)} p_j$$

where *i*) denotes the set of all descendants of cell type *i* in the DAG. This adjustment ensures that the probability of a parent node reflects its entire subgraph. The hierarchical loss is then:

$$\mathcal{L}_{HCE} = -\sum_{i=1}^{C} \mathbb{1}\{|abe| = i\} \log s_i.$$

This formulation directly parallels the evaluation framework, where predictions are considered correct if they match the ground-truth label or any of its descendants. By aligning the training objective with the assessment criterion, HCE encourages cell-type classification models to distribute probability mass in a way that respects biological hierarchy and annotation granularity.

Consider an ontology subgraph that is rooted at the node T cell, which includes subtype labels such as CD4+ T cell, CD8+ T cell and γ–δ T cell. The HCE enables classifications models to predict fine-grained subtypes when available, while also deferring to parent categories when annotations are coarse or ambiguous. For example, if some studies annotate cells as T cell while others use more specific labels such as CD4+ T cell or CD8+ T cell, the adjusted score is computed as:

$$s_{\text{Tcell}} = p_{\text{Tcell}} + p_{\text{CD4+}} + p_{\text{CD8+}} + p_{\gamma-\delta} + \dots$$

This hierarchical set-up allows the model to aggregate subtype information upward, improving consistency across annotations with varying granularity.

## Implementation Details for the HCE Loss

We implemented the HCE loss using a reachability matrix *R*∈ {0, 1}<sup>C</sup>×<sup>C</sup>, where element *Rij* = 1 if the *j*th class is reachable from the *i*th class (meaning *j* is either *i* itself or *j* is a descendant of *i* in the hierarchy) and *Rij* = 0 otherwise. The reachability relation encoded in this matrix is a partial order and has the following mathematical properties:

- Reflexive—every class is reachable from itself (diagonal elements are 1).
- Antisymmetric—if class *i* can reach *j* and *j* can reach *i*, then *i* = *j*.
- Transitive—if class *i* can reach *j* and *j* can reach *k*, then *i* can reach *k*.

Indeed, the reachability matrix represents the transitive closure of the inverted adjacency matrix of the hierarchical DAG structure. Since the original DAG encodes is_a relationships from child to parent, we invert the edge directions to enable parent-to-descendant reachability, ensuring reflexivity by setting the diagonal to 1. Each trained model outputs a raw probability distribution **p** = (*p*1, …, *pC*) over the class labels. The adjusted scores are computed via matrix–vector multiplication: **s** = *R***p**, which efficiently aggregates descendant probabilities for each class. We then apply a log transformation with numerical stability log(**s** + *ϵ*), where *ϵ* = 10−6. The final loss uses a weighted negative log-likelihood as implemented in PyTorch, with class weights computed following scikit-learn's compute_class_weight approach: *wi* = *N*/(*Cni*), where *N* is the total number of samples, *C* is the number of classes and *ni* is the count of samples for the class *i*. The complete loss for a single training sample *x* with true label *t* is:

$$\mathcal{L}_{HCE}(x) = -w_t \log(s_t + \epsilon).$$

This formulation maintains consistency with the models trained with the weighted CE, while incorporating hierarchical structure through efficient matrix operations.

## Statistical Evaluation of Performance Differences Across Loss Functions

To assess changes in predictive performance induced by the ontology-aware training strategy, we computed per-cell-type differences in macro *F*1 score between models trained with standard CE and HCE across four independent training runs. For each cell type, a paired *t*-test was performed and *P* values were adjusted using the Holm–Bonferroni method to correct for multiple hypothesis testing. Statistically significant differences indicate cell types for which ontology-aware training produces consistent changes beyond random variability.