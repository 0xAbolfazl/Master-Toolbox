from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel  # customtkinter
from network_ping_sweep_gui import ping_sweep                     # customtkinter, thraeding, tkinter, scapy, time, subproccess
from http_sniffer_network_gui import http_sniffer_network_func    # customtkinter, thraeding, time, scapy, datetime
from domain_to_ip_network_gui import dti_page                     # customtkinter, threading, socket
from ip_routing_network_gui import ip_routing_page                # customtkinter, threading, win32serviceutil, time
from port_scanner_network_gui import port_scanner_page            # customtkinter, threading, tkinter, socket
from my_interfaces_network_gui import my_interfaces_page          # customtkinter, threading, psutil
from my_mac_table_network_gui import my_mac_table_page            # customtkinter, threading, subprocess
from packet_sniffer_network_gui import packet_sniffer_page        # customtkinter, thraeding, tkinter, scapy, datetime, os, fpdf
from wifi_tools_network_gui import wifi_tools_page                # customtkinter, threading, tkinter, pywifi, time



def network_page():
    padx = 90
    pady = 120



    network_page = CTk()
    network_page.geometry('700x550')
    network_page.resizable(0, 0)
    network_page.title('NETWORK TOOLS')
    nframe = CTkFrame(master=network_page, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=nframe, text='NETWORK TOOLS', font=('montserrat', 30, 'bold'))


    
    nframe.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=175, y=30)


    ping_sweep_button = CTkButton(nframe, text='PING SWEEP', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=ping_sweep)
    http_sniffer_button = CTkButton(nframe, text='HTTP SNIFFER', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=http_sniffer_network_func)
    packet_sniffer_button = CTkButton(nframe, text='PACKET SNIFFER', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=packet_sniffer_page)
    dti_button = CTkButton(nframe, text='DOMAIN TO IP', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=dti_page)
    ip_routing_button = CTkButton(nframe, text='IP ROUTING', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=ip_routing_page)
    port_scanner_button = CTkButton(nframe, text='PORT SCANNER', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=port_scanner_page)
    my_mac_table_button = CTkButton(nframe, text='MY MAC TABLE', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=my_mac_table_page)
    my_interfaces_button = CTkButton(nframe, text='MY INTERFACES', width=230, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=my_interfaces_page)
    wifi_button = CTkButton(nframe, text='WIFI TOOLS', width=480, height=40, font=('montserrat', 15, 'bold'), corner_radius=30, command=wifi_tools_page)
    exit_button = CTkButton(nframe, text='EXIT', width=480, height=40, font=('montserrat', 15, 'bold'), text_color='white', fg_color='red', corner_radius=30, hover_color='#A82B2B', command=lambda: network_page.destroy())




    ping_sweep_button.place(            x=padx,       y=pady)
    http_sniffer_button.place(          x=padx+250,   y=pady)
    packet_sniffer_button.place(        x=padx,       y=pady+60)
    dti_button.place(                   x=padx+250,   y=pady+60)
    ip_routing_button.place(            x=padx,       y=pady+120)
    port_scanner_button.place(          x=padx+250,   y=pady+120)
    my_mac_table_button.place(          x=padx,       y=pady+180)
    my_interfaces_button.place(         x=padx+250,   y=pady+180)
    wifi_button.place(                  x=padx,       y=pady+240)
    exit_button.place(                  x=padx,   y=pady+300)






    network_page.mainloop()








if __name__ == '__main__':
    network_page()