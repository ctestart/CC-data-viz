### Script to read link data from link-date-rel files
### C Testart

import json

with open('20190901_20190901.link-date-rel', 'r') as jsonfile:
	data = json.load(jsonfile)
print len(data)