## [Check our Zero To Deep Learning 5 day bootcamp. New dates are out!](https://www.zerotodeeplearning.com/?utm_source=github.com&utm_medium=affiliate&utm_campaign=https%3A%2F%2Fgithub.com%2FDataweekends%2Ftdwi_intro_ml_one_day&utm_content=README.md)

------

[![Build Status](https://travis-ci.org/Dataweekends/tdwi_intro_ml_one_day.svg?branch=master)](https://travis-ci.org/Dataweekends/tdwi_intro_ml_one_day)


# TDWI Intro to Machine Learning

Hands-on Introduction to Machine Learning with Python, Pandas, Matplotlib and Scikit-Learn


## Quick start guide

#### Download and Install Anaconda Python 3.7

The first step is to download and install Python 3 on your system, together with all the necessary libraries. Luckily for us Anaconda provides a convenient way to do so. Just download and install it here:

https://www.anaconda.com/download

Next we are going to download the code and access the notebooks. The following commands should be run from a terminal.

#### Clone this repository on your local computer

```
git clone https://github.com/Dataweekends/tdwi_intro_ml_one_day.git
```

> TIP: If you are not familiar with git and github you can just download the most recent release file from the [releases tab](https://github.com/Dataweekends/tdwi_intro_ml_one_day/releases/) and unpack the zip file on your computer.

#### Change to course folder

```
cd tdwi_intro_ml_one_day
```

> TIP: If you downloaded the zip file and not the repo, your folder name will be `tdwi_intro_ml_one_day_master`, just cd into that one: `cd tdwi_intro_ml_one_day_master`

#### Launch Jupyter Notebook

From the course folder, in the terminal, type:
```
jupyter notebook
```
If the command is not recognized try to close and open the terminal again, maybe the path needs to be updated after installation.

> TIP: You can also launch Jupyter using the Anaconda Launcher. This will open Jupyter at your default Home location and you will have to manually navigate to the course folder.

#### Open your browser to

If it didn't open automatically, you can find Jupyter at the following url:
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
