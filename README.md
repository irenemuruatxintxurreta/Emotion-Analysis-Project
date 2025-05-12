# Multi‑Label Emotion Detection in Text

This project compares three approaches—TF‑IDF + SVM, BERT, and RoBERTa—for detecting up to **28 emotions** in a single sentence.  
All experiments use the GoEmotions dataset; the best model is demonstrated in an optional Gradio demo.

---

## Folder overview

| Path | Contents |
|------|----------|
| `notebooks/` | Colab notebooks for every experiment: SVM baseline, BERT fine‑tune, RoBERTa fine‑tune, domain‑shift test, and Gradio demo |
| `report/Emotion_Project_Report.pdf` | Full IEEE‑style project report |
| `slides/presentation.pdf` | 5‑minute presentation deck |

---

## Quick‑start (Google Colab)

Run the notebooks **in numeric order** to follow the full process:

1. Open [1_SUPPORT_VECTOR_MACHINE.ipynb](notebooks/1_SUPPORT_VECTOR_MACHINE.ipynb) → click **Open in Colab** → **Runtime ▶ Run all**.  
   This trains the word‑count + SVM baseline.

2. Repeat for  
   [2_BERT.ipynb](notebooks/2_BERT.ipynb) (fine‑tunes BERT)  
   [3_ROBERTA.ipynb](notebooks/3_ROBERTA.ipynb) (fine‑tunes RoBERTa)  

3. Optional:  
   * [4_Emotion_Model_Domain_Shift_Evaluation.ipynb](notebooks/4_Emotion_Model_Domain_Shift_Evaluation.ipynb) tests the best model on Twitter data.  
   * [5_INTERACTIVE_DEMO_GRADIO.ipynb](notebooks/5_INTERACTIVE_DEMO_GRADIO.ipynb) launches the interactive web demo.

Each notebook installs its own Python packages automatically the first time you run it.


### Notebook guide

| Notebook | Purpose |
|----------|---------|
| [1_SUPPORT_VECTOR_MACHINE.ipynb](notebooks/1_SUPPORT_VECTOR_MACHINE.ipynb) | Build TF‑IDF features and train a Support Vector Machine baseline |
| [2_BERT.ipynb](notebooks/2_BERT.ipynb) | Fine‑tune BERT on GoEmotions |
| [3_ROBERTA.ipynb](notebooks/3_ROBERTA.ipynb) | Fine‑tune RoBERTa (best model) |
| [4_Emotion_Model_Domain_Shift_Evaluation.ipynb](notebooks/4_Emotion_Model_Domain_Shift_Evaluation.ipynb) | Test the trained model on a Twitter emotion dataset (no extra training) |
| [5_INTERACTIVE_DEMO_GRADIO.ipynb](notebooks/5_INTERACTIVE_DEMO_GRADIO.ipynb) | Launch a small web page that shows the model’s top‑3 emotions |

---

## Citation

*GoEmotions* — D. Demszky *et al.* “GoEmotions: A Dataset of Fine‑Grained Emotions.” ACL 2020.  
*BERT* — Devlin *et al.*, NAACL 2019.  
*RoBERTa* — Liu *et al.*, arXiv 2019.

---

## License

MIT License
