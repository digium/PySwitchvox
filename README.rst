About
-----

This package contains a Python client library for the Switchvox Extend API.

This library is only a very thin wrapper around the Extend API Methods, and seeks primarily to provide a Pythonic way of invoking the API.

For more information on the Extend API, see the developer documentation: http://developers.digium.com/switchvox/

Installation
-----

```
python setup.py install
```

Notes
-----
Due to a quirky bug in Switchvox's HTTP server's 401 Challenges, a very recent version of the ```requests``` library is needed. So recent, in fact, that it isn't released yet.

As such, PySwitchvox maintains that it needs requests 2.8.1, when in reality we will need the eventually released 2.8.2. When that release is made, the library dependency in ```setup.py``` will be updated appropriately. Until then, ```requests``` will need to be installed from Github: https://github.com/kennethreitz/requests
