# Can BERT keep up with the news?

A Virginia Tech CS 4804 case study by Cinthia Terceros. I fine-tuned BERT to classify hyperpartisan news headlines, then measured how its performance changed on headlines from two later periods.

Hyperpartisan recall fell from **73.8%** in 2017–2020 to **58.5%** in 2021–2022. Over the same comparison, accuracy moved from **75.9%** to **73.8%**.

## What I used

- **Python and Jupyter** for model training and evaluation
- **PyTorch and Hugging Face Transformers** for fine-tuning BERT
- **scikit-learn** for splitting the data and calculating metrics
- **HTML and CSS** for presenting the case study

Open [the case study](index.html) in a browser to see the experiment design, confusion matrices, and examples of errors. The case-study page was drafted with Codex from my notebook's saved results.

## Dataset

[Computational Assessment of Hyperpartisanship in News Titles](https://github.com/VIStA-H/Hyperpartisan-News-Titles), Lyu et al., ICWSM 2024. I combined the two manually labeled files and created a new chronological split for this experiment.
