from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, END, NORMAL, DISABLED
from threading import Thread
from subprocess import run




def my_mac_table_page():
        
    def button():
        res_box.configure(state=NORMAL)
        res_box.delete(1.0, END)
        res_box.configure(state=DISABLED)

        def adding(text):
            where = res_box
            where.configure(state=NORMAL)
            where.insert(END, f"{text}\n")
            where.configure(state=DISABLED)

        def run_command(command):
            result = run(command, shell=True, capture_output=True, text=True)
            return result.stdout

        def my_mac_table():
            try:
                res = run_command('arp -a')
                adding(res)
            except Exception:
                ('[!]    Error occurred while showing mac table !')

        Thread(target=my_mac_table).start()



    root = CTk()
    root.title('MY MAC TABLE')
    root.geometry('800x540')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='MY MAC TABLE', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=260, y=30)



    getting_button = CTkButton(frame, width=620, height=45, text='SHOW', font=('montserrat', 20, 'bold'), command=button)
    getting_button.place(x=70, y=110)

    res_box = CTkTextbox(frame, width=620, height=250, font=('ebrima', 20, 'bold'))
    res_box.configure(state=DISABLED)
    res_box.place(x=70, y=170)

    close_button = CTkButton(frame, width=620, height=45, text='CLOSE', font=('montserrat', 20, 'bold'), command=lambda: root.destroy(), fg_color='red', hover_color='#A80000')
    close_button.place(x=70, y=430)

    root.mainloop()




if __name__ == '__main__':
    my_mac_table_page()