#! /usr/bin/python
# -*- coding: utf-8 -*-

# ==================================================================== #
# Libs to install, usage: pip install <NAME>
# Example: pip install godaddypy
import pif
import sys 
import os.path 
from godaddypy import Client, Account
# ==================================================================== #
# ==================================================================== #
# goDaddy API Tokens 
# Reference: https://developer.godaddy.com/
# Reference lib godaddypy: https://pypi.org/project/GoDaddyPy/
api_key = 'API KEY HERE'
api_secret = 'API SECRET HERE'
# goDaddy API Tokens 
# ==================================================================== #
userAccount = Account(api_key, api_secret)
client = Client(userAccount)

if len(sys.argv) != 4:
	print ("Usage: python update_godaddy.py DOMAIN SUB-DOMAIN IP")
	sys.exit(0)
	
domain = sys.argv[1]
name_domain = sys.argv[2]
ip_add = sys.argv[3]

def config_domain(domain, ip_add, name_domain):
	if (len(domain) == 0 or len(ip_add) == 0 or len(name_domain) == 0):
		print('Empty variables, sorry :(')
		sys.exit(0)
	# Update domain and sub-domain
	client.add_record(domain, {'data':ip_add,'name':name_domain,'ttl':3600, 'type':'A'})
	
	# Get results in goDaddy Api
	domains_response = client.get_records(domain, record_type='A')
	for i in domains_response:
		print('domain: ' + i['name'].encode("utf-8") + '.' + domain + ' | ip: ' + i['data'].encode("utf-8"))

# function call		
config_domain(domain, ip_add, name_domain)	
