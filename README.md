# Multi‑Label Emotion Detection in Text

This repository contains all materials for my project on detecting up to **28 emotions** in a single sentence.

---

## Folder overview

| Path | Contents |
|------|----------|
| `notebooks/` | Colab notebooks for every experiment: SVM baseline, BERT fine‑tune, RoBERTa fine‑tune, domain‑shift test, and Gradio demo |
| `report/Emotion_Project_Report.pdf` | Full IEEE‑style project report |
| `slides/presentation.pdf` | 5‑minute presentation deck |

---

## Quick start (in Google Colab)

1. Click any notebook in the `notebooks/` folder.  
2. Choose **Open in Colab**.  
3. In Colab, go to **Runtime → Run all**.  
   All required Python packages are installed automatically.

### Notebook guide

| Notebook | Purpose |
|----------|---------|
| `01_svm_baseline.ipynb` | Build TF‑IDF features and train a Support Vector Machine baseline |
| `02_bert_finetune.ipynb` | Fine‑tune BERT on GoEmotions |
| `03_roberta_finetune.ipynb` | Fine‑tune RoBERTa (best model) |
| `04_domain_shift_eval.ipynb` | Zero‑shot evaluation on a Twitter emotion dataset |
| `05_gradio_demo.ipynb` | Launch the interactive web demo (top‑3 emotions) |

---

## Demo

Run `05_gradio_demo.ipynb`, then click the link that appears (e.g., `https://xxxx.gradio.live`).  
Type any text and the page will show the three most likely emotions and their confidence scores.

---

## Citation

*GoEmotions* — D. Demszky *et al.* “GoEmotions: A Dataset of Fine‑Grained Emotions.” ACL 2020.  
*BERT* — Devlin *et al.*, NAACL 2019.  
*RoBERTa* — Liu *et al.*, arXiv 2019.

---

## License

MIT License
