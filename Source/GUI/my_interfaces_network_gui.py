from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, END, NORMAL, DISABLED
from psutil import net_if_addrs
from threading import Thread




def my_interfaces_page():
        
    def button():
        res_box.configure(state=NORMAL)
        res_box.delete(1.0, END)
        res_box.configure(state=DISABLED)
        def adding(text):
            where = res_box
            where.configure(state=NORMAL)
            where.insert(END, f"{text}\n")
            # where.insert(END, '------------------------------------------------------------------\n')
            where.configure(state=DISABLED)

        def my_interfaces():
            try:
                my_interface = net_if_addrs()
                if len(my_interface) != 0:
                    adding("## TOTAL INTERFACE : {}".format(len(my_interface)))
                    adding('------------------------------------------------')
                    x = 0
                    for i in my_interface:
                        x+=1
                        adding('#{} '.format(x)+i)
                    # adding('-------------------------------')
                else:
                    adding("NOTHING FOUNDED")
            except Exception:
                adding('[ ! ]    ERROR OCURRED WHILE GETTING INTERFACES !')
        Thread(target=my_interfaces()).start()


    root = CTk()
    root.title('MY INTERFACES')
    root.geometry('600x540')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='MY INTERFACES', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=150, y=30)



    getting_button = CTkButton(frame, width=420, height=45, text='SHOW', font=('montserrat', 20, 'bold'), command=button)
    getting_button.place(x=70, y=110)

    res_box = CTkTextbox(frame, width=420, height=250, font=('montserrat', 20, 'bold'))
    res_box.configure(state=DISABLED)
    res_box.place(x=70, y=170)

    close_button = CTkButton(frame, width=420, height=45, text='CLOSE', font=('montserrat', 20, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    close_button.place(x=70, y=430)

    root.mainloop()




if __name__ == '__main__':
    my_interfaces_page()