from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel  # customtkinter
from directory_wordpress_gui import directory_wordpress_page


def wordpress_page():

    wordpress_page = CTk()
    wordpress_page.geometry('700x300')
    wordpress_page.resizable(0, 0)
    wordpress_page.title('BASED ON WORDPRESS')
    wpframe = CTkFrame(master=wordpress_page, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=wpframe, text='BASED ON WORDPRESS', font=('montserrat', 30, 'bold'))
    word_press_button = CTkButton(wpframe, text='VULNEBRATE DIRECTORY SCANNER', width=440, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=directory_wordpress_page)
    close_button = CTkButton(wpframe, text='CLOSE', width=440, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=lambda: wordpress_page.destroy(), hover_color='#A82B2B', fg_color='red')

    
    wpframe.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=130, y=30)
    close_button.place(x=105, y=190)
    word_press_button.place(x=105, y=130)    


    wordpress_page.mainloop()




if __name__  == '__main__':
    wordpress_page()