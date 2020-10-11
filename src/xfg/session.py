import logging
import requests
from .page_parsing import parse_tables


class Session(object):
    """docstring for Session"""
    def __init__(self, address="10.0.0.1", username="admin", password="password"):
        super(Session, self).__init__()
        self.address = address
        self.username = username
        self.password = password
        self.connected = False
        self.session = requests.session()
        self.base_url = f"http://{self.address}"
        logging.debug(f"base_url: {self.base_url}")
        self.login()

    def post(self, page, data):
        logging.debug(f"posting to: {page}")
        return self.session.post(f"{self.base_url}/{page}", data=data)

    def login(self):
        auth = {
            'username': self.username,
            'password': self.password,
        }
        result = self.post(page="check.php", data=auth).status_code
        if result != 200:
            logging.error(f"Login Failed!")
            exit(1)

    def xfinity_network(self, page="network_setup.php"):
        return parse_tables(self.session.get(f"{self.base_url}/{page}").content)
