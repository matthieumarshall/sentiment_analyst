# sentiment_analyst

## Development practice

This repo uses a number of automated tools for:
* code formatting
* packaging
* testing

These tools are:
* pytest for testing
* flake8 for analysing compliance with PEP8
* black for automatically formatting code according to PEP8
* pre-commit for automatically calling pre-commit hooks

### FLake 8
Flake 8 will automatically analyse your code and tell you where there are errors in your code
that do not comply to PEP8 standards. It is configured via the `.flake8` file.
It has been setup to run automatically pre-commit and as such is also specified in the .pre-commit-config.yaml file.
Otherwise, it can be run in the command line by simply calling:
```
flake8 .
```
### pre-commit
pre-commit is a python package that will run a series of hooks before you commit. It will allow you to commit
if all of these pass. The pre-commit uses the .pre-commit-config.yaml file for its' configuration.
On first use you need to run `pre-commit install` to set it up.

### Black
black is a python package that will auto format your code to PEP8 standards. It is configured via the 
pyproject.toml file. It is also run pre-commit via the .pre-commit-config.yaml.
If you want to run it standalone, you simply need to run
```
black .
```

### Packaging
The setup.py enables packaging of this code into a `.whl` or `.tar.gz`.
To create a wheel, run the following command:
```
python setup.py bdist_wheel
```
This will generate files in the `dist` and `build` directories.

## GitHub Secrets

In the Workflow file, this repository uses Github secrets for the credentials to access TWEEPY.
These are named TWEEPY_CONSUMER_SECRET and TWEEPY_ACCESS_TOKEN_SECRET.

The TWEEPY_CONSUMER_SECRET should be set to the tweepy consumer secret token
And similarly the TWEEPY_ACCESS_TOKEN_SECRET should be set the tweepy consumer secret token.

You can set up a Powershell script to do this for example:
```
# set environment variables for the tweepy credentials while developping
$Env:TWEEPY_CONSUMER_SECRET="<<insert value here>>"
$Env:TWEEPY_ACCESS_TOKEN_SECRET="<<insert value here>>"
```
which can then be run in Powershell by simply executing
.\scripts\development_environment_variavles.ps1 if that is how you named the script.
You may also need to run the following to allow execution of powershell scripts
```
Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope CurrentUser
```
## Algorithm information

Some early articles from which to get ideas about the algorithm part:

https://towardsdatascience.com/sentiment-analysis-on-us-twitter-airline-dataset-2-of-2-9e23d8563441

https://github.com/frlim/data2040_final/blob/master/project_1/final_notebook.ipynb

