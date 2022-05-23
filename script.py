"""Download files from collab"""
import os
from functools import cache
from pathlib import Path

import requests
from webdav3.exceptions import RemoteResourceNotFound, NoConnection
from webdav3.client import Client
from tqdm import tqdm
from dotenv import load_dotenv
import logging

logging.getLogger().setLevel(logging.INFO)

load_dotenv()  # take environment variables from .env.

HOST = "https://collab.its.virginia.edu"
EXPORT_DIR = "export"
site_list_endpoint = f"{HOST}/direct/site.json"
cookie = os.environ["COOKIE"]
webdav_token = os.environ["WEBDAV_TOKEN"]
computing_id = os.environ["COMPUTING_ID"]


def list_sites():
    page = 1
    sites = []
    while True:
        headers = {"Cookie": cookie}
        params = {"page": page}
        response = requests.get(site_list_endpoint, headers=headers, params=params)
        response.raise_for_status()
        site_collection = response.json()["site_collection"]
        if len(site_collection) == 0:
            break
        sites += site_collection
        page += 1

    assert len(sites) > 0, "could not access list of sites"
    return sites


sites = list_sites()
print([site["entityTitle"] for site in sites])


def download_sites(sites):
    for site in sites:
        id = site["entityId"]
        name = site["entityTitle"]
        output_dir = Path(EXPORT_DIR) / name
        try:
            output_dir.mkdir(parents=True)
        except FileExistsError:
            logging.info(f"{name} already exists, skipping")
            continue
        webdav_host = f"{HOST}/dav/{id}"
        options = {
            "webdav_hostname": webdav_host,
            "webdav_login": computing_id,
            "webdav_password": webdav_token,
        }
        client = Client(options)
        try:
            client.download(
                remote_path="/", local_path=output_dir, progress=progress_update
            )
        except RemoteResourceNotFound:
            logging.warning(f"could not find any files for {name}")
            continue
        except NoConnection:
            logging.error("Lost connection")
            break


def progress_update(current, total):
    t = tqdm_instance(total)
    t.update(current)


@cache
def tqdm_instance(total):
    return tqdm(total)


download_sites(sites)
