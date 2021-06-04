import json

import requests
from stem import Signal
from stem.connection import IncorrectPassword
from stem.control import Controller


class ProxyManager:
    def __init__(self, password, reset_after=2):
        self.reset_after = reset_after
        self.request_count = 0
        self.password = password

        self.last_session = None
        self.updating_ip = False

        self.check_connection()

    def check_connection(self):
        try:
            self.get("http://httpbin.org/ip")
            self.renew_connection()
        except requests.exceptions.ConnectionError:
            print("[!] Please run 'python manage.py startbridge' before running the script.")
            quit()
        except IncorrectPassword:
            print("[!] Incorrect password, you can use 'python manage.py setpassword' to create new password.")
            quit()

    def get_current_ip(self):
        data = json.loads(self.get("http://httpbin.org/ip").text)
        return data.get("origin")

    def reset_ip_if_required(self):
        if self.updating_ip:
            return

        self.updating_ip = True

        if self.request_count >= self.reset_after:
            self.renew_connection()
            self.request_count = 0

        self.updating_ip = False

    def get_session(self):
        self.reset_ip_if_required()
        self.request_count += 1

        session = requests.Session()
        session.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }
        self.last_session = session

        return session

    def __request(self, *args, method="GET", use_last_session=False, **kwargs):
        session = self.last_session if (use_last_session and self.last_session) else self.get_session()

        if method == "GET":
            return session.get(*args, **kwargs)
        elif method == "POST":
            return session.post(*args, **kwargs)
        else:
            raise ValueError(f"'{method}' METHOD NOT FOUND.")

    def post(self, *args, use_last_session=False, **kwargs):
        return self.__request(*args, use_last_session=use_last_session, method="POST", **kwargs)

    def get(self, *args, use_last_session=False, **kwargs):
        return self.__request(*args, use_last_session=use_last_session, method="GET", **kwargs)

    def renew_connection(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=self.password)
            controller.signal(Signal.NEWNYM)
