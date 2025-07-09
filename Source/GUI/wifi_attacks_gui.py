from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTabview  # customtkinter
from syn_flood_wifi_gui import syn_flood_page
from syn_flood_detector_wifi_gui import syn_flood_detector_page

def wifi_attack_page():
    padx = 90
    pady = 120



    wifi_attack_page = CTk()
    wifi_attack_page.geometry('700x350')
    wifi_attack_page.resizable(0, 0)
    wifi_attack_page.title('BASED ON WIFI ATTACK')
    wframe = CTkFrame(master=wifi_attack_page, corner_radius=10, border_width=2, border_color='red')
    tabv = CTkTabview(wframe, height=280)
    tabv.add('ATTACK')
    tabv.add('DEFENCE')
    tabv.set('ATTACK')
    # --------------------------------------------------------
    frame1 = tabv.tab('ATTACK')
    frame2 = tabv.tab('DEFENCE')
    # --------------------------------------------------------
    title = CTkLabel(master=frame1, text='BASED ON WIFI [ATTACK]', font=('montserrat', 30, 'bold'))
    title2 = CTkLabel(master=frame2, text='BASED ON WIFI [DEFENCE]', font=('montserrat', 30, 'bold'))
    syn_flood_button = CTkButton(frame1, text='SYN FLOOD', width=440, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=syn_flood_page)
    syn_flood_detector_button = CTkButton(frame2, text='DETECTOR [SYN-F]', width=440, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=syn_flood_detector_page)
    exit1_button = CTkButton(frame1, text='EXIT', width=440, height=40, font=('montserrat', 15, 'bold'), text_color='white', fg_color='red', corner_radius=30, hover_color='#A82B2B', command=lambda: wifi_attack_page.destroy())
    exit2_button = CTkButton(frame2, text='EXIT', width=440, height=40, font=('montserrat', 15, 'bold'), text_color='white', fg_color='red', corner_radius=30, hover_color='#A82B2B', command=lambda: wifi_attack_page.destroy())



    wframe.pack(padx=20, pady=20, fill='both', expand=True)
    tabv.pack(padx=22, pady=5,fill='both', expand=False)
    title.place(x=95, y=10)
    title2.place(x=85, y=10)
    syn_flood_button.place(x=80, y=120)
    syn_flood_detector_button.place(x=80, y=120)
    exit1_button.place(x=80, y=180)
    exit2_button.place(x=80, y=180)





    wifi_attack_page.mainloop()








if __name__ == '__main__':
    wifi_attack_page()