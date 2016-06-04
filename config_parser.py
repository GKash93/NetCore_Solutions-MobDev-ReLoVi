#!/usr/bin/env python
#-------------------------------------------------------------------------------------------------------
#Import the ConfigParser and from there import ConfigParser
import ConfigParser
from ConfigParser import ConfigParser
#-------------------------------------------------------------------------------------------------------
#Set the ConfigParser
config = ConfigParser()
#Read the Config Parser
config.read("config.ini")
#--------------------------------------------------------------------------------------------------------
#Get the Values and Print it
groups = config.get('Groups','group_list')
#Create Group List
group_list = groups.split(',')
print group_list 
#Create DropDown 
group_drop_down = '<select>\n'
for abc in group_list:
	group_drop_down += '<option>' + (abc) + '</option>\n'
	
group_drop_down += '</select>\n'	
print group_drop_down
#----------------------------------------------------------------------------------------------------------
#Get the values and print it
#group_servers = config.get('Servers','abc')
#Create Server List
#server_list = group_servers.split(',')
#print server_list
#Create DropDown
#server_drop_down = '<select>\n'
#for xyz in server_list:
#	    server_drop_down += '<option>' + (xyz) + '</option>\n'
#server_drop_down += '</select>\n'
#print server_drop_down

		#servers_logs = config.get('LogFile',xyz)
		#logfiles_list = servers_logs.split(',')
		#for pqr in logfiles_list:
		#print '\n' +xyz +'\t' + pqr+'\t'


