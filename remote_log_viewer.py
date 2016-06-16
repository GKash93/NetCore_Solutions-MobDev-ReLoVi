############ SHEBANG#########
#!/usr/bin/env python
######### IMPORT FILES AND SCRIPTS#################
import sys, re
from datetime import datetime
######SET ARGUMENTS FOR CMD LINE####################
file_name = sys.argv[1]                           #LOGFILE NAME
frmdt = sys.argv[2]                               #FROM_DATE
todt = sys.argv[3]                                #TO_DATE
wrd = sys.argv[4]                                 #WORD
######SET MATCHING EXPRESSION###################
w = re.compile(r'%s' % (wrd))                                   #WORD EXPRESSION
#########OPEN FILE AND SEARCH EACH LINE FOR PATTERN############
for line in open(file_name,"r"):                  #Read every line in the LogFile and search for pattern
	frm_dt = frmdt + ' 00:00:00'
	to_dt = todt + ' 23:59:59'
	dt1 = datetime.strptime(frm_dt, "%Y-%m-%d %H:%M:%S")
	dt2 = datetime.strptime(to_dt, "%Y-%m-%d %H:%M:%S")
	date_re = re.compile(r'(\d+-\d+-\d+\s\d+:\d+:\d+)')
	match_date = date_re.search(line)
	matchonly = match_date.group(1)
	dt_match = datetime.strptime( matchonly, '%Y-%m-%d %H:%M:%S')
	if dt_match >= dt1 and dt_match <= dt2:
            wrd_re = re.compile(r'%s' % (wrd))
	    match_word = wrd_re.search(line)
            if match_word:
	        line.replace("\n", "<br/>", 10)
	        print line
