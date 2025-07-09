from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, CTkEntry, END, NORMAL, DISABLED
from threading import Thread
import win32serviceutil
from time import sleep

def ip_routing_page():

    def adding(text):
        where = res_box
        where.configure(state=NORMAL)
        where.insert(END, text)
        where.insert(END, '------------------------------------------------------------------\n')
        where.configure(state=DISABLED)

        
    def ip_routing(func):
        class WService:
            def __init__(self, service, machine=None, verbose=False):
                self.service = service
                self.machine = machine
                self.verbose = verbose

                    
            @property
            def running(self):
                return win32serviceutil.QueryServiceStatus(self.service)[1] == 4
        

            def start(self):
                adding(f"[+]    STARTING ...\n")
                sleep(1)

                if not self.running:
                    win32serviceutil.StartService(self.service)
                    sleep(1)
                    if self.running:
                        if self.verbose:
                            adding(f"[+]    {self.service} STARTED  SUCCESSFULLY !\n")
                        return True
                    else:
                        if self.verbose:
                            adding(f"[!]   CAN NOT START \n")
                        return False
                elif self.verbose:
                    adding(f"[ ! ]   {self.service} IS ALREADY  RUNNING\n")
                    
                
            def stop(self):
                adding(f"[+]    STOPING ...\n")
                sleep(1)
                if self.running:
                    win32serviceutil.StopService(self.service)
                    sleep(0.5)
                    if not self.running:
                        if self.verbose:
                            adding(f"[+]    {self.service} STOPED  SUCCESSFULLY !\n")
                            return True
                    else:
                        if self.verbose:
                            adding(f"[ ! ]    CANNOT STOP\n")
                        return False
                elif self.verbose:
                    adding(f"[ ! ]    {self.service} IS NOT RUNNING !\n")

            def restart(self):
                adding(f"[+]     RESTARTING  {self.service}...\n")
                sleep(1)
                if self.running:
                    win32serviceutil.RestartService(self.service)
                    sleep(2)
                    if self.running:
                        if self.verbose:
                            adding(f"[+]    {self.service} RESTARTED  SUCCESSFULLY !\n")
                        return True
                    else:
                        if self.verbose:
                            adding(f"[ ! ]    CANNOT START\n")
                        return False
                elif self.verbose:
                    adding(f"[ ! ]    {self.service} IS  NOT RUNNING !\n")

        def main(action, service):
            service = WService(service, verbose=True)
            if action == "start":
                service.start()
            elif action == "stop":
                service.stop()
            elif action == "restart":
                service.restart()
        try:
            main(func, 'RemoteAccess')
        except Exception as er:
            if 'Access is denied' in str(er):
                adding("    ERROR : ACCESS DENIED !\n    ADMIN ACCESS IS REQUIRED !\n")

    def service_start():
        def run():
            # res_box.configure(state=NORMAL)
            # res_box.delete(1.0, END)
            # res_box.configure(state=DISABLED)
            func = 'start'
            ip_routing(func=func)
        Thread(target=run).start()


    def service_stop():
        def run():
            # res_box.configure(state=NORMAL)
            # res_box.delete(1.0, END)
            # res_box.configure(state=DISABLED)
            func = 'stop'
            ip_routing(func=func)
        Thread(target=run).start()

    def service_restart():
        def run():
            # res_box.configure(state=NORMAL)
            # res_box.delete(1.0, END)
            # res_box.configure(state=DISABLED)
            func = 'restart'
            ip_routing(func=func)
        Thread(target=run).start()
    
    def clear():
        res_box.configure(state=NORMAL)
        res_box.delete(1.0, END)
        res_box.configure(state=DISABLED)      



    root = CTk()
    root.title('IP ROUTING')
    root.geometry('775x520')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='IP ROUTING', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=265, y=30)




    enable_button  = CTkButton(frame, text='START',width=200, height=50, font=('montserrat', 25), border_color='white', border_width=2, command=service_start)
    enable_button.place(x=30, y=136)

    disable_button  = CTkButton(frame, text='STOP',width=200, height=52, font=('montserrat', 25), border_color='white', border_width=2, command=service_stop)
    disable_button.place(x=30, y=201)

    restart_button  = CTkButton(frame, text='RESTART',width=200, height=52, font=('montserrat', 25), border_color='white', border_width=2, command=service_restart)
    restart_button.place(x=30, y=268) 

    clear_button  = CTkButton(frame, text='CLEAR LOG',width=670, height=52, font=('montserrat', 25, 'bold'), border_color='white', border_width=2, fg_color='red', command=clear, hover_color='#A80000')
    clear_button.place(x=30, y=337) 

    close_button  = CTkButton(frame, text='CLOSE',width=670, height=50, font=('montserrat', 25, 'bold'), border_color='white', border_width=2, fg_color='red', command=lambda: root.destroy(), hover_color='#A80000')
    close_button.place(x=30, y=400) 

    res_box = CTkTextbox(frame, width=450, height=185, font=('montserrat', 18), border_color='white', border_width=2)
    res_box.configure(state=DISABLED)
    res_box.place(x=250, y=135)


    
    root.mainloop()





if __name__ == '__main__':
    ip_routing_page()