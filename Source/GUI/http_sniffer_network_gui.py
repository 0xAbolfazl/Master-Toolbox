from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, CTkEntry, END, NORMAL, DISABLED
from threading import Thread
from scapy.all import sniff, IP, Raw
from scapy.layers.http import HTTPRequest
from time import sleep
from datetime import datetime


def http_sniffer_network_func():
    def button():
        def http_sinffer_button():
            try:
                user_interface = interface_entry.get()
                res_box.configure(state=NORMAL)
                res_box.delete(1.0, END)
                res_box.insert(END, '[+]     SNIFFING STARTED !\n')
                res_box.configure(state=DISABLED)
                def sniff_packets(iface=None):
                    if iface:
                        sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
                    else:
                        sniff(filter="port 80", prn=process_packet, store=False)

                def process_packet(packet):

                    if packet.haslayer(HTTPRequest):      # if this packet is an HTTP Request
                        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()    # get the requester's IP Address
                        ip = packet[IP].src
                        des = packet[IP].dst
                        ua = packet[HTTPRequest].User_Agent.decode()  
                        if len(ua) > 60:
                            ua = f'{ua[0:65]}\n{" "*41}{ua[65:]}'
                        # if len(ua) > 40:
                        #     ua = ua[0:41]

                        method = packet[HTTPRequest].Method.decode()
                        res_box.configure(state=NORMAL)
                        res_box.insert(END, (f"\n------------------------------------------------------------------------------------------------------------------------------\n[+] METHOD              :   {method}\n      USER-AGENT      :   {ua}\n      TIME                      :   {str(datetime.now())[0:19]}\n      SOURCE               :   {ip} \n      DESTINATION     :   {des}\n      REQUESTED        :   {url}"))
                        res_box.configure(state=DISABLED)
                        if packet.haslayer(Raw) and method == "POST":
                            # if show_raw flag is enabled, has raw data, and the requested method is "POST"
                            # then show raw
                            res_box.configure(state=NORMAL)
                            res_box.insert(END, (f"\n------------------------------------------------------------------------------------------------------------------------------\n[+] METHOD              :   {method}\n      USER-AGENT      :   {ua}\n      TIME                      :   {str(datetime.now())[0:19]}\n      SOURCE               :   {ip} \n      DESTINATION     :   {des}\n      REQUESTED        :   {url}\n    [0+0] Some useful Raw data: {packet[Raw].load}"))
                            sleep(2)
                            res_box.configure(state=DISABLED)
                sniff_packets(iface=user_interface)
            except Exception as er:
                if 'Error opening adapter' in str(er):
                    res_box.configure(state=NORMAL)
                    res_box.insert(END, '[ ! ]     ERROR WHILE OPENING ADAPTER !')
                    res_box.configure(state=DISABLED)
                else:
                    res_box.configure(state=NORMAL)
                    res_box.insert(END, er)
                    res_box.configure(state=DISABLED)
        Thread(target=http_sinffer_button).start()



    root = CTk()
    root.title('HTTP SNIFFER')
    root.geometry('1000x640')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='HTTP SNIFFER', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=350, y=30)


    interface_lbl = CTkLabel(master=frame, text='YOUR INITERFACE : ', font=('montserrat', 25, 'bold'))
    interface_lbl.place(x=65, y=120)

    interface_entry = CTkEntry(frame, width=293, height=37, font=('montserrat', 25))
    interface_entry.insert(END, 'Wi-Fi')
    interface_entry.place(x=600 ,y=120)

    start_button  = CTkButton(frame, text='START',width=830, height=40, font=('montserrat', 25), command=button)
    start_button.place(x=65, y=175)

    res_box = CTkTextbox(frame, width=830, height=300, font=('montserrat', 18))
    res_box.configure(state=DISABLED)
    res_box.place(x=65, y=230)

    close_button  = CTkButton(frame, text='CLOSE',width=830, height=40, font=('montserrat', 25), command=lambda : root.destroy(), fg_color='red', hover_color='#A80000')
    close_button.place(x=65, y=540)





    root.mainloop()










if __name__ == '__main__':
    http_sniffer_network_func()