from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel  # customtkinter
from url_info_website_gui import url_info_page
from adming_panel_finder_website_gui import admin_panel_finder_page
from subdomain_finder_website_gui import subdomain_finder_page
from full_scan_website_gui import full_scanner_page

def website_page_page():



    website_page = CTk()
    website_page.geometry('710x370')
    website_page.resizable(0, 0)
    website_page.title('BASED ON WEBSITE')
    wsframe = CTkFrame(master=website_page, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=wsframe, text='BASED ON WEBSITE', font=('montserrat', 30, 'bold'))
    close_button = CTkButton(wsframe, text='CLOSE', width=530, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=lambda: website_page.destroy(), hover_color='#A82B2B', fg_color='red')
    url_info_button = CTkButton(wsframe, text='URL INFO', width=250, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=url_info_page)
    admin_panel_button = CTkButton(wsframe, text='ADMIN PANEL FINDER', width=250, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=admin_panel_finder_page)
    subdomain_button = CTkButton(wsframe, text='SUBDOMAIN FINDER', width=250, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=subdomain_finder_page)
    full_scan_button = CTkButton(wsframe, text='FULL SCAN', width=250, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=full_scanner_page)

    
    wsframe.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=165, y=30)
    close_button.place(x=70, y=250)

    url_info_button.place(x=70, y=130)    
    admin_panel_button.place(x=350, y=130) 
    subdomain_button.place(x=70, y=190) 
    full_scan_button.place(x=350, y=190) 

    website_page.mainloop()




if __name__  == '__main__':
    website_page_page()