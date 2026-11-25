# Can BERT keep up with the news?

**Cinthia Terceros · Virginia Tech CS 4804**

[Live case study](https://ferchitp.github.io/bert-headline-evaluation/) · [Python training and evaluation notebook](bert_headline_evaluation.ipynb) · [Recall calculation](evaluate_recall.py)

I fine-tuned BERT to identify hyperpartisan news headlines from their titles. To see how the model held up over time, I trained on 2014–2016 headlines and evaluated the selected checkpoint on two later periods.

**Hyperpartisan recall dropped 15.3 percentage points.** Overall accuracy fell 2.1 points, so accuracy alone understated the drop in how often the model caught hyperpartisan headlines.

| Test period | Headlines | Accuracy | Macro F1 | Hyperpartisan recall |
| --- | ---: | ---: | ---: | ---: |
| 2017–2020 | 1,018 | 75.9% | 75.8% | 73.8% |
| 2021–2022 | 447 | 73.8% | 71.9% | 58.5% |

## Explore the experiment

- **Notebook.** Python, pandas, PyTorch, Hugging Face Transformers, and scikit-learn. It covers data cleanup, chronological splitting, fine-tuning, checkpoint selection, and evaluation. The notebook has setup instructions for a GPU-enabled Colab session.
- **Recall script.** Run `python3 evaluate_recall.py` to reproduce the reported recall comparison from the saved confusion counts.
- **Case study.** Compare the confusion matrices and inspect two misclassified headlines. The HTML/CSS case-study page was drafted with Codex using my notebook’s saved results.

The two test periods differ in their sample sizes and label mix. The observed gap comes from one trained checkpoint. A follow-up would compare BERT with TF-IDF and logistic regression on the same splits.

## Dataset

[Computational Assessment of Hyperpartisanship in News Titles](https://github.com/VIStA-H/Hyperpartisan-News-Titles), Lyu et al., ICWSM 2024. I combined the two manually labeled source files and created a new chronological split.
