from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkTextbox, CTkFrame, DISABLED, NORMAL, END, set_default_color_theme, set_appearance_mode, CTkOptionMenu, CTkTabview
import socket
from threading import Thread
from tkinter import messagebox


def port_scanner_page():

    def button():

        def adding(txt):
            res_box.configure(state=NORMAL)
            res_box.insert(END, text=f'{txt}\n')
            res_box.configure(state=DISABLED)

        res_box.configure(state=NORMAL)
        res_box.delete(1.0, END)
        res_box.configure(state=DISABLED)  


        def scan_ports():
            try:
                ip = ip_entry.get()
                ipx = socket.gethostbyname(ip)
                

                if ip == '':
                    messagebox.showerror('ADRESS ERROR', message='ADDRESS CANT BE EMPTY !')
                    raise Exception
                
                try:
                    start_point = int(start_entry.get())
                    end_point = int(end_entry.get())
                except Exception:
                    messagebox.showerror('TYPE ERROR', 'START / END PORT SHOULD BE INT')
                    raise Exception

                try:
                    timeout = float(timeout_entry.get())  / 1000          
                except Exception:
                    messagebox.showerror('TYPE ERROR', 'TIMEOUT SHOULD BE INT OR FLOAT')
                    raise Exception

                ports = []
                adding(f'    ADDRESS    :  {ip}\n    IP                   :  {ipx}\n    PORTS          :  RANGE({start_point} - {end_point})\n    TIMEOUT     :  {timeout}')
                adding('    SCANNING STARTED !') 
                adding('---------------------------------------------------------------------------')

                for port in range(start_point, end_point+1):
                    socket.setdefaulttimeout(timeout)
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    res = tcp.connect_ex((ipx, port))
                    
                    if res == False:
                        ports.append(port)
                        adding(f'    PORT [   {port}   ] IS OPEN')

                    tcp.close()
                if len(ports) == 0:
                    adding('     NOTHIN FOUND !')

                adding("---------------------------------------------------------------------------\n     SCANNING FINISHED !\n---------------------------------------------------------------------------")

            except Exception as er:
                adding(er)

        try:
            Thread(target=scan_ports).start() 
        except Exception as er:
            adding('    ERROR OCCURRED !') 
            adding(er)          



    root = CTk()
    root.title('PORT SCANNER')
    root.geometry('700x650')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    pframe = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    pframe.pack(padx=20, pady=20, fill='both', expand=True)
    # --------------------------------------------------------
    tabv = CTkTabview(pframe, height=580)
    tabv.add('DEFAULT PORT')
    tabv.add('SPECIFIC PORT')
    tabv.add('CUSTOM PORT')
    tabv.set('SPECIFIC PORT')
    tabv.pack(padx=22, pady=5,fill='both', expand=False)
    # --------------------------------------------------------
    frame = tabv.tab('CUSTOM PORT')
    title = CTkLabel(frame, text='PORT SCANNER', font=('montserrat', 30, 'bold'))
    title.place(x=170, y=10)



    ip_entry_lbl = CTkLabel(master=frame, text='ADDRESS : ', font=('montserrat', 25, 'bold'))
    ip_entry_lbl.place(x=45, y=100)

    ip_entry = CTkEntry(frame, width=180, height=37, font=('montserrat', 25), placeholder_text='address')
    ip_entry.place(x=375 ,y=100)

    domain_entry_lbl = CTkLabel(master=frame, text='START / END PORT :', font=('montserrat', 25, 'bold'))
    domain_entry_lbl.place(x=45, y=150)
    
    start_entry = CTkEntry(frame, width=85, height=37, font=('montserrat', 25), placeholder_text='start')
    start_entry.insert(1, '1')
    start_entry.place(x=375 ,y=150)

    end_entry = CTkEntry(frame, width=85, height=37, font=('montserrat', 25), placeholder_text='end')
    end_entry.insert(1, '65535')
    end_entry.place(x=470 ,y=150)

    timeout_entry_lbl = CTkLabel(master=frame, text='TIMEOUT (ms) :', font=('montserrat', 25, 'bold'))
    timeout_entry_lbl.place(x=45, y=200)
    
    timeout_entry = CTkEntry(frame, width=180, height=37, font=('montserrat', 25), placeholder_text='timeout')
    timeout_entry.insert(1, '500')
    timeout_entry.place(x=375 ,y=200)


    scan_button  = CTkButton(frame, text='SCAN',width=511, height=40, font=('montserrat', 25), command=button)
    scan_button.place(x=45, y=250)

    res_box = CTkTextbox(frame, width=511, height=150, font=('montserrat', 18), border_color='white', border_width=2)
    res_box.configure(state=DISABLED)
    res_box.place(x=45, y=310)

    close_button  = CTkButton(frame, text='CLOSE',width=511, height=40, font=('montserrat', 25, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    close_button.place(x=45, y=475)






# 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    def sp_button():

        def adding(txt):
            sp_res_box.configure(state=NORMAL)
            sp_res_box.insert(END, text=f'{txt}\n')
            sp_res_box.configure(state=DISABLED)

        sp_res_box.configure(state=NORMAL)
        sp_res_box.delete(1.0, END)
        sp_res_box.configure(state=DISABLED)  


        def sp_scan_ports():
            try:
                sp_ip = sp_ip_entry.get()
                sp_ipx = socket.gethostbyname(sp_ip)
                

                if sp_ip == '':
                    messagebox.showerror('ADRESS ERROR', message='ADDRESS CANT BE EMPTY !')
                    raise Exception
                
                try:
                    get_port = int(sp_port_entry.get())     
                except Exception:
                    messagebox.showerror('TYPE ERROR', 'PORT SHOULD BE INT')
                    raise Exception

                try:
                    timeout = float(sp_timeout_entry.get())  / 1000          
                except Exception:
                    messagebox.showerror('TYPE ERROR', 'TIMEOUT SHOULD BE INT OR FLOAT')
                    raise Exception

                ports = []
                adding(f'    ADDRESS    :  {sp_ip}\n    IP                   :  {sp_ipx}\n    PORT            :  {get_port}\n    TIMEOUT     :  {timeout}')
                adding('    SCANNING STARTED !') 
                adding('---------------------------------------------------------------------------')

                socket.setdefaulttimeout(timeout)
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = tcp.connect_ex((sp_ipx, get_port))

                if res == False:
                    ports.append(get_port)
                    adding(f'    PORT [   {get_port}   ] IS OPEN')
                tcp.close()
                if len(ports) == 0:
                    adding('     NOTHIN FOUND !')
                adding("---------------------------------------------------------------------------\n     SCANNING FINISHED !\n---------------------------------------------------------------------------")

            except Exception as er:
                adding(er)

        try:
            Thread(target=sp_scan_ports).start() 
        except Exception as er:
            adding('    ERROR OCCURRED !') 
            adding(er)




    spframe = tabv.tab('SPECIFIC PORT')
    sp_title = CTkLabel(spframe, text='PORT SCANNER', font=('montserrat', 30, 'bold'))
    sp_title.place(x=170, y=10)


    sp_ip_entry_lbl = CTkLabel(master=spframe, text='ADDRESS : ', font=('montserrat', 25, 'bold'))
    sp_ip_entry_lbl.place(x=45, y=100)

    sp_ip_entry = CTkEntry(spframe, width=180, height=37, font=('montserrat', 25), placeholder_text='address')
    sp_ip_entry.place(x=375 ,y=100)

    sp_port_entry_lbl = CTkLabel(master=spframe, text='PORT :', font=('montserrat', 25, 'bold'))
    sp_port_entry_lbl.place(x=45, y=150)
    
    sp_port_entry = CTkEntry(spframe, width=180, height=37, font=('montserrat', 25), placeholder_text='start')
    sp_port_entry.insert(1, '1')
    sp_port_entry.place(x=375 ,y=150)

    sp_timeout_entry_lbl = CTkLabel(master=spframe, text='TIMEOUT (ms) :', font=('montserrat', 25, 'bold'))
    sp_timeout_entry_lbl.place(x=45, y=200)
    
    sp_timeout_entry = CTkEntry(spframe, width=180, height=37, font=('montserrat', 25), placeholder_text='timeout')
    sp_timeout_entry.insert(1, '500')
    sp_timeout_entry.place(x=375 ,y=200)


    sp_scan_button  = CTkButton(spframe, text='SCAN',width=511, height=40, font=('montserrat', 25), command=sp_button)
    sp_scan_button.place(x=45, y=250)

    sp_res_box = CTkTextbox(spframe, width=511, height=150, font=('montserrat', 18), border_color='white', border_width=2)
    sp_res_box.configure(state=DISABLED)
    sp_res_box.place(x=45, y=310)

    sp_close_button  = CTkButton(spframe, text='CLOSE',width=511, height=40, font=('montserrat', 25, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    sp_close_button.place(x=45, y=475)




# 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    def dp_button():

        def adding(txt):
            dp_res_box.configure(state=NORMAL)
            dp_res_box.insert(END, text=f'{txt}\n')
            dp_res_box.configure(state=DISABLED)

        dp_res_box.configure(state=NORMAL)
        dp_res_box.delete(1.0, END)
        dp_res_box.configure(state=DISABLED)  


        def dp_scan_ports():
            try:
                dp_ip = dp_ip_entry.get()
                dp_ipx = socket.gethostbyname(dp_ip)
                

                if dp_ip == '':
                    messagebox.showerror('ADRESS ERROR', message='ADDRESS CANT BE EMPTY !')
                    raise Exception
                
                default_ports = [21, 22, 23, 25, 53, 80, 110, 115, 111, 135, 137, 138, 139,
                        143, 194, 443, 445, 548, 587, 993, 995, 1701, 1723, 2083,
                        1433, 3306, 3389, 5632, 5432, 8008, 8080, 8443,5900, 25565,
                        515, 631, 3282, 5190, 5050, 4443, 1863, 6891, 1503, 5631, 5632, 6667]

                try:
                    timeout = float(sp_timeout_entry.get()) / 1000   
                except Exception:
                    messagebox.showerror('TYPE ERROR', 'TIMEOUT SHOULD BE INT OR FLOAT')
                    raise Exception

                ports = []
                adding(f'    ADDRESS    :  {dp_ip}\n    IP                   :  {dp_ipx}\n    PORT            :  DEFAULT PORTS\n    TIMEOUT     :  {timeout}')
                adding('    SCANNING STARTED !') 
                adding('---------------------------------------------------------------------------')
                for port in default_ports:
                    socket.setdefaulttimeout(timeout)
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    res = tcp.connect_ex((dp_ipx, port))

                    if res == False:
                        ports.append(port)
                        adding(f'    PORT [   {port}   ] IS OPEN')

                    tcp.close()
                if len(ports) == 0:
                    adding('     NOTHIN FOUND !')
                adding("---------------------------------------------------------------------------\n     SCANNING FINISHED !\n---------------------------------------------------------------------------")

            except Exception as er:
                adding(er)

        try:
            Thread(target=dp_scan_ports).start() 
        except Exception as er:
            adding('    ERROR OCCURRED !') 
            adding(er)




    dpframe = tabv.tab('DEFAULT PORT')
    dp_title = CTkLabel(dpframe, text='PORT SCANNER', font=('montserrat', 30, 'bold'))
    dp_title.place(x=170, y=10)


    dp_ip_entry_lbl = CTkLabel(master=dpframe, text='ADDRESS : ', font=('montserrat', 25, 'bold'))
    dp_ip_entry_lbl.place(x=45, y=100)

    dp_ip_entry = CTkEntry(dpframe, width=180, height=37, font=('montserrat', 25), placeholder_text='address')
    dp_ip_entry.place(x=375 ,y=100)




    dp_timeout_entry_lbl = CTkLabel(master=dpframe, text='TIMEOUT (ms) :', font=('montserrat', 25, 'bold'))
    dp_timeout_entry_lbl.place(x=45, y=150)
    
    dp_timeout_entry = CTkEntry(dpframe, width=180, height=37, font=('montserrat', 25), placeholder_text='timeout')
    dp_timeout_entry.insert(1, '500')
    dp_timeout_entry.place(x=375 ,y=150)


    dp_scan_button  = CTkButton(dpframe, text='SCAN',width=511, height=40, font=('montserrat', 25), command=dp_button)
    dp_scan_button.place(x=45, y=200)

    dp_res_box = CTkTextbox(dpframe, width=511, height=200, font=('montserrat', 18), border_color='white', border_width=2)
    dp_res_box.configure(state=DISABLED)
    dp_res_box.place(x=45, y=260)

    dp_close_button  = CTkButton(dpframe, text='CLOSE',width=511, height=40, font=('montserrat', 25, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    dp_close_button.place(x=45, y=475)

    root.mainloop()


if __name__ == '__main__':
    port_scanner_page()