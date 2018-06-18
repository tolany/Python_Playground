#-*- coding: utf-8 -*-

import json 

jsondocu = open('data-text.json').read()
data = json.loads(jsondocu)

for item in data:
    print item 
