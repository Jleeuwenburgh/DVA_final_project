# Heart Disease Data Analysis - Presentation Script

## Presentation Overview

| Detail | Information |
|--------|-------------|
| **Total Duration** | 18-20 minutes |
| **Speakers** | 4 people |
| **Structure** | Each speaker covers 4 slides (~4-5 minutes each) |

---

## Speaker 1: Introduction & Data Preprocessing

**Slides 1-4 | Duration: ~5 minutes**

---

### Slide 1: Title Slide
*(30 seconds)*

Good morning/afternoon everyone. We're presenting our comprehensive analysis of heart disease data, focusing on dimensionality reduction, manifold learning, and responsible AI practices. This work was conducted by our team at OPIT.

---

### Slide 2: Analysis Overview
*(1.5 minutes)*

Cardiovascular diseases remain the leading cause of death worldwide, with approximately 17.9 million deaths annually. Our goal was to apply advanced machine learning visualization techniques to understand patterns in cardiac health data.

We worked with the UCI Heart Disease dataset, but discovered a critical issue: over 70% of the original records were duplicates. This reduced our dataset from 1,025 to just 302 unique patient profiles.

Perhaps our most important finding is that heart disease exists on a continuous spectrum rather than as a simple binary condition. This insight emerged only through nonlinear analysis methods.

---

### Slide 3: Dataset Overview & Preprocessing
*(2 minutes)*

Let me walk you through our preprocessing pipeline:

We started with 1,025 patient records containing 14 clinical attributes. The duplicate detection phase was crucial—we found 723 duplicate rows, representing 70.5% of the data. This highlights why data quality assessment must be the first step in any analysis.

For outlier detection, we applied the IQR method to continuous variables. We found notable outliers particularly in cholesterol and blood pressure measurements, which you can see in these boxplots.

After applying StandardScaler normalization, we had 302 clean records ready for analysis—138 healthy patients and 164 with heart disease, giving us a 54.3% disease rate.

---

### Slide 4: PCA Results
*(1 minute)*

Now let me introduce our first dimensionality reduction technique: Principal Component Analysis.

The key finding here is that PCA captures only 33.3% of variance in two dimensions. PC1 explains 21.4% and PC2 just 11.9%. We need seven components to reach even 73.6% cumulative variance.

Looking at feature loadings, PC1 is dominated by ST depression and maximum heart rate, while PC2 is influenced by exercise-induced angina and age.

The considerable class overlap you see in the scatter plot tells us that linear separation alone is insufficient for this problem. I'll now hand over to [Speaker 2] who will explore nonlinear solutions.

---

## Speaker 2: Nonlinear Methods (t-SNE & UMAP)

**Slides 5-7 | Duration: ~4-5 minutes**

---

### Slide 5: PCA Biplot
*(1 minute)*

Thank you. Before diving into nonlinear methods, let's examine the PCA biplot more closely.

Notice how oldpeak and thalach point in opposite directions along PC1—these represent contrasting cardiac indicators. Meanwhile, age, blood pressure, and cholesterol vectors align, showing positive correlation among these clinical measures.

Most importantly, see how the red disease points and blue healthy points intermingle. This confirms that linear dimensionality reduction cannot adequately separate our classes.

---

### Slide 6: t-SNE Analysis
*(2 minutes)*

This brings us to t-SNE, a nonlinear technique that preserves local neighborhood structures.

The perplexity parameter is crucial here. At perplexity 5, we get fragmented clusters—the algorithm overemphasizes local structure. At perplexity 50, we see more globular structures emphasizing global patterns.

The sweet spot is perplexity 30, shown in the bottom-left plot. Notice the clear cluster separation between disease and healthy populations that was completely invisible in our PCA projection. This is the power of nonlinear methods—they can capture complex relationships that linear techniques miss entirely.

---

### Slide 7: UMAP Analysis
*(1.5 minutes)*

UMAP offers a compelling alternative to t-SNE. It's based on Riemannian geometry and algebraic topology, but what matters practically is its performance.

The n_neighbors parameter works similarly to perplexity. Small values like 5 emphasize local structure with tighter clusters, while larger values like 50 capture more global relationships.

The key advantage of UMAP is computational efficiency—it achieves comparable visualization quality to t-SNE but runs significantly faster, making it ideal for larger datasets.

Both methods successfully reveal the hidden structure in our heart disease data that PCA couldn't capture. Now [Speaker 3] will discuss manifold learning approaches that provide theoretical insights into why these nonlinear methods work.

---

## Speaker 3: Manifold Learning & Feature Analysis

**Slides 8-13 | Duration: ~5 minutes**

---

### Slide 8: Isomap
*(1 minute)*

Thank you. Manifold learning assumes our high-dimensional data lies on a lower-dimensional curved surface embedded in the ambient space.

Isomap extends classical multidimensional scaling by using geodesic distances—the shortest path along the data manifold—rather than straight Euclidean distances.

Our Isomap analysis confirms that heart disease data lies on a curved manifold. You can see disease and healthy populations occupy different regions of this manifold. Higher neighbor values produce smoother embeddings while preserving the global structure exceptionally well.

---

### Slide 9: Locally Linear Embedding
*(45 seconds)*

LLE takes a different approach, preserving local geometry by reconstructing each point as a weighted combination of its k-nearest neighbors.

The optimization formula shown here finds low-dimensional coordinates that maintain these local neighborhood relationships. LLE excels at revealing fine-grained patient subgroups within the broader disease categories.

---

### Slide 10: Method Comparison
*(1 minute)*

This comprehensive comparison shows all five methods side by side.

PCA on the top left shows the overlapping classes we discussed. Moving to t-SNE and UMAP, we see clear separation emerge. Isomap and LLE in the bottom row reveal the curved manifold structure.

The key takeaway: nonlinear methods consistently outperform PCA for this dataset. The choice between them depends on your priorities—t-SNE for best local structure, UMAP for speed, Isomap for global geometry.

---

### Slide 11: Class Density Distributions
*(45 seconds)*

These density plots quantify the separation quality. In PCA space, the healthy and disease distributions overlap substantially. But look at t-SNE—we see distinct bimodal distributions for the disease class, indicating identifiable patient subgroups.

This suggests heart disease may manifest as multiple subtypes or progression stages, not a single homogeneous condition.

---

### Slide 12: Feature Correlations
*(1 minute)*

Now let's identify which features drive these patterns.

Chest pain type and maximum heart rate show the strongest positive correlations with disease presence, around +0.43 and +0.42 respectively. Exercise-induced angina shows a strong negative correlation of -0.44.

The correlation matrix reveals that age correlates with blood pressure and cholesterol, confirming that no single feature provides a complete diagnostic picture—we need multivariate analysis.

---

### Slide 13: Feature Gradients
*(30 seconds)*

This visualization maps how clinical measurements vary across t-SNE space. The clear gradients for thalach and oldpeak—shown by the color transitions—indicate these features most strongly influence the cluster structure.

I'll now pass to [Speaker 4] to discuss ethical considerations and conclusions.

---

## Speaker 4: Ethics, Conclusions & Recommendations

**Slides 14-16 | Duration: ~4-5 minutes**

---

### Slide 14: Ethical Considerations & Bias Analysis
*(2 minutes)*

Thank you. As we move toward potential clinical applications, we must address critical ethical issues.

Our bias analysis revealed three major concerns:

**First, sex imbalance:** 68.2% of our sample is male. This limits generalizability to female populations—a significant problem given that heart disease presents differently in women.

**Second, differential disease rates:** females in our dataset show 75% disease rate compared to 44.7% for males. This may reflect selection bias in how patients were recruited, not true population differences.

**Third, age concentration:** our data clusters in the 50-65 age range, limiting applicability to younger or elderly patients.

For privacy and compliance, heart disease status constitutes Protected Health Information under HIPAA. Any production deployment must implement proper de-identification, access controls, and for European applications, full GDPR compliance including explicit consent for health data processing.

---

### Slide 15: Key Insights Summary
*(1.5 minutes)*

Let me synthesize our four key findings:

**One:** Disease patients consistently show lower maximum heart rate across all age groups. This validates the clinical importance of exercise stress testing.

**Two:** Healthy patients cluster near zero ST depression, while disease patients exhibit higher oldpeak values—another clinically meaningful biomarker.

**Three:** t-SNE reveals hidden cluster structure with clearer separation than linear methods. The patterns exist in the data, but you need the right tools to see them.

**Four:** Disease risk exists on a continuous spectrum. The gradual transitions visible in PCA space suggest we shouldn't think of heart disease as purely binary.

---

### Slide 16: Conclusions & Recommendations
*(1.5 minutes)*

To conclude, here are our key takeaways:

**Data quality is critical.** Removing 70.5% duplicates fundamentally changed our analysis—always verify your data before proceeding.

**Nonlinear methods excel for medical data.** t-SNE and UMAP reveal complex patterns invisible to PCA, uncovering patient subgroups that may represent different disease mechanisms.

**For clinical validation,** maximum heart rate and ST depression emerge as the most informative predictors, supporting current exercise stress testing protocols.

**We must address bias** through diverse data collection, regular fairness audits, and transparent documentation of limitations.

**Finally, responsible deployment** requires implementing differential privacy, maintaining human oversight for clinical decisions, and ensuring regulatory compliance.

Our analysis demonstrates that advanced dimensionality reduction techniques can reveal meaningful patterns in cardiac health data—but only when combined with rigorous data quality assessment and ethical consideration.

Thank you for your attention. We're happy to take questions.

---

## Time Allocation Summary

| Speaker | Slides | Topic | Duration |
|---------|--------|-------|----------|
| Speaker 1 | 1-4 | Introduction & Preprocessing | ~5 min |
| Speaker 2 | 5-7 | Nonlinear Methods (t-SNE, UMAP) | ~4.5 min |
| Speaker 3 | 8-13 | Manifold Learning & Features | ~5 min |
| Speaker 4 | 14-16 | Ethics & Conclusions | ~4.5 min |
| **Total** | **16** | | **~19 min** |

---

*Document prepared for: Heart Disease Data Analysis Presentation*  
*Authors: Edoardo Cipriano, Clara Reynolds, Joep Leeuwenburgh, Oghenekaro Arausi*  
*Date: December 2025*
