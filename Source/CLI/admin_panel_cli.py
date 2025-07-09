from requests import get
from banner_cli import rtxt, gtxt, ytxt, lmtxt, ctxt



def admin_panel_finder():
    try:
        valid = []
        ctxt("[?]    Enter URL : [ex. https://site.ir] ", end="")
        site = input("")
        lmtxt('[~]    SCANNING STARTED !')
        payload = {
            'wp-login.php' : 'Wordpress login page',
            'login' : 'Login page',
            'admin.php' : 'Login page',
            'admin.html' : 'Login page',
            'login.php' : 'Login page',
            'login.html' : 'Login page',
            'administrator' : 'Login page',
            'admin' : 'Login page',
            'adminpanel' : 'Login page',
            'cpanel' : 'Cpanel login page',
            'login' : 'Login page',
            'administrator' : 'Login page',
            'admins' : 'Login page',
            'logins' : 'Login page',
            'admin.asp' : 'Login page',
            'login.asp' : 'Login page',
        }
        for i in payload.keys():
            url = f"{site}/{i}"
            admin = get(url=url)
            if admin.status_code == 200:
                valid.append(i)
                if len(valid) != 0:
                    rtxt(f"\n[+]  >> Login Panel --> {url}\n     -- status code : {admin}\n     -- info exploit : {payload[i]}\n")
                else:
                    rtxt('[!]    NOTHING FOUND')

    except Exception as er:
        print(er)
        rtxt("[!]    ERROR")


def auto_admin_panel_finder(site):
    try:
        # gtxt("[~] Trying to Find Admin page ...")
        payload = {
            'wp-login.php' : 'Wordpress login page',
            'login' : 'Login page',
            'admin.php' : 'Login page',
            'admin.html' : 'Login page',
            'index.php' : 'Login page',
            'login.php' : 'Login page',
            'login.html' : 'Login page',
            'administrator' : 'Login page',
            'admin' : 'Login page',
            'adminpanel' : 'Login page',
            'cpanel' : 'Cpanel login page',
            'login' : 'Login page',
            'administrator' : 'Login page',
            'admins' : 'Login page',
            'logins' : 'Login page',
            'admin.asp' : 'Login page',
            'login.asp' : 'Login page',
        }
        for i in payload.keys():
            url = f"{site}/{i}"
            admin = get(url=url)
            if admin.status_code == 200:
                rtxt(f"\n[+]  >> Login Panel --> {url}\n     -- status code : {admin}\n     -- info exploit : {payload[i]}\n")
        gtxt('\n--------------------------------------')
    except Exception as er:
        rtxt("[!]    ERROR")
        print(er)


if __name__ == '__main__':
    admin_panel_finder()