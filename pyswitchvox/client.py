"""Extend API Client

Copyright (C) 2015, Digium, Inc.
Matthew Jordan <mjordan@digium.com>
"""

from requests.auth import HTTPDigestAuth
import requests

# Since Switchvox uses a self signed cert, disable the spammy
# warning message.
requests.packages.urllib3.disable_warnings()

class HTTPException(Exception):
    """An exception raised if a non-success response is returned
    """

    def __init__(self, message, status_code):
        super(HTTPException, self).__init__(message)
        self.status_code = status_code


class ExtendAPIError(Exception):
    """An exception raised if an error is returned from the Extend API
    """

    def __init__(self, message, error_code):
        super(ExtendAPIError, self).__init__(message)
        self.error_code = error_code


class Query(object):
    """A query sent to the Extend API
    """

    def __init__(self, name, client):
        self._path = ['switchvox', name]
        self._client = client

    def __getattr__(self, name):
        self._path.append(name)
        return self

    def __call__(self, **kwargs):
        """Invoke the query
        """
        request_json = {'request': {'method': '.'.join(self._path),
                                    'parameters': kwargs}}
        return self._client(query=request_json)


class Client(object):
    """A client back to the Switchvox Extend API
    """

    def __init__(self, address, username, password, timeout=30):
        """Create a new client connection

        Keyword Arguments:
        address  The address of the Switchvox server
        username The admin username
        password The admin password
        timeout  The timeout to use for requests. Defaults to 30.
        """

        self._address = address
        self._session = requests.Session()
        self._session.auth = HTTPDigestAuth(username, password)
        self.timeout = timeout

    def close(self):
        """Close the client connection
        """
        self._session.close()

    def __call__(self, query):
        """Execute a query object
        """

        # Since Switchvox uses self signed certs, we need to not
        # verify the cert
        response = self._session.post('https://' + self._address + '/json',
            json=query,
            timeout=self.timeout,
            verify=False)

        if (response.status_code / 100 != 2):
            raise HTTPException(response.reason, response.status_code)

        json = response.json().get('response')

        errors = json.get('errors')
        if errors:
            if type(errors['error']) is list:
                # Since raising multiple exceptions is a bit silly, simply
                # raise the first
                message = errors['error'][0]['message']
                code = errors['error'][0]['code']
            else:
                message = errors['error']['message']
                code = errors['error']['code']
            raise ExtendAPIError(message, int(code))

        return json

    def __getattr__(self, name):
        """Intercept an attribute retrieval and invoke the API call
        """
        return Query(name, self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        return self.close()
