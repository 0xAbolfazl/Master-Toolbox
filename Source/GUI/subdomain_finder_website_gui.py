from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkTextbox, DISABLED, NORMAL, END  # customtkinter
from threading import Thread
from getpass import getuser
from os import path
from requests import get
from tkinter import messagebox



def subdomain_finder_page():

    def scan_button():
        def adding(txt):
            res_box.configure(state=NORMAL)
            res_box.insert(END, str(txt)+'\n')
            res_box.configure(state=DISABLED)
        def scan():
            # at_XoA4R4WAgXhKQckw6UMmBWjVn1iaa
            uurl = str(addr_entry.get())
            if uurl == '':
                adding('ENTER VALID ADDRESS')
                raise TypeError
            if api_entry.get() == '':
                api_k = 'at_XoA4R4WAgXhKQckw6UMmBWjVn1iaa'
                # api_k = 'at_gZrcBV6rp8X1X0y5X4lNXc6n0FOri'
            elif api_entry.get() != '':
                api_k = api_entry.get()



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
                        save.write(f"\n\n\n############################################\n##<-- BY MASTER TOOL BOX - GUI VERSION -->##\n############################################")
                        save.close
                        break
                    else:
                        num+=1
                return defpath
            def getting_subdomain(addr):
                try:
                    adding('SCANNING STARTED !')
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
                    print(er)
                    adding(er)
            def output():
                    adding('SCANNING FINISHED !')
                    if len(subdom) == 0:
                        adding('NOTHING FOUND')
                    if len(subdom) != 0:
                        adding('SAVING DATA')
                        global adr
                        adr = saving(data=subdom) 
                        adding(f"{len(subdom)} SUBDOMAIN HAS BEEN FOUNDED AND SAVE TO \n{adr}!")
                        def msg():
                            messagebox.showinfo('RESULT' ,f"{len(subdom)} SUBDOMAIN HAS BEEN FOUNDED AND SAVE TO \n{adr}!")
                        def show_res():
                            adding('-----------------------------------------------------------------')
                            for i in subdom:
                                adding(i)
                        Thread(target=msg).start()
                        Thread(target=show_res).start()
            res_box.configure(state=NORMAL)
            res_box.delete(1.0, END)
            res_box.configure(state=DISABLED)       
            getting_subdomain(uurl)
            output()



        Thread(target=scan).start()

    root = CTk()
    root.geometry('720x620')
    root.title('SUBDOMAIN FINDER')
    sframe = CTkFrame(master=root, border_color='red', border_width=2)
    title = CTkLabel(master=sframe, text='SUBDOMAIN FINDER', font=('montserrat', 35, 'bold'))
    show_button = CTkButton(sframe, text='SCAN', width=521, height=35, font=('montserrat', 22, 'bold'), command=scan_button)
    addr_lbl = CTkLabel(sframe, text='ADDRESS : ', font=('montserrat', 28, 'bold'))
    addr_entry = CTkEntry(sframe, width=270, height=40, font=('montserrat', 19, 'bold'), placeholder_text='https://www.site.ir')
    api_lbl = CTkLabel(sframe, text='API KEY : ', font=('montserrat', 28, 'bold'))
    api_entry = CTkEntry(sframe, width=270, height=40, font=('montserrat', 16, 'bold'), placeholder_text='for default let it empty')
    res_box = CTkTextbox(sframe, width=521, height=200,  font=('montserrat', 16))
    res_box.configure(state=DISABLED)
    close_button = CTkButton(sframe, text='CLOSE', width=521, height=35, font=('montserrat', 22, 'bold'),fg_color='red' , hover_color='#A82B2B', command=lambda: root.destroy())


    title.place(x=140, y=30)
    sframe.pack(padx=20, pady=20, expand=True, fill = 'both')
    addr_lbl.place(x=80, y=130)
    addr_entry.place(x=330, y=130)
    api_lbl.place(x=80, y=190)
    api_entry.place(x=330, y=190)
    show_button.place(x=80, y=250)
    res_box.place(x=80, y=300)
    close_button.place(x=80, y=515)


    root.mainloop()



if __name__ == '__main__':
    subdomain_finder_page()