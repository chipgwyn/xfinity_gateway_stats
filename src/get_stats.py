#!/usr/bin/env python3

import os
import xfg
import json

password = os.getenv('XFG_PASSWD', "password")
connx = xfg.Session(password=password)
print(json.dumps(connx.xfinity_network(), indent=2))
