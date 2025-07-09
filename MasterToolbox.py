from Source.CLI.cli import cli_v
from Source.GUI.main_gui import gui_v
from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, set_appearance_mode, set_default_color_theme
from threading import Thread
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR / "Source/GUI"))
sys.path.append(str(BASE_DIR / "Source/CLI"))

import ctypes
def hide_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)

def show_console():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 1)

hide_console()

def packet_sniffer_page():

    def cli():
        root.destroy()
        show_console()
        Thread(target=cli_v).start()

    def gui():
        root.destroy()
        hide_console()
        Thread(target=gui_v).start()




    root = CTk()
    root.title('MASTER TOOL BOX')
    root.geometry('600x330')
    root.resizable(False, False)
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
    title = CTkLabel(master=frame, text='MASTER TOOL BOX', font=('montserrat', 30, 'bold'))
    # --------------------------------------------------------
    frame.pack(padx=20, pady=20, fill='both', expand=True)
    title.place(x=130, y=30)
    # --------------------------------------------------------

    # -------------------------------------------------------
    start_button = CTkButton(master=frame, width=400, height=40, text='CLI VERSION', font=('montserrat', 18, 'bold'), command=cli)
    start_button.place(x=80, y=160)

    stop_button = CTkButton(master=frame, width=400, height=40, text='GUI VERSION', font=('montserrat', 18, 'bold'), command=gui)
    stop_button.place(x=80, y=100)

    close_button = CTkButton(master=frame, width=400, height=40, text='CLOSE', font=('montserrat', 18, 'bold'), fg_color='red', hover_color='#A80000', command=lambda: root.destroy())
    close_button.place(x=80, y=220)

    root.mainloop()


 
if __name__ == '__main__':
    # starter_check()
    packet_sniffer_page()





















# def starter_check():
#     try:
#         print("CHECKING MODULES ...")
#         time.sleep(1)
#         from requests import get
#         # from banner_cli import rtxt, gtxt, ytxt, lmtxt, ctxt, lbtxt, lctxt, back_color
#         from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkEntry, CTkTextbox, DISABLED, NORMAL, END  # customtkinter
#         from keyboard import is_pressed
#         from scapy.all import Ether, ARP, srp, sendp, conf, sniff
#         from tkinter import messagebox, filedialog, messagebox,ttk, CENTER, BOTH, RIGHT, Y, VERTICAL, messagebox
#         from time import sleep
#         from colorama import init
#         from termcolor import colored
#         from os import system
#         ######## cli version #########################################
#         from banner_cli import ctxt, lmtxt, rtxt, lbtxt, mtxt, gtxt, back_color
#         from syn_flood_cli import syn_flood_function
#         from ping_sweep_cli import ping_sweep_runner
#         from arp_spoofing_cli import arp_sp
#         from arp_spoofing_detector_cli import arp_spoofing_detector_runner 
#         from http_sniffer_cli import http_sniffer_runner
#         from packet_sniffer_cli import packet_sniffer
#         from domain_to_ip_cli import dti                                       # socket
#         from ip_routing_cli import ip_router_runner                            # win32serviceutil
#         from port_scanner_cli import port_scanner_runner                       # tqdm - socket
#         from my_mac_table_cli import my_mac_table as mc                        # subprocess
#         from my_interfaces_cli import my_interfaces                            # psutil
#         from wifi_tools_cli import wifi_runner                                 # pywifi - tqdm
#         from directory_cli import diretory_search
#         from admin_panel_cli import admin_panel_finder
#         from full_scanner_cli import fullscan
#         from subdomain_finder_cli import ssubdomain_func
#         from ip_details_cli import ip_information_runner
#         from syn_flood_detector_cli import syn_flood_detector_runner
#         #########################################################
#         from fpdf import FPDF
#         from socket import gethostbyname, socket, setdefaulttimeout, AF_INET, SOCK_STREAM
#         import socket
#         from getpass import getuser
#         ###### full scanner cli ################################
#         from banner_cli import gtxt, rtxt, ctxt
#         from port_scanner_cli import auto_scan_port
#         from admin_panel_cli import auto_admin_panel_finder
#         from directory_cli import auto_diretory_search
#         from ip_details_cli import ip_information
#         from subdomain_finder_cli import full_scanner_subdomain_finder
#         ########################################################
#         from scapy.layers.http import HTTPRequest 
#         from datetime import datetime
#         # website ###############################################
#         from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel  # customtkinter
#         from url_info_website_gui import url_info_page
#         from adming_panel_finder_website_gui import admin_panel_finder_page
#         from subdomain_finder_website_gui import subdomain_finder_page
#         from full_scan_website_gui import full_scanner_page
#         # wifi atacks gui ######################################
#         from syn_flood_wifi_gui import syn_flood_page
#         from syn_flood_detector_wifi_gui import syn_flood_detector_page
#         # wifi tools cli #######################################
#         from tqdm import tqdm
#         import pywifi
#         from pywifi import const
#         # wordpress gui ########################################
#         from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel  # customtkinter
#         from directory_wordpress_gui import directory_wordpress_page
#         print('ALL THE MODULES (52) FOUNDED SUCCESSFULY !')
#         time.sleep(3)


#     except Exception as e:
#         print(e)
#         print('ERR')





# print("PRIMARY BANNER")
# print("[+]    1- CLI VERSION\n...    2- GUI VERSION")
# while True:
#     user_input = input('Your choice : ')
#     if user_input == '1':
#         print("STARTING COMMAND LINE INTERFACE VERSION ...")
#         sleep(2)
#         cli_v()
#         break
#     elif user_input == '2':
#         print("STARTING GRAPHICAL VERSION ...")
#         sleep(2)
#         gui_v()
#         break
#     else :
#         print(' ---- YOUR CHOICE MUST BE BETWEEN 1 OR 2 ! ----')
