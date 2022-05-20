"""Download files from collab"""
import os

import requests
from webdav3.client import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

HOST="https://collab.its.virginia.edu"
site_list_endpoint = f"{HOST}/direct/site.json"
cookie = os.environ['COOKIE']
webdav_token = os.environ['WEBDAV_TOKEN']
computing_id = os.environ['COMPUTING_ID']

page = 1
sites = []
while True:
    headers = {
      'Cookie': cookie
    }
    params = {
        'page': page
    }
    response = requests.get(site_list_endpoint, headers=headers, params=params)
    site_collection = response.json()['site_collection']
    if len(site_collection) == 0:
        break
    sites += site_collection
    page += 1

print([site['entityTitle'] for site in sites])
for site in sites:
    id = site['entityId']
    webdav_host = f'{HOST}/dav/{id}'
    options = {
        'webdav_hostname': webdav_host,
        'webdav_login': computing_id,
        'webdav_password': webdav_token,
    }
    client = Client(options)
    print(client.list())
