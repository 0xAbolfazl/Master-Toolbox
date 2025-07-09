from requests import get
import time
import socket
from banner_cli import rtxt, ctxt, lbtxt
from socket import gethostbyname

def domain_2_ip(name):
    try:

        xurl = name
    except Exception:
        rtxt('[!]    ERROR OCCURRED [dti] !')
    try:
        ipadd = gethostbyname(xurl)
        lbtxt(f'[+]    IP ADDRESS    : {ipadd}')
    except Exception:
        rtxt(f'[+]    IP ADDRESS    : COUDNT GET IP')

        

def ip_information(targetwithprotocol):
    try:
        targetbase = targetwithprotocol
        del_l = ['https://', 'http://']
        try:
            for i in del_l :
                if i in targetwithprotocol:
                    targetbase = targetwithprotocol.replace(i, "")
                    break     
            if "." in targetbase:
                splited_target = targetbase.split(".")          
            if len(splited_target) == 2 or 3:          
                try:
                    targetipa = str(socket.gethostbyname(targetbase))
                except:
                    targetipa = ''
                    rtxt("[!]    ERROR")
        except:
            rtxt("[!]    ERROR ")
        try:
            print('')
            lbtxt(f"[+]    SITE          : {targetbase}")
            domain_2_ip(name=targetbase)
            lbtxt(f"[+]    SERVER        : {get(url=targetwithprotocol).headers['Server']}")
            lbtxt(f"[+]    CONTENT TYPE  : {get(url=targetwithprotocol).headers['Content-type']}")
        except Exception:
            pass

        try:    
            req = get("http://ip-api.com/json/"+targetipa)
            result = req.text.split(",")
            result = result[1:-1]
            myl = [0, 1, 3, 4, 8, 9]
            # print(result)
            for i in myl:
                r = result[i].replace("\""," ")
                r = r.strip()
                txt = (r[:r.index(':')]).upper()
                # print(txt)
                lbtxt(f"[+]    {txt}{' '*(14-len(txt))}:{r[(r.index(':'))+1:]}")
                time.sleep(0.1)
            
        except Exception as er:
            print(er)
            rtxt("[!]    ERROR 3")
    except Exception:
        rtxt('[!]    ERROR OCCURRED !')

def ip_information_runner():
        try:
            ctxt("[?]    ENTER YOUR URL : [ex. https://site.ir] ", end="")
            targetwithprotocol = input()
            if targetwithprotocol == '':
                rtxt('[!]    ENTER VALID ADDRESS !')
                raise TypeError
            ip_information(targetwithprotocol=targetwithprotocol)
        except Exception:
            rtxt('[!]    ERROR OCCURRED !')



def ip_information_gui(targetwithprotocol, resbox):
    def adding(txt, resbox=resbox):
        resbox.configure(state='normal')
        resbox.insert('end', str(txt)+'\n')
        resbox.configure(state='disabled')
    try:
        targetbase = targetwithprotocol
        del_l = ['https://', 'http://']
        try:
            for i in del_l :
                if i in targetwithprotocol:
                    targetbase = targetwithprotocol.replace(i, "")
                    break     
            if "." in targetbase:
                splited_target = targetbase.split(".")          
            if len(splited_target) == 2 or 3:          
                try:
                    targetipa = str(socket.gethostbyname(targetbase))
                except Exception:
                    targetipa = '[+]    TARGET IP     : COUDNT GET'
                    adding("[!]    ERROR OCCURRED")
        except:
            adding("[!]    ERROR OCCURRED ")
        try:
            print('')
            adding(f"[+]    SITE          : {targetbase}")
            # domain_2_ip(name=targetbase)
            adding(targetipa)
            adding(f"[+]    SERVER        : {get(url=targetwithprotocol).headers['Server']}")
            adding(f"[+]    CONTENT TYPE  : {get(url=targetwithprotocol).headers['Content-type']}")
        except Exception:
            pass
        print('going for target ip')
        print(targetipa)
        if targetipa != '[+]    TARGET IP     : COUDNT GET':
            try: 
                print('here')   
                req = get("http://ip-api.com/json/"+targetipa)
                result = req.text.split(",")
                result = result[1:-1]
                myl = [0, 1, 3, 4, 8, 9]
                # print(result)
                for i in myl:
                    print(i)
                    r = result[i].replace("\""," ")
                    r = r.strip()
                    txt = (r[:r.index(':')]).upper()
                    # print(txt)
                    adding(f"[+]    {txt}{' '*(14-len(txt))}:{r[(r.index(':'))+1:]}")
                    time.sleep(0.1)
                
            except Exception as er:
                adding("[!]    ERROR 3")
                adding(er)
    except Exception:
        adding('[!]    ERROR OCCURRED')

if __name__ == '__main__':
    ip_information_runner()