import os
import re
import getpass
import time

from utils.config import CONFIG_FILE_TEMPLATE
from .proxy_manager import ProxyManager


def set_password(base_dir):
    new_password = input("New Password: ")
    password_hash_output = os.popen(f"{base_dir}\\utils\\bridge\\Tor\\tor.exe --hash-password {new_password}").read()
    password_hash = password_hash_output.strip().split("\n")[-1].strip()

    if os.path.exists(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\tor\\torrc"):
        with open(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\tor\\torrc", "r") as f:
            file_data = f.read()
            old_hash = re.search(r"HashedControlPassword\s(.*)\n", file_data)
            if old_hash:
                config_file_data = file_data.replace(old_hash.group(1), password_hash)
            else:
                raise ValueError("Old Hash Not Found.")
    else:
        config_file_data = CONFIG_FILE_TEMPLATE.format(PASSWORD_HASH=password_hash)

    with open(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\tor\\torrc", "w") as f:
        f.write(config_file_data)
        print("[!] Password Updated.")
        print("[!!] If you have a open bridge then close it and run 'python manage.py startbridge' again.")


def start_bridge(base_dir):
    if os.path.exists(f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\tor\\torrc"):
        print(f"[!] Starting bridge.")
        os.system(f"start {base_dir}\\utils\\bridge\\Tor\\tor.exe")
        print(f"[!] Bridge started, please keep the window open when using this script.")
    else:
        print(f"[!] Run 'python manage.py setpassword' before starting the bridge.")


def get_new_ip(_base_dir, args):
    if args:
        print("[!] Changing IP address.")
        proxy_manager = ProxyManager(password=args[0])
        print("[+] IP address changed.")
        print(f"[+] New Address: '{proxy_manager.get_current_ip()}'")
    else:
        print("[!] Password is required, RUN: 'python manage.py getnewip <PASSWORD>'")
        quit()


def get_current_ip(_base_dir, args):
    if args:
        print(f"[+] Current IP Address: '{ProxyManager(password=args[0]).get_current_ip()}'")
    else:
        print("[!] Password is required, RUN: 'python manage.py getcurrentip <PASSWORD>'")
        quit()


def set_ip_change_interval(_base_dir, args):
    if len(args) == 2:
        print("[!] press 'CTRL + C' to exit.")
        while True:
            try:
                time.sleep(int(args[1]))
                get_new_ip(_base_dir, [args[0]])
            except ValueError:
                print("[!] <TIME IN SECONDS> must be a number.")
                quit()
    else:
        print(
            "[!] Password and time is required, RUN: "
            "'python manage.py setipchangeinterval <PASSWORD> <TIME IN SECONDS>'"
        )
        quit()
