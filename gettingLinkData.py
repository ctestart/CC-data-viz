import sys
import json
from datetime import date
from collections import defaultdict

def next_month_date(initial_date):
    month = initial_date.month
    year = initial_date.year + month // 12
    month = month % 12 + 1
    return date(year, month, initial_date.day)


asn_list = ['133416', '134202', '137510', '136749', '139761', '140866', '135017', '111', '10961', '138995', '4847', '42962', '17767', '327776', '328328', '136796', '35145', '55720', '131297', '135026', '42909', '55720', '132825', '133448', '135026', '133771', '139265', '139269', '131651', '139761', '140866' ]


start_date = '20190901'
end_date = '20200901'
if len(sys.argv) >2:
	start_date = sys.argv[1]
	end_date = sys.argv[2]

d= date(year=int(start_date[:4]), month = int(start_date[4:6]), day = int(start_date[6:]))
end = date(year=int(end_date[:4]), month = int(end_date[4:6]), day = int(end_date[6:]))

# Getting file list
file_path = "ASRelData/"
dates =[]
while(d<=end):
	str_y, str_m, str_d = str(d).split('-')
	dates.append(str_y+str_m+"01")
	d = next_month_date(d)

print '%s files, starting on %s, ending on %s'%(len(dates), start_date, end_date)


#The as-rel files contain p2p and p2c relationships.  The format is:
#<provider-as>|<customer-as>|-1
# #<peer-as>|<peer-as>|0

link_date_rel = defaultdict(list) # for each link the dict returns a list of (date,relationship) tuples

# Readind AS relationship data
for da in dates:
	with open(file_path+da+'.as-rel.txt','r') as of:
		lines = of.readlines()
	link_rels = [tuple(line.strip('\n').split('|')) for line in lines if '#' not in line]
	for link_rel in link_rels:
		# print link_rel
		if link_rel[0] in asn_list or link_rel[1] in asn_list:
			link_date_rel[(link_rel[0]+'|'+link_rel[1])].append((da,link_rel[2]))

#Writing output file (dumping defaultdict as string of json object)
print len(link_date_rel)
outfile_name = start_date+'_'+end_date+'.link-date-rel'
with open(outfile_name,'w') as fout:
	json.dump(link_date_rel, fout, sort_keys=True)

print 'Wrote '+ outfile_name

