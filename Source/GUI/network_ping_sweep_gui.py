from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkTextbox, CTkFrame, DISABLED, NORMAL, END, set_default_color_theme, set_appearance_mode, CTkOptionMenu
from scapy.all import Ether, srp, ARP
from threading import Thread
from time import sleep
from subprocess import run, PIPE
from tkinter import messagebox

def ping_sweep():

    def button_func():
        def primaty_print():
            try:
                gettimeout = float(delay_ip.get())
                domain = entry_ip.get()
                last = (ip_last_entry.get())
                last2 = (ip_last2_entry.get())
                target_ip = f'{domain}.{last}'
                result_box.configure(state=NORMAL)  # Enable editing to insert the message
                result_box.delete(1.0, END)  # Clear the text area
                
                result_box.insert(END, f"[+]      FIRST IP    :  {target_ip}\n")
                result_box.configure(state=DISABLED)
                sleep(0.3)
                result_box.configure(state=NORMAL)
                result_box.insert(END, f"  ...      LAST IP      :  {f'{domain}.{last2}'}\n")
                result_box.configure(state=DISABLED)
                sleep(0.3)
                result_box.configure(state=NORMAL)
                result_box.insert(END, f"  ...      TIMEOUT   :  {gettimeout} (ms)\n")
                result_box.configure(state=DISABLED)
                sleep(0.3)

                if option.get() == 'USING ARP':
                    result_box.configure(state=NORMAL)
                    result_box.insert(END, "  ...      METHOD   :  USING ARP\n")
                    result_box.insert(END, "------------------------------------------\n")
                    result_box.configure(state=DISABLED)
                elif option.get() == 'USING CMD':
                    result_box.configure(state=NORMAL)
                    result_box.insert(END, "  ...      METHOD   :  USING SUBPROCCES (CMD)\n")
                    result_box.insert(END, "------------------------------------------\n")
                    result_box.configure(state=DISABLED)
                sleep(0.3)
                result_box.configure(state=NORMAL)
                result_box.insert(END, "[~]      SCANNING STARTED ...\n")
                result_box.configure(state=DISABLED)

            except Exception as er:
                print(er)

        def ping_sweep_fisrt():
            try:
                sleep(2.5)
                gettimeout = float(delay_ip.get())
                domain = entry_ip.get()
                last = int(ip_last_entry.get())
                last2 = int(ip_last2_entry.get())
                target_ip = f'{domain}.{last}'
                # result_box.configure(state=NORMAL)  # Enable editing to insert the message
                # result_box.delete(1.0, END)  # Clear the text area
                clients = []#
                print('x')
                for i in (range(1)):
                    for j in range(last, last2+1):
                        # print('were here')
                        target_ip = f'{domain}.{j}'
                        arp = ARP(pdst=target_ip)              # create ARP packet
                        ether = Ether(dst="ff:ff:ff:ff:ff:ff") # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
                        packet = ether/arp                     # stack them
                        result = srp(packet, timeout=gettimeout/1000, verbose=0)[0]
                        for sent, received in result:          # for each response, append ip and mac address to `clients` list
                            clients.append(f'              {received.psrc}{(13-len(received.psrc))*" "*2}{9*" "}{received.hwsrc}\n')
                printed = []
                for i in clients:
                    if i not in printed:
                        printed.append(i)
                    else:
                        pass
                result_box.configure(state=NORMAL) 
                result_box.insert(END, "[!]    --- SCANNING FINISHED ")
                result_box.configure(state=DISABLED) 
                sleep(1)
                # printed = ['      192.168.1.105        ff:ff:ff:ff:ff:ff',]
                if len(printed) == 0:
                    # result_box.delete(1.0, END)
                    result_box.configure(state=NORMAL) 
                    result_box.insert(END, "\n[~]    NOTHING FOUND ")
                    result_box.configure(state=DISABLED)
                else:
                    result_box.configure(state=NORMAL) 
                    result_box.delete(1.0, END)
                    text = f'''[+]         AVAILABLE DEVICE[S] IN YOUR NETWORK :

              IP                           MAC
              -----------------------------------------------
'''
                    result_box.insert(END, text)
                    result_box.configure(state=DISABLED) 
                    for i in printed:
                        result_box.configure(state=NORMAL)
                        # result_box.delete(1.0, END)  
                        result_box.insert(END, i)
                        result_box.configure(state=DISABLED) 


            except Exception as d:
                result_box.delete(1.0, END) 
                result_box.insert(END, '[!]    ERORR OCCURRED !\n\n')
                result_box.insert(END, d)

        def ping_sweep_second():
            sleep(2.5)
            gettimeout = str(delay_ip.get())
            domain = entry_ip.get()
            last = int(ip_last_entry.get())
            last2 = int(ip_last2_entry.get())
            result_box.configure(state=NORMAL)  # Enable editing to insert the message
            active_ips = []
            for ip in range(last, last2 + 1):
                result_box.configure(state=NORMAL)
                # num = 105/(last2+1 - last)
                # result_box.insert(END, '|||')
                result_box.configure(state=DISABLED)
                address = f"{domain}.{ip}"
                result = run(["ping", "-n", "1", "-w", gettimeout, address], stdout=PIPE, stderr=PIPE)
                if result.returncode == 0:
                    active_ips.append(address)
            result_box.delete(1.0, END)  # Clear the text area

            result_box.configure(state=NORMAL)
            result_box.insert(END, '\n')
            result_box.configure(state=DISABLED)

            result_box.configure(state=NORMAL) 
            result_box.insert(END, "[~]    --- SCANNING FINISHED ")
            result_box.configure(state=DISABLED) 
            sleep(1)

            if len(active_ips) == 0:
                result_box.delete(1.0, END)
                result_box.configure(state=NORMAL) 
                result_box.insert(END, "\n[~]    NOTHING FOUND ")
                result_box.configure(state=DISABLED)
            else:
                result_box.configure(state=NORMAL) 
                result_box.delete(1.0, END)
                text = f'''[+]         AVAILABLE DEVICE[S] IN YOUR NETWORK :

              IP                           
              ------------------------------------
'''
                result_box.insert(END, text)
                for i in active_ips:
                    result_box.configure(state=NORMAL)
                        # result_box.delete(1.0, END)  
                    result_box.insert(END, f'              {i}\n')
                    result_box.configure(state=DISABLED) 

      
        Thread(target=primaty_print).start()
        if option.get() == 'USING ARP':
            Thread(target=ping_sweep_fisrt).start()
        elif option.get() == 'USING CMD':
            Thread(target=ping_sweep_second).start()


    network_ping_sweep_page = CTk()
    network_ping_sweep_page.title('PING SWEEP')
    network_ping_sweep_page.geometry('700x630')
    network_ping_sweep_page.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")

    npframe = CTkFrame(master=network_ping_sweep_page, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=npframe, text='PING SWEEP', font=('montserrat', 30, 'bold'))
    # ----------------------------------------------------------------------
    npframe.pack(padx=20, pady=20, fill='both', expand=True)
    # ----------------------------------------------------------------------

    ip_label = CTkLabel(master=npframe, text='FIRST 3 SECTION OF YOUR IP : ', font=('montserrat', 23))
    entry_ip = CTkEntry(master=npframe, width=150, height=35, font=('montserrat', 20), border_color='white', border_width=2)
    entry_ip.insert(END, '192.168.1')
    ip_last_label = CTkLabel(master=npframe, text='START / END POINT : ', font=('montserrat', 23))  
    ip_last_entry = CTkEntry(master=npframe, width=72, height=35, font=('montserrat', 20), border_color='white', border_width=2)
    ip_last2_entry = CTkEntry(master=npframe, width=72, height=35, font=('montserrat', 20), border_color='white', border_width=2)
    ip_last_entry.insert(END, '1')
    ip_last2_entry.insert(END, '254')
    delay_label = CTkLabel(master=npframe, text='TIMEOUT (ms) : ', font=('montserrat', 23))
    delay_ip = CTkEntry(master=npframe, width=150, height=35, font=('montserrat', 20), border_color='white', border_width=2)
    delay_ip.insert(END, '500')
    option_label = CTkLabel(master=npframe, text='METHOD : ', font=('montserrat', 23))
    option = CTkOptionMenu(master=npframe, values=['USING ARP', 'USING CMD'],width=150, height=35, font=('montserrat', 15))
    get_button = CTkButton(master=npframe, text='SCAN', width=520, height=30, font=('montserrat', 23, 'bold'), command=button_func)
    close_button = CTkButton(master=npframe, text='EXIT', width=520, height=30, font=('montserrat', 23, 'bold'), command=lambda: network_ping_sweep_page.destroy(), fg_color='red', text_color='white', hover_color='#751717')
    result_box = CTkTextbox(master=npframe, width=520, height=170, font=('montserrat', 15), border_color='white', border_width=2)
    result_box.configure(state=DISABLED)


    title.place(x=220, y=20)

    ip_label.place(x=70, y=120)
    entry_ip.place(x=440, y=120)

    ip_last_label.place(x=70, y=160)
    ip_last_entry.place(x=440, y=160)
    ip_last2_entry.place(x=517, y=160)

    delay_label.place(x=70, y=200)
    delay_ip.place(x=440, y=200)

    option_label.place(x=70, y=240)
    option.place(x=440, y=240)    

    get_button.place(x=70, y=280)

    result_box.place(x=70, y=330)  

    close_button.place(x=70, y=520)

    network_ping_sweep_page.mainloop()
    # ------------------------------------------------------------------------


if __name__ == '__main__':
    ping_sweep()