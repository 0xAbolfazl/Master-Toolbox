from customtkinter import CTk, CTkButton, CTkLabel, CTkTextbox, CTkFrame, CTkEntry,DISABLED, NORMAL, END, set_default_color_theme, set_appearance_mode
from scapy.all import Ether, srp, ARP, sniff
from threading import Thread
from tkinter import messagebox

def arp_spoofing_detector_page():

    def cls():
        def clear():
            res_box.configure(state=NORMAL) 
            res_box.delete(1.0, END) 
            res_box.configure(state=DISABLED)
        Thread(target=clear).start()

    def detect_button():
        def adding(txt, end='\n'):
            res_box.configure(state=NORMAL)
            res_box.insert(END, txt+end)
            res_box.configure(state=DISABLED)
        def scann():
            try:
                adding("SCANNING STARTED !")
                def get_mac(ip):
                    pac = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
                    result = srp(pac, timeout=3, verbose=False)[0]
                    return result[0][1].hwsrc
                    
                def process(packet):
                    if packet.haslayer(ARP): # if there is an ARP packet
                        if packet[ARP].op == 2:
                            try:
                                real_mac = get_mac(packet[ARP].psrc)
                                response_mac = packet[ARP].hwsrc
                                if real_mac != response_mac:
                                    adding(f"[ ! ]    YOU ARE UNDER ATTACK")
                                    adding(f'      REAL MAC : {real_mac.upper()}')
                                    adding(f'      FAKE-MAC: {response_mac.upper()}')
                                    messagebox.showwarning('ATTACK DETECTED', f'YOU ARE UNDER ATTACK\n      REAL MAC : {real_mac.upper()}\n      FAKE-MAC: {response_mac.upper()}')

                            except Exception as er:
                                # adding('[!]   ERROR OCCURRED !')
                                # adding(er)
                                pass
                def arp_spoofing_detector_runner():
                    try:
                        iface = interface_entry.get()
                        if iface == 'd':
                            sniff(store=False, prn=process)
                        else:
                            sniff(store=False, prn=process, iface=iface)
                    except Exception as err:
                        # adding('[!]   ERROR OCCURREd !')
                        # adding(err)
                        pass
                arp_spoofing_detector_runner()

            except Exception as er:
                # adding('[!]   Error OCCURRED !')
                # adding(er)
                pass

        Thread(target=scann).start()

        # def scan_func():
        #     try:
        #         iinterface = interface_entry.get()
        #         def get_mac(ip):
        #             pac = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
        #             result = srp(pac, timeout=3, verbose=False)[0]
        #             return result[0][1].hwsrc
                    
        #         def process(packet):
        #             if packet.haslayer(ARP): # if there is an ARP packet
        #                 if packet[ARP].op == 2:
        #                     try:
        #                         real_mac = get_mac(packet[ARP].psrc)
        #                         response_mac = packet[ARP].hwsrc
        #                         if real_mac != response_mac:
        #                             adding('------------------------------------------------')
        #                             adding(f"[ ! ]    YOU ARE UNDER ATTACK")
        #                             adding(f'            REAL-MAC : {real_mac.upper()}')
        #                             adding(f'            FAKE-MAC : {response_mac.upper()}')
        #                             adding('------------------------------------------------')
        #                             messagebox.showwarning('ATTACK DETECTED', f'YOU ARE UNDER ATTACK \n...   REAL MAC : {real_mac.upper()}\n...   FAKE MAC : {response_mac.upper()}')
        #                     except Exception as er:
        #                         adding(er)
        #                         adding('[!]   ERROR OCCURRED !')
        #         def arp_spoofing_detector_runner():
        #             try:
        #                 iface = iinterface
        #                 adding("[~]    SCANNING STARTED ")
        #                 if iinterface == 'd':
        #                     sniff(store=False, prn=process)
        #                 else:
        #                     sniff(store=False, prn=process, iface=iface)
        #             except Exception as e:
        #                 adding(e)
        #                 adding('[!]   ERROR OCCURRED !')

        #         arp_spoofing_detector_runner()

        #     except Exception as er:
        #         adding(er)
        #         adding('[!]   Error OCCURRED !')


        # Thread(target=scan_func).start()


    root = CTk()
    root.title('ARP SPOOFING DETECTOR')
    root.geometry('800x615')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    # --------------------------------------------------------
    title = CTkLabel(frame, text='ARP SPOOFING DETECTOR', font=('montserrat', 30, 'bold'))
    sniff_button = CTkButton(frame, width=615, height=40, text='SNIFF THE NETWORK', font=('montserrat', 20, 'bold'), command=detect_button)
    interface_lbl = CTkLabel(frame, text='INTERFACE :', font=('montserrat', 28, 'bold'))
    interface_entry = CTkEntry(frame, font=('montserrat', 24, 'bold'), placeholder_text='interface', width=200)
    interface_entry.insert(END, 'Wi-Fi')
    res_box = CTkTextbox(frame, width=615, height=200, border_color='white', border_width=2, font=('montserrat', 17))
    res_box.configure(state=DISABLED)
    clear_log_button = CTkButton(frame, width=615, height=40, text='CLEAR LOG', font=('montserrat', 20, 'bold'), command=cls, fg_color='red', hover_color='#A80000')
    exit_button = CTkButton(frame, width=615, height=40, text='CLOSE', font=('montserrat', 20, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    # --------------------------------------------------------



    title.place(x=160, y=30)
    interface_lbl.place(x=70, y=120)
    interface_entry.place(x=485, y=120)
    sniff_button.place(x=70, y=180)
    res_box.place(x=70, y=235)
    clear_log_button.place(x=70, y=450)
    exit_button.place(x=70, y=505)


    root.mainloop()

if __name__ == '__main__':
    arp_spoofing_detector_page()