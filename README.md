
# TDWI Intro to Machine Learning
Hands-on Introduction to Machine Learning with Python, Pandas, Matplotlib and Scikit-Learn


## Quick start guide

#### Clone this repository on your local computer

```
git clone https://github.com/Dataweekends/tdwi_intro_ml_one_day.git
```

> TIP: If you are not familiar with git and github you can just download the most recent release file from the [releases tab](https://github.com/Dataweekends/tdwi_intro_ml_one_day/releases/) and unpack the zip file on your computer.

#### Download and Install Anaconda Python 3.6

https://www.continuum.io/downloads

#### Change to course folder

```
cd tdwi_intro_ml_one_day
```

#### Launch Jupyter Notebook

```
jupyter notebook
```

#### Open your browser to

```
http://localhost:8888
```

You are good to go! Enjoy!



### Instructions for Conda environment creation

The following is not necessary if you have a recent version of Anaconda installed on your computer. If you want to create a virtual environment specifically for this tutorial, we provide an [environment configuration file](environment.yml). From the terminal follow these steps:

#### Change to course folder

```
cd tdwi_intro_ml_one_day
```

#### Create the course environment

```
conda env create
```

wait for the environment to create, this may take a few minutes

#### Activate the environment (Mac/Linux)
```
conda activate tdwi
```

#### Activate the environment (Windows)
```
activate tdwi
```

Check that your prompt changed to

```
(tdwi) $
```

Now you can run jupyter notebook from within the environment.



### Troubleshooting

#### Updating Conda

If you have installed Anaconda a long time ago, you may want to update it by running

```
conda update conda
```

and then

```
conda update anaconda
```
