from github import Github
import yaml
import requests
import sys
import json

# get github token from command line
token = sys.argv[1]
g = Github(token)

# load org yaml
r = requests.get("https://raw.githubusercontent.com/github/government.github.com/gh-pages/_data/governments.yml")

data = None
try:
    data = yaml.safe_load(r.content)
except yaml.YAMLError as exc:
    print(exc)

# get organizations in Sweden
orgs = data["Sweden"]

# List organizations and their repos
for orgname in orgs:
    org = g.get_organization(orgname)
    for repo in org.get_repos(type="public"):
        if not repo.fork:
            j = {"orgname": org.name, "repo": repo.name, "repo_desc": repo.description, "repo_url": repo.html_url}
            print(json.dumps(j, indent=4))