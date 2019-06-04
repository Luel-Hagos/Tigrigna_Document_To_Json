# Tigrigna_Document_To_Json
**Description How It Works**
* It is written with python programming (python3)
* Make sure that the following modules are installed in your python:
      ~~~
      - docx2txt
      - zipfile
      - json
      - re
      ~~~
 * To check if they are installed on your python use
 ~~~
 
 import docx2txt
 import zipfile
 import json
 import re
 
 
 ~~~
 
 
* If the above commands give you an error then use the following commands to install them on **CMD**.
```
pip install docx2txt
pip install zipfile
pip install json
pip install re


```
* you can also install them on Anaconda promot using _conda_
* [ETL_SAMPLE_DICT.zip](https://github.com/Luel-Hagos/Tigrigna_Document_To_Json/blob/master/ETL_SAMPLE_DICT.zip) contains tigrigna documents to be changed in to JSON structure.
* [JsonOutput.py](https://github.com/Luel-Hagos/Tigrigna_Document_To_Json/blob/master/JsonOutput.py) contains the source code.
* [ETL_SAMPLE_DICT01.json](https://github.com/Luel-Hagos/Tigrigna_Document_To_Json/blob/master/ETL_SAMPLE_DICT01.json) and [ETL_SAMPLE_DICT02.json](https://github.com/Luel-Hagos/Tigrigna_Document_To_Json/blob/master/ETL_SAMPLE_DICT02.json) are the output json files.
* When you run the program make sure that you are in the same diroctary with ETL_SAMPLE_DICT.zip , unless you specified the path of it.


