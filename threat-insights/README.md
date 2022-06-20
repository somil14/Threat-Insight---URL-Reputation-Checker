# threat-insights
Threat insights for URL, File Hash, Domain or IP


Introduction
---
  * Provides threat reputation for a provided URL, File Hash, Domain or IP
  * Integrated with Virus Total as threat intelligence provider
  * More intelligence providers can be added in the future
  
Pre-Requisties
---
  * Install python 3 from https://www.python.org/downloads/
  * Check command line python and pip is installed
  * API Key for VT is in the environment file env
  
CLI
---
```
cd threat-intelligence

pip install .

# TI help for option
ti --help
ti rep --help

# Get URL reputation 
ti rep -u <Any valid URL >
e.g. ti rep -u "http://www.virustotal.com"

# Get File reputation
ti rep -f <HASH of the FILE>
e.g. ti rep -f 99017f6eebbac24f351415dd410d522d

# Get Domain reputation
ti rep -d <Any Valid domain>
e.g.  ti rep -d mvision.mcafee.com

# Get IP reputation
ti rep -i <Any Valid IP>
e.g. ti rep -i 8.8.8.8

```