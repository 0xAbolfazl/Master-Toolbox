from customtkinter import CTk, CTkButton, CTkLabel, CTkTextbox, CTkFrame, DISABLED, NORMAL, END, set_default_color_theme, set_appearance_mode
from scapy.all import TCP, IP, Ether, sniff
from collections import defaultdict
from time import sleep
from threading import Thread
from tkinter import messagebox

def syn_flood_detector_page():

    def cls():
        def clear():
            res_box.configure(state=NORMAL) 
            res_box.delete(1.0, END) 
            res_box.configure(state=DISABLED)
        Thread(target=clear).start()

    def detect_button():
        def adding(txt, end='\n', sep='\n------------------------------------------------------------------------------------------'):
            res_box.configure(state=NORMAL)
            res_box.insert(END, txt+sep+end)
            res_box.configure(state=DISABLED)

        def detector():
            try:
                res_box.configure(state=DISABLED)

                adding('[ ! ]    THIS PROGRAM ONLY CHECKS THE TRAFFIC BETWEEN YOU \n          AND YOUR ROUTER, TO CHECK THE TRAFFIC OF THE ENITRE \n          ROUTER NETWORK, YOU NEED TO ACTIVE PORT MIRRORING \n          ON YOUR ROUTER ')
                adding("[+]    LISTENING FOR [ SYN ] PACKETS ...")

                syn_packets = defaultdict(int)
                THRESHOLD = 20
                TIME_WINDOW = 3

                def detect_syn_flood(pkt):
                    if pkt.haslayer(TCP) and pkt[TCP].flags == 'S':  
                        src_ip = pkt[IP].src
                        if pkt.haslayer(Ether):
                            src_mac = pkt[Ether].src  
                        else:
                            src_mac = 'UNKNOWN'

                        syn_packets[(src_ip, src_mac)] += 1

                        if syn_packets[(src_ip, src_mac)] > THRESHOLD :
                            adding(f"[ ! ]    POSSIBLE [ SYN FLOOD ] ATTACK DETECTED FROM ", sep='')
                            adding(f' --->>   IP                        :  {src_ip}', sep='')
                            adding(f' --->>   MAC ADDRESS :  {src_mac}')
                            messagebox.showwarning('ATTACK DETECTED', f'[ ! ]    POSSIBLE [ SYN FLOOD ] ATTACK DETECTED FROM \n --->>   IP                        :   {src_ip}\n --->>   MAC ADDRESS    :   {src_mac}')
                            syn_packets[(src_ip, src_mac)] = 0 

                def reset_counters():
                    while True:
                        sleep(TIME_WINDOW)
                        syn_packets.clear()

                Thread(target=reset_counters, daemon=True).start()


                sniff(prn=detect_syn_flood, store=0)
            except Exception:
                adding('[!]    ERROR OCCURRED IN [SYN-FLOOD-DETECTOR]')
        Thread(target=detector).start()





    root = CTk()
    root.title('SYN FLOOD DETETOR')
    root.geometry('800x555')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    # --------------------------------------------------------
    # --------------------------------------------------------
    title = CTkLabel(frame, text='SYN FLOOD DETECTOR', font=('montserrat', 30, 'bold'))
    title.place(x=200, y=20)

    sniff_button = CTkButton(frame, width=615, height=40, text='SNIFF THE NETWORK', font=('montserrat', 20, 'bold'), command=detect_button)
    sniff_button.place(x=70, y=120)

    res_box = CTkTextbox(frame, width=615, height=200, border_color='white', border_width=2, font=('montserrat', 17, 'bold'))
    res_box.place(x=70, y=175)

    clear_log_button = CTkButton(frame, width=615, height=40, text='CLEAR LOG', font=('montserrat', 20, 'bold'), command=cls, fg_color='red', hover_color='#A80000')
    clear_log_button.place(x=70, y=390)

    exit_button = CTkButton(frame, width=615, height=40, text='CLOSE', font=('montserrat', 20, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    exit_button.place(x=70, y=445)

    root.mainloop()




if __name__ == '__main__':
    syn_flood_detector_page()