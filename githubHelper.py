import urllib2
import json

import requests
from requests.auth import HTTPBasicAuth

import time

lastCall = ''

class Model:
	def __init__(self, name, url):
		self.name = name
		self.url = url

class githubHelper(object):
	def __init__(self, username, repo, branch, password = None):
		self.username = username
		self.repo = repo
		self.branch = branch
		self.password = password

	def getGithubModels(self):
		#check if enough time has passed
		if(self.rateCheck):
			#fetch files from repo/branch and stl folder
			data = requests.get('https://api.github.com/repos/'+ self.username +'/' + self.repo + '/contents/stl', auth=HTTPBasicAuth(self.username, self.password))
			data = data.json()
			files = list()
			for elem in data:
				if(elem['type'] == 'file'):
					crtfilename = elem['name']
					files.append(Model(crtfilename[:-4], crtfilename))

			return files
		else:
			return None

	def rateCheck(self):
		if(lastCall == None):
			lastCall = localtime()
			return True

		crtTime = localtime()
		if(self.password == None and (crtTime - lastCall) < 60 or \
			self.password != None and (crtTime - lastCall) < 1):
			return False
		else:
			lastCall = crtTime
			return True