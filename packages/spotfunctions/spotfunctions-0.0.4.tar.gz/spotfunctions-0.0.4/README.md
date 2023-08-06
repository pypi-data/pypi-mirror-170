# SpotFunctions Python SDK

This is the SpotFunctions Python SDK to build SpotFunctions in python language. 

## Local development

Create a new project `my-spotfunction` 

```bash
mkdir my-spotfunction
cd my-spotfunction
```

Create a virtual environment and activate it 

```bash
virtualenv -p=python3 venv
source venv/bin/activate
```

Install the spotfunction sdk from the release 

```bash
pip install spotfunctions
```

Create your first spotfunction (see [samples](samples/)), and run it locally with 

```bash
python3 -m spotfunctions.v1.executor.local
```

Enjoy!

## Samples

See the folder [samples](samples/) for a set of examples.


## How to contribute

You can make changes and install locally the package with 

```bash 
python setup.py install
```