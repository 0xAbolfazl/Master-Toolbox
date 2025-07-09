from requests import get
from banner_cli import rtxt, ctxt, mtxt
from os import path 
from getpass import getuser



def sub(uurl, api_k):
    ml = ['https://www.', "http://www.",'https://', 'http://']
    for i in ml:
        try:
            if i in uurl:
                uurl = uurl.replace(i, "")
                break
        except Exception:
            pass
    def saving(data):
        num = 0
        while True:
            defpath = fr"C:\Users\{getuser()}\Desktop\subdomain{num}.txt"
            if not path.exists(defpath):
                save = open(defpath, 'w', encoding='utf-8')
                for i in data:
                    save.write(f"{i}\n")
                save.write(f"\n\n\n#########################\n##<-- BY MASTER TOOL BOX -->##\n#########################")
                save.close
                break
            else:
                num+=1
        return defpath
    def getting_subdomain(addr):
        api_key = api_k  # https://user.whoisxmlapi.com/settings/general
        requ = get(f'https://subdomains.whoisxmlapi.com/api/v1?apiKey={api_key}&domainName={addr}')
        res = str(requ.text.split(","))
        res = res[3:-4]
        res = res.replace(f'"search":"{addr}"', '')
        res = res.replace("""', '"result":{""", "")
        res = res.replace('"records":[', '')
        domint = int(res.count('domain'))
        res = res.replace(f'"count":{domint}', '')
        res = res.split("', '")
        x = 1
        global subdom
        subdom = []
        for i in range(int((len(res)-1)/3)):
            subdom.append(res[x][11:-1])
            x+=3 
        global adr
        adr = saving(data=subdom) 


    try:       
        getting_subdomain(uurl)
        ctxt(f"{len(subdom)} SUBDOMAIN HAS BEEN FOUNDED AND SAVED TO {adr}!")


    except Exception as e:
        print(e)
        rtxt("[!]    ERROR OCCURRED WHILE WORKING WITH WHOISXML API")



def ssubdomain_func():
    try:
        ctxt("[?]    ENTER YOUR URL : [ex. https://www.site.ir] ", end="")
        uurl = input()
        ctxt("[?]    ENTER YOUR API KEY FROM WHOISXMLAPI : (DEFAULT -> PRESS ENTER)", end="")
        whois_xml_api_key = input()
        if whois_xml_api_key == '':
            sub(uurl=uurl, api_k='at_XoA4R4WAgXhKQckw6UMmBWjVn1iaa')
        elif whois_xml_api_key != '':
            sub(uurl=uurl, api_k=whois_xml_api_key)
    except Exception:
        rtxt('[!]    ERROR OCCURRED !')

def full_scanner_subdomain_finder(uurl):
    try:
        # ctxt("[?]    Enter URL : [ex. https://www.site.ir] ", end="")
        # uurl = input()
        sub(uurl=uurl, api_k='at_XoA4R4WAgXhKQckw6UMmBWjVn1iaa')
    except Exception:
        rtxt('[!]    ERROR OCCURRED !')