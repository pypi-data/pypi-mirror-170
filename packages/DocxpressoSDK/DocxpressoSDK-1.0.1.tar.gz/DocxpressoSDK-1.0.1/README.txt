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
# Introduce your credentials:
# 'pKey' is the apikey associated with your Docxpresso installation
# 'docxpressoInstalattion' is the URL of your Docxpresso instance, i.e. https://xxxx.docxpresso.net

Example = DocxpressoSDK.Utils({'pKey':'*********','docxpressoInstallation':'***********'})

# If we need, for example, to regenerate a document you need to provide:
# 'id' that corresponds to the template id
# 'token' or unique identifier of the document to be regenerated
data = {}
data['id'] = 1111
data['token'] = '*******'

link = Example.regenerateDocument(data)
print(link)

```

Once you execute this code, it will generate a one time link to regenerate a document associated with that template id and that usage token.