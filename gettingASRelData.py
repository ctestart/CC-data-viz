### This script downloades AS relationship data from CAIDA. 
### You need to sign the Acceptable Use Agreement (https://www.caida.org/data/as-relationships/) to use it.
### C Testart

import sys
import subprocess
from subprocess import Popen, PIPE
from datetime import date

def next_month_date(initial_date):
    month = initial_date.month
    year = initial_date.year + month // 12
    month = month % 12 + 1
    return date(year, month, initial_date.day)

start_date = '20190816'
end_date = '20190901'
if len(sys.argv) >2:
	start_date = sys.argv[1]
	end_date = sys.argv[2]

if int(end_date)<=int(start_date):
	print 'Start date should be earlier than end date.'
	sys.exit()

d= date(year=int(start_date[:4]), month = int(start_date[4:6]), day = int(start_date[6:]))
end = date(year=int(end_date[:4]), month = int(end_date[4:6]), day = int(end_date[6:]))


while(d<=end):
	d = next_month_date(d)
	str_y, str_m, str_d = str(d).split('-')
	link = "https://publicdata.caida.org/datasets/as-relationships/serial-1/"+str_y+str_m+"01.as-rel.txt.bz2"
	print link
	subprocess.call(["wget", link])
