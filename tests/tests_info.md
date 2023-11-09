# Tests

## Requirements

Use the following command to download the libraries needed to use the tests. Use this in a Python terminal **NOT in the WSL**

```
python -m pip install -r tests/test_requirements.txt
```

## Run tests

Be sure to have a Jekyll server up before starting any test. Run the following command in WSL:

```
jekyll serve -s site
```

This command can be used to run the tests:

```
python -m unittest discover -s ./tests/
```
