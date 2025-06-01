Data scientists typically follow a two‑stage workflow:

---

## 1. **Exploration & Prototyping in Notebooks**

* **Quick & dirty**: You start by loading data, visualizing, and building a *single* end‑to‑end pipeline in a notebook cell (just like you did).
* **Iterate by hand**: Tweak a few parameters, rerun cells, inspect outputs.

This is great for intuition, but it doesn’t scale once you need systematic tuning or reproducibility.

---

## 2. **Refactoring into Reusable, Parameterized Code**

Once your prototype “works,” you:

1. **Pull out your core logic**

   * Move data‑prep, feature‑engineering, model‑training, and evaluation into Python functions or classes in a `.py` (or package)
   * Give each step clear function signatures, e.g.

     ```python
     def train_model(X, y, *, learning_rate, depth, n_estimators):
         # build and fit your model
         return fitted_model
     ```

2. **Parameterize & Automate**

   * **Scikit‑learn utilities**:

     ```python
     from sklearn.model_selection import GridSearchCV

     param_grid = {
         "learning_rate": [0.01, 0.1, 0.2],
         "max_depth": [3, 5, 7]
     }
     gs = GridSearchCV(estimator=MyModel(), param_grid=param_grid, cv=5)
     gs.fit(X_train, y_train)
     ```
   * **Modern tuners**: Optuna, Hyperopt, Ray Tune let you search intelligently (Bayesian, early stopping, parallel trials).

3. **Experiment Management**

   * **Command‑line entry points** (using `argparse`, [Hydra](https://hydra.cc), or [Click](https://click.palletsprojects.com/)) so you can run:

     ```
     $ python train.py --lr 0.1 --depth 5 --n-estimators 200
     ```
   * **Notebook parameterization**: Tools like [Papermill](https://papermill.readthedocs.io/) let you tag parameters and execute the same notebook many times with different settings.

4. **Tracking & Reproducibility**

   * **MLflow**, **Weights & Biases**, or **Neptune** to log hyperparameters, versions of data and code, metrics, and even model binaries.
   * **DVC** or **Git‑LFS** for versioning large datasets and trained models alongside your code.

---

### Putting It All Together

1. **Prototype** in a notebook until you’ve nailed down the features and rough architecture.
2. **Refactor**: extract functions, set up a `train.py` (and maybe `evaluate.py`).
3. **Automate**: add a `--config config.yaml` or command‑line flags to sweep hyperparameters.
4. **Track**: run experiments in parallel on your laptop or a cluster, logging everything to a dashboard.
5. **Iterate**: review the experiment dashboard to pick the best hyperparameters, then lock them in for your final run.

---

> **Why bother?**
>
> * **Reproducibility**: Anyone (including Future You) can re‑run an experiment and get the same results.
> * **Scalability**: Sweeping dozens or hundreds of hyperparameter combinations becomes trivial.
> * **Clarity**: Separating exploration from production code keeps both cleaner.

---

So: data scientists usually start in a notebook to explore, but **very quickly** refactor into parameterized scripts or use hyperparameter‐tuning frameworks. Manually editing notebook cells ten times is fine as a first draft, but for real projects almost everyone moves to a more automated, trackable workflow.
