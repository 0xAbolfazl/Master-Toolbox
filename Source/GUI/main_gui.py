def gui_v():    
    from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, set_appearance_mode, set_default_color_theme
    from wifi_attacks_gui import wifi_attack_page
    from network_gui import network_page
    from wordpress_gui import wordpress_page
    from website_gui import website_page_page
    from mitm_gui import mitm_page

    set_appearance_mode("dark")
    set_default_color_theme("blue")


    root = CTk()
    root.title('MASTER TOOL BOX')
    root.geometry('715x400')
    root.resizable(False, False)
    # root.overrideredirect(True)


    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='MASTER TOOL BOX', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=170, y=30)
    # --------------------------------------------------------
    wifi_button = CTkButton(frame, text='WIFI ATTACK', width=250, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=wifi_attack_page)
    network_button = CTkButton(frame, text='NETWORK TOOLS', width=250, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=network_page)
    wp_button = CTkButton(frame, text='WORDPRESS SCANNER', width=250, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=wordpress_page)
    web_button = CTkButton(frame, text='WEBSITE TOOLS', width=250, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=website_page_page)
    mitm_button = CTkButton(frame, text='MAN IN THE MIDDLE ATTACKS', width=510, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=mitm_page)
    exit_button = CTkButton(frame, text='EXIT', width=510, height=40, font=('montserrat', 15, 'bold'), text_color='white', fg_color='red', corner_radius=30, hover_color='#A82B2B', command=lambda: root.destroy())


    padx = 90
    pady = 105

    wifi_button.place(   x=padx-10,     y=pady)
    network_button.place(x=padx+250, y=pady)
    wp_button.place(     x=padx-10,     y=pady+60)
    web_button.place(    x=padx+250, y=pady+60)
    mitm_button.place(   x=padx-10,     y=pady+120)
    exit_button.place(   x=padx-10,     y=pady+180)




    root.mainloop()


if __name__ == '__main__':
    gui_v()



text = '''
#####  |+|-------------------------------------|+|  #####
#####  |||-/                                 \-|||  #####
#####  |||   [  /\/\ @ $ T E R - T00L B0X  ]   |||  #####
#####  |||   [     CODED By RASHIDIAN      ]   |||  #####
#####  |||   [    PROGRAMMER FORM IRAN     ]   |||  #####
#####  |||   [       VERSIONS 1.2.0        ]   |||  #####
#####  |||-\                                 /-|||  #####
#####  |+|-------------------------------------|+|  #####
'''