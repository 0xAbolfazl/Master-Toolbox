from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, CTkEntry, END, NORMAL, DISABLED, ctk_tk
from tkinter import ttk, CENTER, BOTH, RIGHT, Y, VERTICAL, messagebox
from threading import Thread
import pywifi
from pywifi import const
from time import sleep





def wifi_tools_page():


    def scan_button_func():
        def wifi_scanner():
            for i in tree.get_children():
                tree.delete(i)
            items = []
            finall = []

            wifi = pywifi.PyWiFi()
            interface = wifi.interfaces()[0]
            # print(interface.name())

            for i in (range(1)):
                interface.scan()
                sleep(3) 
                x = interface.scan_results()
                if len(x) != 0:
                    for i in x:
                        items.append([i.ssid, i.bssid, str(i.freq)])

                if len(items) != 0:
                    for i in items:
                        if i not in finall:
                            finall.append(i)

                    for i in finall:
                        index_c = int(finall.index(i))
                        name_c = str(finall[index_c][0])
                        bssid_c = str(finall[index_c][1])
                        freq_c = str(((float(finall[index_c][2]))/1000000).__round__(1))
                        tree.insert('', 'end', values=(str(index_c), name_c, bssid_c, freq_c))
                        # print((index_c, name_c, bssid_c, freq_c))



            if len(items) == 0:
                messagebox.showerror('ERROR', 'NOTHING FOUND')

        Thread(target=wifi_scanner).start()



    def connect_button_func():

        def connect_func():

            try:
                selected_item = tree.selection()
                ssid = tree.item(selected_item)['values'][1]
            except Exception:
                ssid = ''

            def adding(text):
                where = res_box
                where.configure(state=NORMAL)
                where.delete(1.0, END)
                where.insert(END, text)
                where.configure(state=DISABLED)


            def conn_handler():
                def conn():

                    adding('CONNECTING ...')
                    profile = pywifi.Profile()
                    profile.ssid = str(ssid_entry.get())
                    print(str(ssid_entry.get()))
                    profile.auth = const.AUTH_ALG_OPEN
                    profile.akm.append(const.AKM_TYPE_WPA2PSK)
                    profile.cipher = const.CIPHER_TYPE_CCMP
                    profile.key = str(pass_entry.get())
                    print(profile.key)
                    wifi = pywifi.PyWiFi()
                    iface = wifi.interfaces()[0]
                    print(iface)
                    print(wifi.interfaces())
                    profile = iface.add_network_profile(profile)
                    iface.connect(profile)
                    sleep(5)
                    if iface.status() == const.IFACE_CONNECTED:
                        adding("[+]    CONNECTED SUCCESSFULLY !")
                    else:
                        adding("[!]    CONNECTION FAILD !")

                Thread(target=conn).start()



            croot = CTk()
            croot.title('CONNECT 2 WIFI')
            croot.geometry('600x500')
            croot.resizable(False, False)
            set_appearance_mode("dark")
            set_default_color_theme("blue")
            cframe = CTkFrame(master=croot, corner_radius=10, border_width=2, border_color='red')
            ttitle = CTkLabel(master=cframe, text='CONNECT TO WIFI', font=('montserrat', 30, 'bold'))
            # --------------------------------------------------------
            cframe.pack(padx=20, pady=20, fill='both', expand=True)
            ttitle.place(x=130, y=30)

            ssid_label = CTkLabel(cframe, text='SSID : ', font=('montserrat', 23, 'bold'))
            ssid_label.place(x=90, y=130)

            ssid_entry = CTkEntry(cframe, width=200, height=40, font=('montserrat', 20, 'bold'))
            ssid_entry.insert(END, string=ssid)
            ssid_entry.place(x=280, y=130)

            pass_label = CTkLabel(cframe, text='PASSWORD : ', font=('montserrat', 23, 'bold'))
            pass_label.place(x=90, y=190)
            pass_entry = CTkEntry(cframe, width=200, height=40, font=('montserrat', 20, 'bold'), show='*')
            pass_entry.place(x=280, y=190)

            connect_button = CTkButton(cframe, width=390, height=40, font=('montserrat', 20, 'bold'), text='CONNECT', command=conn_handler)
            connect_button.place(x=90, y=250)   
            global res_box
            res_box = CTkTextbox(cframe, width=390, height=50, font=('montserrat', 20, 'bold'))
            res_box.configure(state=DISABLED)
            res_box.place(x=90, y=310) 

            exit_button = CTkButton(cframe, width=390, height=40, font=('montserrat', 20, 'bold'), text='CLOSE', command=lambda: croot.destroy(), fg_color='red', hover_color='#A80000')
            exit_button.place(x=90, y=380) 
        
            

            croot.mainloop()


        Thread(target=connect_func).start()
            





    def gui():
        root = CTk()
        root.title('WIFI TOOLS')
        root.geometry('1000x685')
        root.resizable(False, False)
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
        title = CTkLabel(master=frame, text='WIFI TOOLS', font=('montserrat', 30, 'bold'))
        # --------------------------------------------------------
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        title.place(x=380, y=30)
        # --------------------------------------------------------
        wstyle = ttk.Style()
        wstyle.configure("Treeview",
                        foreground="white",
                        rowheight=40,
                        fieldbackground="gray20", font=('montserrat', 18))
        wstyle.map('Treeview', background=[('selected', 'blue')])
        global tree
        tree = ttk.Treeview(frame, columns=('INDEX', 'SSID', 'BSSID', 'FREQUENCY'), show='headings', style="Treeview", height=25)

        tree.heading('INDEX', text='INDEX')
        tree.heading('SSID', text='SSID')
        tree.heading('BSSID', text='BSSID')
        tree.heading('FREQUENCY', text='FREQUENCY')

        tree.column('INDEX', anchor=CENTER, width=3)
        tree.column('SSID', anchor=CENTER, width=220)
        tree.column('BSSID', anchor=CENTER, width=110)
        tree.column('FREQUENCY', anchor=CENTER, width=10)

        tree.pack(padx=83, pady=(110, 180))

        scrollbar = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.pack(fill=BOTH, expand=True)

        # -------------------------------------------------------
        scan_button = CTkButton(master=frame, width=400, height=40, text='SCAN NEAR Wi-Fi', font=('montserrat', 18, 'bold'), command=scan_button_func)
        scan_button.place(x=65, y=520)

        connect_button = CTkButton(master=frame, width=400, height=40, text='CONNECT', font=('montserrat', 18, 'bold'), command=connect_button_func)
        connect_button.place(x=495, y=520)




        close_button = CTkButton(master=frame, width=830, height=40, text='CLOSE', font=('montserrat', 18, 'bold'), fg_color='red', hover_color='#A80000', command=lambda: root.destroy())
        close_button.place(x=65, y=580)

        root.mainloop()

    Thread(target=gui).start()
 
if __name__ == '__main__':
    wifi_tools_page()