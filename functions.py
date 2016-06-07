#!/usr/bin/env python
import psycopg2

conn = psycopg2.connect(database="relovi", user="postgres", password="ganesh", host="127.0.0.1", port="5432")
#--------------------------------------------------------------------------------------
print "Opened Database Sucessfully"
print "Connection Established"
#-------------------------------------------------------------------------------------
cur = conn.cursor()
#--------------------------------------------------------------------------------------
def get_groups():
    cur.execute(" select id, name from Groups ")
    row_gr = cur.fetchall()
    return row_gr
#----------------------------------------------------------------------------------------	
def get_servers(group_id):
    query = "select id, name, g_id from Servers where g_id = %s" % (int(group_id))
    cur.execute(query)
    row_sr = cur.fetchall()
    return row_sr	
#-----------------------------------------------------------------------------------------    
def get_logfiles(server_id):
    query2 = " select id, appname, s_id from LogFiles where s_id= %s" % (int(server_id))
    cur.execute(query2)
    row_lo = cur.fetchall()
    return row_lo
#--------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print "So far so good"
#---------------------------------------------------------------------------------------------
    row_g = get_groups()
    for row_g in row_gr:
	print row_g
#---------------------------------------------------------------------------------------------
    print "Servers "
    row_s = get_servers(group_id)
    for row_s in rows_sr:
	print row_s
#---------------------------------------------------------------------------------------------
    print "Logfiles "
    row_l = get_logfiles()
    for row_l in row_lo:
	print row_l


