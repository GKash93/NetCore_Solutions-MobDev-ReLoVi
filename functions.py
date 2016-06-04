#!/usr/bin/env python
import psycopg2

conn = psycopg2.connect(database="relovi", user="postgres", password="ganesh", host="127.0.0.1", port="5432")

print "Opened Database Sucessfully"

cur = conn.cursor()

def get_groups():
    cur.execute(" select id, name from Groups ")
    rows = cur.fetchall()
    return rows 
	
def get_servers(group_id):
    query = "select id, name from servers where g_id = %s" % (int(group_id)) 
    cur.execute(query)
    rows1 = cur.fetchall()
    return rows1	
    
def get_logfiles(server_id):
    cur.execute(" select id, appname, s_id from LogFiles where s_id= %s" % (server_id))
    rows2 = cur.fetchall()
    return rows2

if __name__ == "__main__":
    print "So far so good"
    
    rows = get_groups()
    for row in rows:
	print row
    print "Servers "
    rows1 = get_servers(group_id)
    for row1 in rows1:
	print row1
    print "Logfiles "
    rows2 = get_logfiles()
    for row2 in rows2:
	print row2


