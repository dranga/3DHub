from flask import Flask, redirect, request, url_for, render_template
import sys
import argparse
import getpass

import githubHelper

# config
# server will reload on source changes, and provide a debugger for errors
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__) # consume the configuration above

#githubUser = ' '
#githubRepo = ' '
#githubBranch = ' '
#githubAuth = ' '

class Model:
	def __init__(self, name, url):
		self.name = name
		self.url = url

# decorator which tells flask what url triggers this fn
@app.route('/', methods=['GET', 'POST'])
def index():
	project_url = "/"
	project_name = "Project Hello World"
	#get models
	#models = gh.getGithubModels()
	global models
	#if models from call empty don't reassign
	#models = Model("qwerty", "qwerty"), Model("asdf", "asdf")
	models = gh.getGithubModels() 

	state = request.args.get('URL','')
	return render_template('index.html', project_url = project_url, project_name = project_name, \
		models = models, state = state, username = githubUser, repo = githubRepo, branch = githubBranch)

# start the application if this is the main python module (which it is)
if __name__ == "__main__":
	
	#argument parsing
	parser = argparse.ArgumentParser()
	parser.add_argument("port", help = "port on which to run on")
	parser.add_argument("username", help = "Github username")
	parser.add_argument("repo", help = "Github repository")
	parser.add_argument("branch", help = "Github branch")
	parser.add_argument("auth", help = "Github Personal token")
	args = parser.parse_args()

	port = int(args.port)
	
	global githubUser
	githubUser = args.username

	global githubRepo
	githubRepo = args.repo

	global githubBranch
	githubBranch = args.branch

	global githubAuth
	#githubAuth = getpass.getpass("Github Personal access token : ")
	githubAuth = args.auth

	global gh
	gh = githubHelper.githubHelper(githubUser, githubRepo, githubBranch, githubAuth)
  	
  	#, use_reloader=False
  	app.run(host='0.0.0.0', port=port)
