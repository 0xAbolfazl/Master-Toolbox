from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkTextbox, DISABLED, NORMAL, END  # customtkinter
from threading import Thread
from requests import get


def admin_panel_finder_page():

    def scan_button():
        def adding(txt, sep='--------------------------------------------------------------------'):
            res_box.configure(state=NORMAL)
            if txt != '':
                res_box.insert(END, str(txt)+'\n'+sep+'\n')
            res_box.configure(state=DISABLED)
        def scan():
            try:
                panel_list = list()
                res_box.configure(state='normal')
                res_box.delete(1.0, END)
                res_box.configure(state='disabled')
                site = str(addr_entry.get())
                if site == '':
                    adding('[ ! ] PLEASE ENTER VALID ADDRESS !')
                    raise TypeError
                if site != '':
                    adding('SCANNING STARTED !')
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
                    adding('SCANNING FINISHED !')
                if len(url) == 0:
                    adding('NOTIHNG FOUND !')

            except Exception as er:
                adding("[!]    ERROR")
                adding(er)


        Thread(target=scan).start()

    root = CTk()
    root.geometry('670x560')
    root.title('ADMIN PANEL FINDER')
    aframe = CTkFrame(master=root, border_color='red', border_width=2)
    title = CTkLabel(master=aframe, text='ADMIN PANEL FINDER', font=('montserrat', 35, 'bold'))
    addr_lbl = CTkLabel(aframe, text='ADDRESS : ', font=('montserrat', 28, 'bold'))
    show_button = CTkButton(aframe, text='SCAN', width=471, height=35, font=('montserrat', 22, 'bold'), command=scan_button)
    addr_entry = CTkEntry(aframe, width=250, height=40, font=('montserrat', 19, 'bold'), placeholder_text='https://site.ir')
    res_box = CTkTextbox(aframe, width=471, height=200,  font=('montserrat', 16))
    res_box.configure(state=DISABLED)
    close_button = CTkButton(aframe, text='CLOSE', width=471, height=35, font=('montserrat', 22, 'bold'),fg_color='red' , hover_color='#A82B2B', command=lambda: root.destroy())


    title.place(x=105, y=30)
    aframe.pack(padx=20, pady=20, expand=True, fill = 'both')
    addr_lbl.place(x=80, y=130)
    addr_entry.place(x=300, y=130)
    show_button.place(x=80, y=190)
    res_box.place(x=80, y=240)
    close_button.place(x=80, y=455)


    root.mainloop()



if __name__ == '__main__':
    admin_panel_finder_page()