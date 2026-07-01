# Generali Data Challenge — Insurance Coverage Recommender

**Hackathon · Genertel (Generali Group) · Trieste, June 2025 · Team project**

Team entry for the Generali Data Challenge: a hybrid recommender that suggests
personalized optional car-insurance coverages to existing customers. The final
team system reached a **45% hit rate** on anonymized Genertel data.

> **This repository holds my part of the project** — the data pipeline, feature
> engineering, and exploratory analysis. The recommender models (collaborative
> filtering + Random Forest) were built by teammates and live outside this repo.

---

## Problem

Genertel's customers buy mandatory liability coverage by default, but high-value
optional coverages (theft, collision, roadside assistance, glass, natural events)
often go unprompted. The challenge: identify the right optional coverage to offer
each customer at quote time, from historical purchase behavior and customer/vehicle
profiles.

**Dataset:** ~150k customers · ~2M quotes · ~10.3M coverage records (anonymized).
Raw data is proprietary to Generali and excluded from this repository.

---

## My contribution

- **Feature engineering** — distilled 61 raw quote variables into 21 predictive
  signals (demographic, vehicle, behavioral) consumed by the downstream models.
- **Data pipeline** — multi-table joins across customer × policy × quote × coverage
  (`src/data_preparation.py`).
- **Exploratory analysis & visualization** — feature distributions with KDE,
  chunked correlation heatmaps, and UMAP projections to validate feature selection
  and inform model choice (`src/eda_visualization.py`, `src/correlation_analysis.py`,
  `notebooks/eda.ipynb`).

---

## The team system (context)

A hybrid recommender combining two signals:

| Component | Method | Weight |
|---|---|---|
| Collaborative filtering | Coverage co-occurrence + cosine similarity | 60% |
| Profile-based prediction | Random Forest classifier per coverage type | 40% |

Blended at inference; profile-based fallback for cold-start customers.
Team results: **45% hit rate**, NDCG 19%, 15/27 coverage types modeled. In the
pitch the team projected ~855k annual upsells (~€10M revenue opportunity) for Genertel.

---

## Repository structure

```
generali_challenge/
├── src/
│   ├── data_preparation.py       # Multi-table joins (customer × policy × quote × coverage)
│   ├── eda_visualization.py      # Feature distribution plots with KDE
│   └── correlation_analysis.py   # Correlation heatmaps (chunked for readability)
├── notebooks/eda.ipynb           # Exploratory data analysis
├── plots/correlation/            # Pre-generated correlation heatmaps (4 parts)
├── assets/er_db.jpg              # Database entity-relationship diagram
├── docs/                         # Team presentation (slides + speech)
└── requirements.txt
```

> Raw data files are excluded (proprietary Generali data). Place `cliente.csv`,
> `polizze.csv`, `preventivi.csv`, `garanzie.csv` in a `data/` directory to run the scripts.

---

## Tech stack

Python · pandas · numpy · scipy · scikit-learn · umap-learn · seaborn · matplotlib · joblib

---

## Setup

```bash
pip install -r requirements.txt
# put the four CSVs in data/, then:
python src/data_preparation.py      # builds joined views
python src/eda_visualization.py     # feature distribution plots
python src/correlation_analysis.py  # correlation heatmaps
```

---

## Team

University of Trieste · Generali Data Challenge 2025

- Manuel Magnabosco ([@xtraid](https://github.com/xtraid))
- Michele ([@MScomina](https://github.com/MScomina))
- Nicola Cortinovis ([@NicolaCortinovis](https://github.com/NicolaCortinovis))
- Christian Faccio ([@christianfaccio](https://github.com/christianfaccio))
