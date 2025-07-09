from requests import get
from banner_cli import rtxt, ytxt, ctxt

def diretory_search():
    try:
        bugs = {
            "readme.html" : "Show WordPress version",
            "xmlrpc.php" : "You can DDos to It file",
            "wp-cron.php" : "You can DDos to It file",
            "info.php" : "Show all site Info (System server, sql info, ...)",
            "license.txt" : "Show site info",
            "robots.txt" : "Show ROBOT Api info",
            "?auther=1" : "Username Login site",
            "wp-json/wp/v2/users" : "You can go to it, search 'auther' and show username login site",
            "wp-links-opm.php" : "",
            "wp-traceback.php" : "",
            "wp-mail.php" : "Go to mail site",
            "wp-settings.php" : "Show Error in site",
            "auther-sitemap.xml" : "Show all user site",
            "wp-config-sample.php" : "You can try download it file and show username and password DB",
            "phpmyadmin" : "you can try crack it page and show info DB",
            "wp-admin" : "Login page site",
            "wp-content/uploads/" : "show uploaded file in the server",            
        }
        ctxt("[?]    ENTER THE URL [ex. https://site.ir] : ", end="")
        site = input("")
        ctxt('[~]    SCANNING STARTED ')
        for bug in bugs:
            url = f"{site}/{bug}"
            status = get(url=url)

            if status.status_code == 200:
                rtxt(f"\n[+]  >> URL --> {url}\n     -- STATUS CODE : {status}\n     -- INFO EXPLOIT : {bugs[bug]}\n")
            elif status.status_code != 200:
                pass    
        ctxt('[~]    SCANNING FINISHED ')

    except Exception as er:
        print(er)
        ytxt("[!] --ERROR")


def auto_diretory_search(site):
    try:
        bugs = {
            "readme.html" : "Show WordPress version",
            "xmlrpc.php" : "You can DDos to It file",
            "wp-cron.php" : "You can DDos to It file",
            "info.php" : "Show all site Info (System server, sql info, ...)",
            "license.txt" : "Show site info",
            "robots.txt" : "Show ROBOT Api info",
            "?auther=1" : "Username Login site",
            "wp-json/wp/v2/users" : "You can go to it, search 'auther' and show username login site",
            "wp-links-opm.php" : "",
            "wp-traceback.php" : "",
            "wp-mail.php" : "Go to mail site",
            "wp-settings.php" : "Show Error in site",
            "auther-sitemap.xml" : "Show all user site",
            "wp-config-sample.php" : "You can try download it file and show username and password DB",
            "phpmyadmin/index.php" : "you can try crack it page and show info DB",
            "PhpMyAdmin/index.php" : "you can try crack it page and show info DB",
            "phpMyAdmin/index.php" : "you can try crack it page and show info DB",
            "wp-admin" : "Login page site",
            "wp-content/uploads/" : "show uploaded file in the server"            
        }
        for bug in bugs:
            url = f"{site}/{bug}"
            status = get(url=url)

            if status.status_code == 200:
                rtxt(f"\n[+]  >> URL --> {url}\n     -- STATUS CODE : {status}\n     -- INFO EXPLOIT : {bugs[bug]}\n")
            elif status.status_code != 200:
                pass

    except Exception:
        ytxt("[!] --ERROR")
