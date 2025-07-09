from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, CTkEntry, NORMAL, END, DISABLED  # customtkinter
from threading import Thread
from requests import get
from fpdf import FPDF
from tkinter import filedialog, messagebox
from os import path

saved_txt1 = []
saved_txt2 = []
saved_txt3 = []

def directory_wordpress_page():

    def pdf_out():
        def out():
            fd = filedialog.askdirectory()
            if fd != '':
                # print('z')
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial', size=12)
                
                for i in saved_txt1:
                    pdf.cell(50, 6 ,txt=i, ln=True)
                    pdf.cell(50, 6 ,txt=saved_txt2[saved_txt1.index(i)], ln=True)
                    pdf.cell(50, 6 ,txt=saved_txt3[saved_txt1.index(i)], ln=True)
                    pdf.cell(50, 6 ,txt='-------------------------------------------------------------------------------------------------', ln=True)

                xnum = 0
                while True:
                    if not path.exists(rf"{fd}\wp-result-{xnum}.pdf"):
                        pdf.output(rf"{fd}\wp-result-{xnum}.pdf")
                        messagebox.showinfo('PDF EXPORT',"PDF GENERATED SUCCESSFULLY ! ")
                        break
                    else:
                        xnum+=1
        
        Thread(target=out).start()
        # for i in saved_txt:
        #     print(i)

    def clear():
        def cl():
            res_box.configure(state=NORMAL)
            res_box.delete(1.0, END)
            res_box.configure(state=DISABLED)
        Thread(target=cl).start()

    def scan_button():
        def adding(txt, sep='-------------------------------------------------------------------------------'):
            res_box.configure(state=NORMAL)
            res_box.insert(END, str(txt)+'\n'+sep+'\n')
            res_box.configure(state=DISABLED)
        def scan():
            if addr_entry.get() == '':
                messagebox.showerror('URL ERROR','ENTER VALID ADDRESS !')
                raise TypeError
            adding("SCANNING STARTED ")
            addr = addr_entry.get()
            try:
                bugs = {
                    "readme.html" : "Show WordPress version",
                    "xmlrpc.php" : "You can DDos to It file",
                    "wp-cron.php" : "You can DDos to It file",
                    "info.php" : "Show all site Info (System server, sql info, ...)",
                    "license.txt" : "Show site info",
                    "robots.txt" : "Show ROBOT Api info",
                    "?auther=1" : "Username Login site",
                    "wp-json/wp/v2/users" : "You can go to it, search 'auther' and show username login site",
                    "wp-links-opm.php" : "",
                    "wp-traceback.php" : "",
                    "wp-mail.php" : "Go to mail site",
                    "wp-settings.php" : "Show Error in site",
                    "auther-sitemap.xml" : "Show all user site",
                    "wp-config-sample.php" : "You can try download it file and show username and password DB",
                    "phpmyadmin/index.php" : "you can try crack it page and show info DB",
                    "PhpMyAdmin/index.php" : "you can try crack it page and show info DB",
                    "phpMyAdmin/index.php" : "you can try crack it page and show info DB",
                    "wp-admin" : "Login page site",
                    "wp-content/uploads/" : "show uploaded file in the server"            
                }
                for bug in bugs:
                    url = f"{addr}/{bug}"
                    status = get(url=url)

                    if status.status_code == 200:
                        adding(f"\n[ + ]  >> URL                       : {url}\n           -- STATUS CODE  : {status}\n           -- INFO EXPLOIT  : {bugs[bug]}\n")
                        saved_txt1.append(f'[+]  URL                    :    {url}')
                        saved_txt2.append(f'...   STATUS CODE  :    {status}')
                        saved_txt3.append(f'...   INFO EXPlOIT    :    {bugs[bug]}')
                        # saved_txt.append(f"\n[ + ]  >> URL --> {url}\n           -- STATUS CODE : {status}\n           -- INFO EXPLOIT : {bugs[bug]}\n-------------------------------------------------------")

                    elif status.status_code != 200:
                        pass
                adding('SCANNING FINISHED !')
            except Exception as er:
                adding(er)

        Thread(target=scan).start()



    d_wordpress_page = CTk()
    d_wordpress_page.geometry('800x700')
    d_wordpress_page.resizable(0, 0)
    d_wordpress_page.title('BASED ON WORDPRESS')
    d_wpframe = CTkFrame(master=d_wordpress_page, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=d_wpframe, text='VULNEBRATE DIRECTORY', font=('montserrat', 30, 'bold'))
    scan_btn = CTkButton(d_wpframe, text='SCAN', width=600, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=scan_button)
    clear_btn = CTkButton(d_wpframe, text='CLEAR LOG', width=285, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=clear)
    pdf_btn = CTkButton(d_wpframe, text='PDF OUTPUT', width=285, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=pdf_out)

    close_button = CTkButton(d_wpframe, text='CLOSE', width=600, height=45, font=('montserrat', 18, 'bold'), corner_radius=30, command=lambda: d_wordpress_page.destroy(), hover_color='#A82B2B', fg_color='red')
    res_box = CTkTextbox(d_wpframe, width=600, height=250, font=('montserrat', 19))
    addr_lbl = CTkLabel(d_wpframe, text="ADDRESS : ", font=('montserrat', 27, 'bold'))
    addr_entry = CTkEntry(d_wpframe, width=250, height=40, font=('montserrat', 20, 'bold'), placeholder_text='https://site.ir')


    d_wpframe.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=160, y=30)
    addr_lbl.place(x=80, y=120)
    addr_entry.place(x=430, y=120)
    close_button.place(x=80, y=570)
    scan_btn.place(x=80, y=510) 
    clear_btn.place(x=80, y=450)  
    pdf_btn.place(x=395, y=450)   
    res_box.place(x=80, y=180)

    d_wordpress_page.mainloop()




if __name__  == '__main__':
    directory_wordpress_page()