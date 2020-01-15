# datetransform
Feature engineering for dates

[![PyPI version](https://badge.fury.io/py/datetransform.svg)](https://badge.fury.io/py/datetransform)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/datetransform.svg)](https://pypi.python.org/pypi/datetransform/)
[![Build Status](https://travis-ci.com/brandonschabell/datetransform.svg?branch=master)](https://travis-ci.com/brandonschabell/datetransform)
[![codecov](https://codecov.io/gh/brandonschabell/datetransform/branch/master/graph/badge.svg)](https://codecov.io/gh/brandonschabell/datetransform)

## Installation
`datetransform` requires Python 3.5+.

```bash
pip install datetransform
```

## Example Usage
```python
from datetransform.transform import add_date_features
import pandas as pd

df = pd.read_csv('someFile.csv')
df = add_date_features(df, date_field_name='dateCol')  # This dataframe now contains additional date features.
```