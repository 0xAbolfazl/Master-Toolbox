from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel, CTkTextbox, set_appearance_mode, set_default_color_theme, CTkEntry, END, NORMAL, DISABLED, ctk_tk
import scapy.all as scapy
from scapy.layers.http import HTTPRequest, HTTPResponse
from scapy.layers.dns import DNS
from tkinter import ttk, CENTER, Scrollbar, BOTH, RIGHT, Y, VERTICAL, messagebox, Text, filedialog
from threading import Thread
import datetime
from fpdf import FPDF
from os import path




packet_index = 0

def packet_sniffer_page():

    protocol_dict = {1: 'ICMP', 6: 'TCP', 17: 'UDP', 2 : 'IGMP', 89 : 'RIP', 41 : 'DTLS', 1900 : 'SSDP', 53 : 'DNS'}
    packets = []

    icmp_types = {
    0: 'Echo Reply',
    3: 'Destination Unreachable',
    4: 'Source Quench',
    5: 'Redirect',
    8: 'Echo Request',
    11: 'Time Exceeded',
    12: 'Parameter Problem',
        }



    def start():
        global is_sniffing
        is_sniffing = True
        Thread(target=sniff_packets, daemon=True).start()

    def stop():
        global is_sniffing
        is_sniffing = False

    def sniff_packets():
        def sniffer():
            scapy.sniff(prn=process_packet, store=False, stop_filter=lambda x: not is_sniffing)
        Thread(target=sniffer).start()


    def process_packet(packet):
        global packet_index
        if packet.haslayer(scapy.IP) or packet.haslayer(scapy.ARP):
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            src_ip = packet[scapy.IP].src if packet.haslayer(scapy.IP) else 'N/A'
            dst_ip = packet[scapy.IP].dst if packet.haslayer(scapy.IP) else 'N/A'
            dst_port = packet[scapy.TCP].dport if packet.haslayer(scapy.TCP) else (packet[scapy.UDP].dport if packet.haslayer(scapy.UDP) else 'N/A')
            proto = packet[scapy.IP].proto if packet.haslayer(scapy.IP) else 'ARP'
            proto_name = protocol_dict.get(proto, str(proto))
            http_method = ''
            
            if packet.haslayer(HTTPRequest):
                http_method = packet[HTTPRequest].Method.decode()
            elif packet.haslayer(HTTPResponse):
                http_method = 'HTTP Response'
            elif packet.haslayer(DNS):
                http_method = 'DNS Query' if packet[DNS].qr == 0 else 'DNS Response'
            elif packet.haslayer(scapy.ARP):
                http_method = 'ARP'
                src_ip = packet[scapy.ARP].psrc
                dst_ip = packet[scapy.ARP].pdst
            else:
                if proto == 1 and packet.haslayer(scapy.ICMP):
                    icmp_type = packet[scapy.ICMP].type
                    http_method = icmp_types.get(icmp_type, 'Unknown ICMP Type')
                elif proto == 6 and packet.haslayer(scapy.TCP):
                    flags = packet[scapy.TCP].flags
                    if flags == 0x02:
                        http_method = 'SYN'
                    elif flags == 0x12:
                        http_method = 'SYN-ACK'
                    elif flags == 0x10:
                        http_method = 'ACK'
                    elif flags == 0x18:
                        http_method = 'PSH-ACK'
                    elif flags == 0x11:
                        http_method = 'FIN-ACK'
                    elif flags == 0x14:
                        http_method = 'RST-ACK'
                    else:
                        http_method = 'TCP'
                elif proto == 17:
                    http_method = 'UDP'
                    if packet.haslayer(scapy.Raw):
                        raw_load = packet[scapy.Raw].load
                        if b'DTLS' in raw_load:
                            http_method = 'DTLS'
                        elif b'SSDP' in raw_load:
                            http_method = 'SSDP'
                elif proto == 2:
                    http_method = 'IGMP'
                elif proto == 89:
                    http_method = 'RIP'
                elif packet.haslayer(scapy.FTP):
                    http_method = 'FTP'
                elif packet.haslayer(scapy.SMTP):
                    http_method = 'SMTP'
                elif packet.haslayer(scapy.EIGRP):
                    http_method = 'EIGRP'
                elif packet.haslayer(scapy.SNMP):
                    http_method = 'SNMP'
                elif packet.haslayer(scapy.NTP):
                    http_method = 'NTP'
                elif packet.haslayer(scapy.DHCP):
                    http_method = 'DHCP'
                elif packet.haslayer(scapy.LLDP):
                    http_method = 'LLDP'
            
            tree.insert('', 'end', values=(packet_index, timestamp, src_ip, dst_ip, f'{proto_name}/{http_method}', dst_port))
            packets.append(packet)
            packet_index += 1

    def export_to_pdf():
        def export_pdf():
            fd = filedialog.askdirectory()
            if fd != '':
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                headers = ['INDEX', 'TIME', 'SOURCE', 'DESTINATION', 'PROTOCOL', 'D-PORT']
                col_widths = [pdf.w / 12, pdf.w / 4.5, pdf.w / 6, pdf.w / 6, pdf.w / 6, pdf.w / 10]
                row_height = pdf.font_size * 1.5

                for i, header in enumerate(headers):
                    pdf.cell(col_widths[i], row_height, header, border=1, ln=0, align='C')
                pdf.ln(row_height)

                for row_id in tree.get_children():
                    row = tree.item(row_id)['values']
                    for i, item in enumerate(row):
                        pdf.cell(col_widths[i], row_height, str(item), border=1, ln=0, align='C')
                    pdf.ln(row_height)
                xnum = 0
                while True:
                    if not path.exists(rf"{fd}\result-{xnum}.pdf"):
                        pdf.output(rf"{fd}\result-{xnum}.pdf")
                        messagebox.showinfo('PDF OUTPUT',"PDF GENERATED SUCCESSFULLY ! ")
                        break
                    else:
                        xnum+=1

        Thread(target=export_pdf).start()
    def show_packet_details():
        def run():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("WARNING", "PLAESE SELECT A PACKET TO VIEW DETAILS !")
                return

            item = tree.item(selected_item)
            details = item['values']
            packet_index = tree.index(selected_item)
            packet = packets[packet_index]
            
            detail_text = f"TIME : {details[0]}\nSOURCE : {details[1]}\nDESTINATION : {details[2]}\nPROTOCOL : {details[3]}/{details[4]}\nRAW PACKET DATA :\n{packet.show(dump=True)}"
            
            troot = CTk()
            troot.title('PACKET SNIFFER')
            troot.geometry('800x500')
            troot.resizable(False, False)
            set_appearance_mode("dark")
            set_default_color_theme("blue")
            tframe = CTkFrame(master=troot, corner_radius=10, border_width=2, border_color='red')
            ttitle = CTkLabel(master=tframe, text='PACKET INFO', font=('montserrat', 30, 'bold'))
            # --------------------------------------------------------
            tframe.pack(padx=20, pady=20, fill='both', expand=True)
            ttitle.place(x=350, y=30)

            txt_box = CTkTextbox(tframe)
            txt_box.insert(END, detail_text)
            txt_box.configure(state=DISABLED)
            txt_box.pack(fill='both', expand=True)


            troot.mainloop()
        Thread(target=run).start()

    def gui():
        root = CTk()
        root.title('PACKET SNIFFER')
        root.geometry('1000x685')
        root.resizable(False, False)
        set_appearance_mode("dark")
        set_default_color_theme("blue")
        frame = CTkFrame(master=root, corner_radius=10, border_width=2, border_color='red')
        title = CTkLabel(master=frame, text='PACKET SNIFFER', font=('montserrat', 30, 'bold'))
        # --------------------------------------------------------
        frame.pack(padx=20, pady=20, fill='both', expand=True)
        title.place(x=350, y=30)
        # --------------------------------------------------------
        style = ttk.Style()
        style.configure("Treeview",
                        foreground="white",
                        rowheight=25)
        style.map('Treeview', background=[('selected', 'blue')])
        global tree
        tree = ttk.Treeview(frame, columns=('INDEX', 'TIME', 'SOURCE', 'DESTINATION', 'PROTOCOL', 'PORT'), show='headings', style="Treeview", height=25)

        tree.heading('INDEX', text='INDEX')
        tree.heading('TIME', text='TIME')
        tree.heading('SOURCE', text='SOURCE')
        tree.heading('DESTINATION', text='DESTINATION')
        tree.heading('PROTOCOL', text='PROTOCOL')
        # tree.heading('METHOD', text='METHOD')
        tree.heading('PORT', text='PORT')

        tree.column('INDEX', anchor=CENTER, width=60)
        tree.column('TIME', anchor=CENTER, width=110)
        tree.column('SOURCE', anchor=CENTER, width=100)
        tree.column('DESTINATION', anchor=CENTER, width=100)
        tree.column('PROTOCOL', anchor=CENTER, width=80)
        # tree.column('METHOD', anchor=CENTER, width=100)
        tree.column('PORT', anchor=CENTER, width=150)

        tree.pack(padx=83, pady=(110, 180))

        scrollbar = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.pack(fill=BOTH, expand=True)

        # -------------------------------------------------------
        start_button = CTkButton(master=frame, width=200, height=40, text='START', font=('montserrat', 18, 'bold'), command=start)
        start_button.place(x=65, y=520)

        stop_button = CTkButton(master=frame, width=200, height=40, text='STOP', font=('montserrat', 18, 'bold'), command=stop)
        stop_button.place(x=275, y=520)

        export_button = CTkButton(master=frame, width=200, height=40, text='EXPORT', font=('montserrat', 18, 'bold'), command=export_to_pdf)
        export_button.place(x=485, y=520)

        info_button = CTkButton(master=frame, width=200, height=40, text='INFO', font=('montserrat', 18, 'bold'), command=show_packet_details)
        info_button.place(x=695, y=520)

        close_button = CTkButton(master=frame, width=830, height=40, text='CLOSE', font=('montserrat', 18, 'bold'), fg_color='red', hover_color='#A80000', command=lambda: root.destroy())
        close_button.place(x=65, y=580)

        root.mainloop()

    Thread(target=gui).start()
 
if __name__ == '__main__':
    packet_sniffer_page()