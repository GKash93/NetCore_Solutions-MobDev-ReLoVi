#!/usr/bin/env python
import ConfigParser
from ConfigParser import ConfigParser

#Using the ConfigParser in Python
config = ConfigParser() 
file = open("config.ini",'r')
config.add_section("Group")
config.add_section("Server")
config.add_section("LogFile")
file.close()

