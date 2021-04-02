### Script to read link data from link-date-rel files
### C Testart

import json

with open('20171201_20201001.link-date-rel', 'r') as jsonfile:
	data = json.load(jsonfile)
print len(data)
