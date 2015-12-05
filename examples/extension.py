#!/usr/bin/env python
"""Example of using the sample client to get an extension

Copyright (C) 2015, Digium, Inc.
Matthew Jordan <mjordan@digium.com>
"""

from pyswitchvox.client import Client

URL = '127.0.0.1'
USERNAME = 'admin'
PASSWORD = 'password'

client = Client(URL, USERNAME, PASSWORD)
resp = client.extensions.getInfo(extensions=['100'])

print resp