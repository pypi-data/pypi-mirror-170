<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.7-green.svg"></a>
[![Documentation Status](https://readthedocs.org/projects/setlipy/badge/?version=latest)](https://setlipy.readthedocs.io/en/latest/?badge=latest)
<a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
# Setlipy
A simple Python wrapper for the setlist.fm API

## Installation
```bash
pip install setlipy
```

## Quick Start
To get started, install setlipy, register a free account on https://www.setlist.fm/signup and apply for an API key on 
https://www.setlist.fm/settings/api
Add your API Key to your environment:

```python
# Get all setlists from an artist and a specific year. 
# Default as JSON file format.
from setlipy import client

sfm = client.Setlipy(auth="YOUR_API_KEY")

results = sfm.setlists(artist_name="The Rolling Stones", year="2022")

json_dump = (results.json())

for idx, setlists in enumerate(json_dump["setlist"]):
    print(idx, setlists)
```

Default file format is JSON. Use the following to request the data as XML:
```python
# Get all setlists from an artist and a specific year. 
# As XML file format.
import xml
import xml.etree.ElementTree as ET

from setlipy import client

sfm = client.Setlipy(file_format="xml", auth="YOUR_API_KEY")

results = sfm.setlists(artist_name="The Rolling Stones", year="2022")

string_xml = results.content
tree = xml.etree.ElementTree.fromstring(results.content)
print(xml.etree.ElementTree.dump(tree))
```

## Reporting Issues
I'm happy about any suggestions you might have. If you find bugs or other issues specific to this library, file them here. Or just send a pull request.

## License 
MIT © Setlipy Project
