from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTabview  # customtkinter
from arp_spoofing_mitm_gui import arp_spoofing_mitm_page
from arp_spoofing_detector_mitm_gui import arp_spoofing_detector_page



def mitm_page():


    padx = 90
    pady = 120

    mitm_page = CTk()
    mitm_page.geometry('700x350')
    mitm_page.resizable(0, 0)
    mitm_page.title('MAN IN THE MIDDLE')
    mframe = CTkFrame(master=mitm_page, corner_radius=10, border_width=2, border_color='red')
    tabv = CTkTabview(mframe, height=280)
    tabv.add('ATTACK')
    tabv.add('DEFENCE')
    tabv.set('ATTACK')
    # --------------------------------------------------------
    frame1 = tabv.tab('ATTACK')
    frame2 = tabv.tab('DEFENCE')
    # --------------------------------------------------------
    title = CTkLabel(master=frame1, text='MITM [ATTACK]', font=('montserrat', 30, 'bold'))
    title2 = CTkLabel(master=frame2, text='MITM [DEFENCE]', font=('montserrat', 30, 'bold'))
    arp_spoofing_button = CTkButton(frame1, text='ARP SPOOFING', width=440, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=arp_spoofing_mitm_page)
    arp_spoofing_detector_button = CTkButton(frame2, text='DETECTOR [ARP-S]', width=440, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=arp_spoofing_detector_page)
    exit1_button = CTkButton(frame1, text='EXIT', width=440, height=40, font=('montserrat', 15, 'bold'), text_color='white', fg_color='red', corner_radius=30, hover_color='#A82B2B', command=lambda: mitm_page.destroy())
    exit2_button = CTkButton(frame2, text='EXIT', width=440, height=40, font=('montserrat', 15, 'bold'), text_color='white', fg_color='red', corner_radius=30, hover_color='#A82B2B', command=lambda: mitm_page.destroy())



    mframe.pack(padx=20, pady=20, fill='both', expand=True)
    tabv.pack(padx=22, pady=5,fill='both', expand=False)
    title.place(x=170, y=10)
    title2.place(x=160, y=10)
    arp_spoofing_button.place(x=80, y=120)
    arp_spoofing_detector_button.place(x=80, y=120)
    exit1_button.place(x=80, y=180)
    exit2_button.place(x=80, y=180)





    mitm_page.mainloop()








if __name__ == '__main__':
    mitm_page()