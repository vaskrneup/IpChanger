import os
import sys

from utils.settings import set_password, start_bridge, get_new_ip, get_current_ip, set_ip_change_interval

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

COMMANDS = {
    "setpassword": {
        "command": lambda: set_password(BASE_DIR),
        "help": "Sets the password, this must be used if ever the password is required."
    },
    "startbridge": {
        "command": lambda: start_bridge(BASE_DIR),
        "help": "Starts the bride."
    },
    "getproxies": {
        "command": lambda: print("socks5://127.0.0.1:9050"),
        "help": "Gives proxy to use externally."
    },
    "getnewip": {
        "command": lambda: get_new_ip(BASE_DIR, sys.argv[2:]),
        "help": "Gets new IP, FORMAT: 'python manage.py getnewip <PASSWORD>'"
    },
    "getcurrentip": {
        "command": lambda: get_current_ip(BASE_DIR, sys.argv[2:]),
        "help": "Gets current IP, FORMAT: 'python manage.py getnewproxy <PASSWORD>'"
    },
    "setipchangeinterval": {
        "command": lambda: set_ip_change_interval(BASE_DIR, sys.argv[2:]),
        "help": "Changes IP in given , FORMAT: 'python manage.py setipchangeinterval <PASSWORD> <TIME IN SECONDS>'"
    }
}


def main():
    args = sys.argv

    if len(args) > 1:
        sub_command = args[1]
        if sub_command in COMMANDS:
            COMMANDS[sub_command]["command"]()
        else:
            print("[!] Command Not Found.")
    else:
        print(f"{'COMMAND':<20} | HELP TEXT")
        print("-------------------------------------------------------")
        for command in COMMANDS:
            print(f"{command:<20} | {COMMANDS[command]['help']}")


main()
