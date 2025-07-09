from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkTextbox, DISABLED, NORMAL, END  # customtkinter
from tkinter import NORMAL, DISABLED, END
from requests import get
from time import sleep
from socket import gethostbyname, socket, setdefaulttimeout, AF_INET, SOCK_STREAM
import socket
from getpass import getuser
from os import path
from threading import Thread


def admin_panel_finder(addr, res_box):

        def adding(txt, res_box=res_box, sep='\n----------------------------------------------------------------'):
            res_box.configure(state=NORMAL)
            if txt != '':
                res_box.insert(END, str(txt)+sep+'\n')
            res_box.configure(state=DISABLED)

        try:
            panel_list = list()
            site = addr
            adding('---------------------------------------------\nPART 3 -> ADMIN PANEL FINDER\n---------------------------------------------', sep='')
            payload = {
                'wp-login.php' : 'WORDPRESS LOGIN PAGE',
                'login' : 'LOGIN PAGE',
                'admin.php' : 'LOGIN PAGE',
                'admin.html' : 'LOGIN PAGE',
                'index.php' : 'LOGIN PAGE',
                'login.php' : 'LOGIN PAGE',
                'login.html' : 'LOGIN PAGE',
                'administrator' : 'LOGIN PAGE',
                'admin' : 'LOGIN PAGE',
                'adminpanel' : 'LOGIN PAGE',
                'cpanel' : 'CPANEL LOGIN PAGE',
                'login' : 'LOGIN PAGE',
                'administrator' : 'LOGIN PAGE',
                'admins' : 'LOGIN PAGE',
                'logins' : 'LOGIN PAGE',
                'admin.asp' : 'LOGIN PAGE',
                'login.asp' : 'LOGIN PAGE',
            }
            for i in payload.keys():
                url = f"{site}/{i}"
                status = get(url=url)
                if status.status_code == 200:
                    panel_list.append(url)
                    adding(f"[+]   LOGIN PANEL : {url}\n        STATUS CODE : {status}")
            if len(url) != 0:
                    adding('SCANNING FINISHED !', sep='')
            if len(url) == 0:
                adding('NOTIHNG FOUND !', sep='')
            adding('---------------------------------------------\nPART 3 FINISHED \n---------------------------------------------', sep='')

        except Exception as er:
            adding("[!]    ERROR", sep='')
            adding(er)

def ip_information_gui(targetwithprotocol, resbox):
    def adding(txt, resbox=resbox):
        resbox.configure(state='normal')
        resbox.insert('end', str(txt)+'\n')
        resbox.configure(state='disabled')
    try:
        adding('---------------------------------------------\nPART 1 -> IP DETAIL\n---------------------------------------------')
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
                    t_ip = str(gethostbyname(targetbase))
                    targetipa = f'[+]    TARGET IP     : {t_ip}'
                except Exception:
                    targetipa = '[+]    TARGET IP     : COUDNT GET'
                    adding("[ ! ]    ERROR OCCURRED")
        except:
            adding("[ ! ]    ERROR OCCURRED ")
        try:
            print('')
            adding(f"[+]    SITE          : {targetbase}")
            adding(targetipa)
            adding(f"[+]    SERVER        : {get(url=targetwithprotocol).headers['Server']}")
            adding(f"[+]    CONTENT TYPE  : {get(url=targetwithprotocol).headers['Content-type']}")
        except Exception:
            pass

        try:    
            req = get("http://ip-api.com/json/"+t_ip)
            result = req.text.split(",")
            result = result[1:-1]
            myl = [0, 1, 3, 4, 8, 9]
            # print(result)
            for i in myl:
                r = result[i].replace("\""," ")
                r = r.strip()
                txt = (r[:r.index(':')]).upper()
                # print(txt)
                adding(f"[+]    {txt}{' '*(14-len(txt))}:{r[(r.index(':'))+1:]}")
                sleep(0.1)
            adding('---------------------------------------------\nPART 1 FINISHED \n---------------------------------------------')
            
        except Exception as er:
            adding("[ ! ]    ERROR 3")
            adding(er)
    except Exception:
        adding('[ ! ]    ERROR OCCURRED')

def auto_scan_port_gui(ip='empty', resbox='res_box'):
    def adding(txt, resbox=resbox):
        resbox.configure(state='normal')
        resbox.insert('end', str(txt)+'\n')
        resbox.configure(state='disabled')

    adding('---------------------------------------------\nPART 2 -> PORT SCANNER\n---------------------------------------------')

    ports = [21, 22, 23, 25, 53, 80, 110, 115, 111, 135, 137, 138, 139,
                        143, 194, 443, 445, 548, 587, 993, 995, 1701, 1723, 2083,
                        1433, 3306, 3389, 5632, 5432, 8008, 8080, 8443,5900, 25565,
                        515, 631, 3282, 5190, 5050, 4443, 1863, 6891, 1503, 5631, 5632, 6667]
    opens = list()
    final_opens = list()
    if ip != 'empty':
        addr = ip
    address = gethostbyname(addr)

    adding(f"[+]    SCANNING STARTED ON  \n{11*'  '}# ADDRESS : {addr}\n{11*'  '}# IP{7*'  '}: {address}\n{11*'  '}# TIMEOUT : 500(ms)\n{11*'  '}# PORT[S] : DEFAULT")
    for i in range(1):
        for port in (ports):
            try:
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                result = tcp.connect_ex((address, port))
                if result == 0:
                    opens.append(port)
                    tcp.close()
            except Exception:
                adding('[!]    ERROR OCCURRED IN PORT SCANNER !')
                # print(er)
            
    for i in opens:
        if i not in final_opens:
            final_opens.append(i)
    if len(final_opens) != 0:

        adding(f'THESE PORT[S] ARE OPEN : \n{final_opens}')
    adding('---------------------------------------------\nPART 2 FINISHED \n---------------------------------------------')

def subdomain_scan_button(uurl, res_box):
        
        # uurl = uurl
        def adding(txt):
            res_box.configure(state=NORMAL)
            res_box.insert(END, str(txt)+'\n')
            res_box.configure(state=DISABLED)
        adding('SCANNING SARTED !')
        def scan():
            # at_XoA4R4WAgXhKQckw6UMmBWjVn1iaa
            api_k = 'at_XoA4R4WAgXhKQckw6UMmBWjVn1iaa'
            url = uurl
            ml = ['https://www.', "http://www.",'https://', 'http://']
            for i in ml:
                try:
                    if i in url:
                        url = url.replace(i, "")
                        break
                except Exception:
                    adding('ERROR OCCURRED WHILE SCANNING ADDRESS\nCORRECT ADDRESS FORM : https://site.ir')
            def saving(data):
                try:
                    num = 0
                    while True:
                        defpath = fr"C:\Users\{getuser()}\Desktop\subdomain{num}.txt"
                        if not path.exists(defpath):
                            save = open(defpath, 'w', encoding='utf-8')
                            for i in data:
                                save.write(f"{i}\n")
                            save.write(f"\n\n\n############################################\n##<-- BY MASTER TOOL BOX - GUI VERSION -->##\n############################################")
                            save.close
                            break
                        else:
                            num+=1
                    return defpath
                except Exception:
                    adding('ERROR OCCURRED WHILE SAVING DATA !')
            def getting_subdomain(addr):
                try:
                    adding('---------------------------------------------\nPART 4 -> SUBDOMAIN FINDER\n---------------------------------------------')

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
                except Exception as er:
                    # print(er)
                    adding(er)
            def output():
                adding('SCANNING FINISHED !')
                if len(subdom) == 0:
                    adding('NOTHING FOUND')
                if len(subdom) != 0:
                    adding('SAVING DATA ...')
                    global adr
                    adr = saving(data=subdom) 
                    adding(f"{len(subdom)} SUBDOMAIN HAS BEEN FOUNDED AND SAVE TO \n{adr}!")
                    def show_res():
                        # adding('-----------------------------------------------------------------')
                        for i in subdom:
                            adding(i)
                    show_res()
                    # Thread(target=show_res).start()
            res_box.configure(state=NORMAL)     
            getting_subdomain(url)
            output()
            adding('---------------------------------------------\nPART 4 -> FINISHED\n---------------------------------------------')

        try:
            Thread(target=scan).start()
        except Exception:
            adding('[ ! ]  ERROR OCCURED WHILE SCANNING SUBDOMAINS')


def full_scanner_page():

    def scan_button():
        def adding(txt):
            res_box.configure(state=NORMAL)
            res_box.insert(END, str(txt)+'\n')
            res_box.configure(state=DISABLED)
        def scan():
            try:
                res_box.configure(state=NORMAL)
                res_box.delete(1.0, END)
                res_box.insert(END, 'SCANNING STARTED\n')
                res_box.configure(state=DISABLED)
                addr = addr_entry.get()
                # --------  name - ip - cut protocol --------
                addr_with_protocol = addr
                addr_without_protocol = ''

                delete_item = ["https://www.", 'http://www.','https://', 'http://']
                for i in delete_item :
                    if i in addr :
                        addr_without_protocol = addr.replace(i, "")
                        break
                ip = gethostbyname(addr_without_protocol)

                ip_information_gui(addr_with_protocol, res_box)
                auto_scan_port_gui(addr_without_protocol, res_box)
                admin_panel_finder(addr_with_protocol, res_box=res_box)
                subdomain_scan_button(addr_with_protocol, res_box=res_box)

            except Exception as er:
                print(er)

                adding('ERROR OCCURRED ')

        Thread(target=scan).start()

    root = CTk()
    root.geometry('750x560')
    root.title('FULL SCAN')
    fsframe = CTkFrame(master=root, border_color='red', border_width=2)
    title = CTkLabel(master=fsframe, text='FULL SCAN', font=('montserrat', 35, 'bold'))
    addr_lbl = CTkLabel(fsframe, text='ADDRESS : ', font=('montserrat', 28, 'bold'))
    show_button = CTkButton(fsframe, text='SCAN', width=551, height=35, font=('montserrat', 22, 'bold'), command=scan_button)
    addr_entry = CTkEntry(fsframe, width=330, height=40, font=('montserrat', 22, 'bold'), placeholder_text='https://site.ir')
    res_box = CTkTextbox(fsframe, width=551, height=200,  font=('montserrat', 18))
    res_box.configure(state=DISABLED)
    close_button = CTkButton(fsframe, text='CLOSE', width=551, height=35, font=('montserrat', 22, 'bold'),fg_color='red' , hover_color='#A82B2B', command=lambda: root.destroy())


    title.place(x=245, y=30)
    fsframe.pack(padx=20, pady=20, expand=True, fill = 'both')
    addr_lbl.place(x=80, y=130)
    addr_entry.place(x=300, y=130)
    show_button.place(x=80, y=190)
    res_box.place(x=80, y=240)
    close_button.place(x=80, y=455)


    root.mainloop()



if __name__ == '__main__':
    full_scanner_page()

