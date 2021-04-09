### Script to read link data from link-date-rel files
### C Testart

import json

with open('20171201_20201001.link-date-rel', 'r') as jsonfile:
	data = json.load(jsonfile)

#Searching for customer links of a given ASN.
asn_of_interest = '55720'
customer_links= [link for link in data if asn_of_interest+'|' in link and '-1' in list(zip(*data[link]))[1]]
print 'ASN: %s'%asn_of_interest 
print 'Customer links: %d'%len (customer_links)
print 'Dates customer links are visible: '
for link in customer_links:
	print 'Link: %s'%link
	link_dates = [t[0] for t in data[link]]
	link_rels = [t[1] for t in data[link]]
	for rel in link_rels:
		if int(rel)== 0:
			print 'Change in relationship'
	print 'Date count: %d'%len(link_dates)
	print 'Dates: %s'%' '.join(link_dates)

print '###############'
peering_links = [link for link in data if asn_of_interest in link and '0' in list(zip(*data[link]))[1]]
print 'Peering links: %d'%len (peering_links)

print 'Peering links with a change in relationship: '
for link in peering_links:
	link_rels = [int(t[1]) for t in data[link]]
	if -1 in link_rels:
		#Change in relationship
		print 'Change in relationship in link %s'%link
		print ' '.join([t[0]+'('+t[1]+')' for t in data[link]])
			

