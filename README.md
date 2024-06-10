# A Fisher's exact test interpretation of the TF–IDF term-weighting scheme

This repository contains computer code for reproducing the results described in the manuscript “A Fisher's exact test interpretation of the TF–IDF term-weighting scheme”. ArXiv preprint link: https://arxiv.org/abs/XXXX.XXXXX

## Getting Started

Clone this repository by running the command
```
git clone https://github.com/sheridan-stable/from-fisher-to-tfidf.git
```
and `cd` into the repository root folder `from-fisher-to-tfidf`.

## Running Repository Code
Repository code is written in Python 3 in a Jupyter Notebook environment. Below is one way to run the Jupyter Notebook:

From the command line, create a virtual environment:
```
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```
Launch a Jupyter Notebook server in your default web browser:
```
jupyter notebook
```
and open a Jupyter notebook of interest.

Remember to close the virtual environment once you are done:
```
deactivate
```

## Numerical Experiments
Run the `numerical-experiments.ipynb` notebook to reproduce the results in Table 3 from the manuscript.

## Questions
Feel free to raise an [issue](https://github.com/Sheridan-Stable/from-fisher-to-tfidf/issues) or start a [discussion](https://github.com/Sheridan-Stable/from-fisher-to-tfidf/discussions).

## Citation
If you find anything useful please cite our work using:
```
@misc{Sheridan2024,
  author = {Paul Sheridan and Zeyad Ahmed and Aitazaz A. Farooque},
  title = {A Fisher's exact test interpretation of the TF–IDF term-weighting scheme},
  year = {2024},
  eprint = {arXiv:XXXX.XXXXX}
}
```
