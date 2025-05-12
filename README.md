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

## Citation

If you use this project or its components in your research, please cite the following:

- **GoEmotions**  
  Demszky, M., Movshovitz-Attias, D., Ko, M., & McAuley, J. (2020). _GoEmotions: A Dataset of Fine-Grained Emotions._  
  **ACL 2020**  
  ```bibtex
  @inproceedings{demszky-etal-2020-goemotions,
    title     = {GoEmotions: A Dataset of Fine-Grained Emotions},
    author    = {Demszky, Max and Movshovitz-Attias, Yacine and Ko, Mark and McAuley, Julian J.},
    booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},
    year      = {2020}
  }

-**BERT**
  Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.
**NAACL-HLT 2019**
@inproceedings{devlin-etal-2019-bert,
  title     = {BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author    = {Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  booktitle = {Proceedings of NAACL-HLT},
  year      = {2019}
}

**RoBERTa**
Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M., Zettlemoyer, L., & Stoyanov, V. (2019). RoBERTa: A Robustly Optimized BERT Pretraining Approach.
**arXiv preprint arXiv:1907.11692**
@article{liu2019roberta,
  title   = {RoBERTa: A Robustly Optimized BERT Pretraining Approach},
  author  = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
  journal = {arXiv preprint arXiv:1907.11692},
  year    = {2019}
}

**Hugging Face Transformers**
Wolf, T. et al. (2020). Transformers: State-of-the-Art Natural Language Processing.
**Journal of Machine Learning Research**

@article{wolf-etal-2020-transformers,
  title   = {Transformers: State-of-the-Art Natural Language Processing},
  author  = {Wolf, Thomas and Debut, Lysandre and Sanh, Victor and Chaumond, Julija and Delangue, Clement and Moi, Anthony and Cistac, Pierric and Rault, Tim and Louf, Rémi and Funtowicz, Morgan and Brew, Jamie},
  journal = {Journal of Machine Learning Research},
  volume  = {21},
  number  = {107},
  pages   = {1--8},
  year    = {2020}
}


---

## License

Code and notebooks in this repository are released under the MIT License.

GoEmotions dataset is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

The pre-trained BERT and RoBERTa models from Hugging Face are under the Apache 2.0 License.
