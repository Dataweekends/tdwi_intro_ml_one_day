import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=10000",
                "--output", fout.name, path]
        subprocess.check_call(args)

# to test chapter 13 one needs to first run the flask and the tensorflow serving servers


def test_1():
    _exec_notebook("labs/Lab_01_ML Jupyter Pandas review.ipynb")


def test_2():
    _exec_notebook("labs/Lab_02_ML Data Exploration.ipynb")


def test_3():
    _exec_notebook("labs/Lab_03_ML Regression.ipynb")


def test_4():
    _exec_notebook("labs/Lab_04_ML Classification.ipynb")


def test_5():
    _exec_notebook("labs/Lab_05_ML Clustering.ipynb")


def test_1_sol():
    _exec_notebook("solutions_do_not_open/Lab_01_ML Jupyter Pandas review_solution.ipynb")


def test_2_sol():
    _exec_notebook("solutions_do_not_open/Lab_02_ML Data Exploration_solution.ipynb")


def test_3_sol():
    _exec_notebook("solutions_do_not_open/Lab_03_ML Regression_solution.ipynb")


def test_4_sol():
    _exec_notebook("solutions_do_not_open/Lab_04_ML Classification_solution.ipynb")


def test_5_sol():
    _exec_notebook("solutions_do_not_open/Lab_05_ML Clustering_solution.ipynb")
