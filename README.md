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
flake8
```



Some early articles from which to get ideas about the algorithm part:

https://towardsdatascience.com/sentiment-analysis-on-us-twitter-airline-dataset-2-of-2-9e23d8563441

https://github.com/frlim/data2040_final/blob/master/project_1/final_notebook.ipynb

