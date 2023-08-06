# Docxpresso

This is the python version of Docxpresso SDK


## Install
### Prerequisites
- Python 3.9

### Install Package
```
pip install DocxpressoSDK
```

## Quick Start
The following is the minimum needed code to generate a one time link. Use this example, and modify the data[] variables:

```python

import DocxpressoSDK


Example = DocxpressoSDK.Utils({'pKey':'*********','docxpressoInstallation':'***********'})

data = {}
data['id'] = 1111
data['token'] = '*******'

Example.regenerateDocument(data)


```

Once you execute this code, it will generate a one time link to validate a document in the associated Docxpresso SERVER interface


