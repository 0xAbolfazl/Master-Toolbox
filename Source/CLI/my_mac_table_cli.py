from subprocess import run
from banner_cli import rtxt, lbtxt


def run_command(command):
    result = run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def my_mac_table():
    try:
        res = run_command('arp -a')
        lbtxt(res)
    except Exception:
        rtxt('[!]    Error occurred while showing mac table !')



if __name__ == '__main__':
    my_mac_table()