from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkTextbox, DISABLED, NORMAL, END  # customtkinter
from threading import Thread
from socket import gethostbyname
from requests import get
from time import sleep


def url_info_page():

    def scan_button():
        def adding(txt):
            res_box.configure(state=NORMAL)
            res_box.insert(END, str(txt)+'\n')
            res_box.configure(state=DISABLED)
        def scan():
            try:
                res_box.configure(state=NORMAL)
                res_box.delete(1.0, END)
                res_box.configure(state=DISABLED)
                addr = addr_entry.get()
                def domain_2_ip(name):
                    try:
                        ipadd = gethostbyname(name)
                        adding(f'[+]    IP ADDRESS  : {ipadd}')
                    except Exception:
                        adding(f'[+]    IP ADDRESS  : COUDNT GET IP') 

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
                                    targetipa = str(gethostbyname(targetbase))
                                except:
                                    targetipa = ''
                                    adding("[!]    ERROR")
                        except:
                            adding("[!]    ERROR ")
                        try:
                            # print('')
                            adding(f"[+]    SITE  : {targetbase}")
                            domain_2_ip(name=targetbase)
                            adding(f"[+]    SERVER  : {get(url=targetwithprotocol).headers['Server']}")
                            adding(f"[+]    CONTENT TYPE  : {get(url=targetwithprotocol).headers['Content-type']}")
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
                                adding(f"[+]    {txt}{' '*(14-len(txt)*2)}:{r[(r.index(':'))+1:]}")
                                sleep(0.1)
                            
                        except Exception as er:
                            print(er)
                            adding("[!]    ERROR 3")
                    except Exception:
                        adding('[!]    ERROR OCCURRED ')


                ip_information(addr)

            except Exception:
                adding('ERROR OUCCURRED ')
        
        Thread(target=scan).start()



    root = CTk()
    root.geometry('670x560')
    root.title('URL INFO')
    uframe = CTkFrame(master=root, border_color='red', border_width=2)
    title = CTkLabel(master=uframe, text='URL INFO', font=('montserrat', 35, 'bold'))
    addr_lbl = CTkLabel(uframe, text='ADDRESS : ', font=('montserrat', 28, 'bold'))
    show_button = CTkButton(uframe, text='SCAN', width=471, height=35, font=('montserrat', 22, 'bold'), command=scan_button)
    addr_entry = CTkEntry(uframe, width=220, height=40, font=('montserrat', 22, 'bold'), placeholder_text='https://site.ir')
    res_box = CTkTextbox(uframe, width=471, height=200,  font=('montserrat', 18))
    res_box.configure(state=DISABLED)
    close_button = CTkButton(uframe, text='CLOSE', width=471, height=35, font=('montserrat', 22, 'bold'),fg_color='red' , hover_color='#A82B2B', command=lambda: root.destroy())


    title.place(x=210, y=30)
    uframe.pack(padx=20, pady=20, expand=True, fill = 'both')
    addr_lbl.place(x=80, y=130)
    addr_entry.place(x=330, y=130)
    show_button.place(x=80, y=190)
    res_box.place(x=80, y=240)
    close_button.place(x=80, y=455)


    root.mainloop()



if __name__ == '__main__':
    url_info_page()