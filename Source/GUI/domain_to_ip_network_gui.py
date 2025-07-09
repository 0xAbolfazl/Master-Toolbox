from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, CTkEntry, END, NORMAL, DISABLED
from threading import Thread
from socket import gethostbyname

def dti_page():

    def button_d2i():
        def func():
            try:
                res_box.configure(state=NORMAL)
                res_box.delete(1.0, END)
                res_box.configure(state=DISABLED)
                addr = domain_entry.get()
                ip = gethostbyname(addr)
                res_box.configure(state=NORMAL)
                res_box.insert(END, ip)
                res_box.configure(state=DISABLED)

            except Exception:
                res_box.configure(state=NORMAL)
                res_box.delete(1.0, END)
                res_box.insert(END, 'ERROR')
                res_box.configure(state=DISABLED)
        Thread(target=func).start()

    root = CTk()
    root.title('DOMAIN TO IP')
    root.geometry('650x400')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='DOMAIN TO IP', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=185, y=30)


    domain_entry_lbl = CTkLabel(master=frame, text='DOMAIN : ', font=('montserrat', 25, 'bold'))
    domain_entry_lbl.place(x=85, y=120)

    domain_entry = CTkEntry(frame, width=280, height=37, font=('montserrat', 25))
    domain_entry.place(x=240 ,y=120)

    convert_button  = CTkButton(frame, text='CONVERT',width=435, height=40, font=('montserrat', 25), command=button_d2i)
    convert_button.place(x=85, y=175)

    res_box = CTkTextbox(frame, width=435, height=60, font=('montserrat', 25), border_color='white', border_width=2)
    res_box.configure(state=DISABLED)
    res_box.place(x=85, y=230)

    close_button  = CTkButton(frame, text='CLOSE',width=435, height=40, font=('montserrat', 25), command=lambda : root.destroy(), fg_color='red', hover_color='#A80000')
    close_button.place(x=85, y=300)





    root.mainloop()



if __name__ == '__main__':
    dti_page()