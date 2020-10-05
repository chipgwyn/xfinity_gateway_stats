#!/usr/bin/env python3

import os
import json
import logging
import requests
from xfg.parse_contents import parse_tables

logging.basicConfig()

xfg_ip_address = os.getenv("XFG_ADDRESS", "10.0.0.1")
xfg_base_url = f"http://{xfg_ip_address}"
login_url = f"{xfg_base_url}/check.php"
network_setup_url = f"{xfg_base_url}/network_setup.php"
login_creds = {
    'username': 'admin',
    'password': os.getenv('XFG_PASSWD', "password"),
}

with requests.session() as s:
    logging.info(f"Connecing to: {xfg_base_url}")
    s.post(login_url, data=login_creds)
    logging.info(f"Logged in, pulling data (this may take a few seconds)")
    network_setup = s.get(network_setup_url)

data = parse_tables(network_setup.content)
print(json.dumps(data))




