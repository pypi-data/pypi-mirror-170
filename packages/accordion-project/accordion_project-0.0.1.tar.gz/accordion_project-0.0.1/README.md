## Intro
A python library with various tools for the ACCORDION developer.
### ACCORDION namespace and ID parser
A tool to parse ACCORDION namespaces and IDs. It retrieves the ACCORDION identifier of the application or the component and returns a dictionary with these elements:
{'root':root, 'appName':appName, 'appVersion':appVersion, 'appInstanceId':appInstanceId, 'componentName':componentName, 'runningInstanceId':runningInstanceId, 'minicloudId':minicloudId, 'appInfo':appInfo, 'appInstanceInfo':appInstanceInfo, 'componentInfo':componentInfo, 'runningComponentInfo':runningComponentInfo}
### ACCORDION Intermediate model retriever
A tool to retrieve the intermediate model from the ACCORDION bucket

## Installation instructions
### Locally
1. get file 'utilslib-0.1.0-py3-none-any.whl' from /dist
2. pip install /path/to/accordion/utilslib/parserlib-0.0.1-py3-none-any.whl
### pip
pip install accordionparserlib==0.0.1

## Usage
`from accordion.utilslib import utils`

`print(utils.parse('accordion.OVR.0-0-1.q123-e213-3f56-63h7.LSPart.345g-4g47-2gg6-8hf3.minicloud1'))`

**Expected output**: {'root': 'accordion', 'appName': 'OVR', 'appVersion': '0-0-1', 'appInstanceId': 'q123-e213-3f56-63h7', 'componentName': 'LSPart', 'runningInstanceId': '345g-4g47-2gg6-8hf3', 'minicloudId': 'minicloud1', 'appInfo': 'accordion.OVR.0-0-1', 'appInstanceInfo': 'accordion.OVR.0-0-1.q123-e213-3f56-63h7', 'componentInfo': 'accordion.OVR.0-0-1.q123-e213-3f56-63h7.LSPart', 'runningComponentInfo': 'accordion.OVR.0-0-1.q123-e213-3f56-63h7.LSPart.345g-4g47-2gg6-8hf3.minicloud1'}

`print(parser.parse('accordion.OVR.0-0-1.q123-e213-3f56-63h7.LSPart'))`

**Expected output**: {'root': 'accordion', 'appName': 'OVR', 'appVersion': '0-0-1', 'appInstanceId': 'q123-e213-3f56-63h7', 'componentName': 'LSPart', 'runningInstanceId': None, 'minicloudId': None, 'appInfo': 'accordion.OVR.0-0-1', 'appInstanceInfo': 'accordion.OVR.0-0-1.q123-e213-3f56-63h7', 'componentInfo': 'accordion.OVR.0-0-1.q123-e213-3f56-63h7.LSPart', 'runningComponentInfo': None}

`print(utils.fetch_intermediate_model('29-09-22-testig-ri','0-0-1').status_code)`

**Expecte output**: 200
