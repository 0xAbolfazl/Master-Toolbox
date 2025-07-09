try:
    from scapy.all import Ether, srp, ARP, sniff
    from banner_cli import rtxt, lbtxt, ctxt
except Exception as ew:
    print(ew)
    rtxt('[!]   ERROR OCCURRED WHILE IMPORTING MODULES')
try:
    def get_mac(ip):
        pac = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
        result = srp(pac, timeout=3, verbose=False)[0]
        return result[0][1].hwsrc
        
    def process(packet):
        if packet.haslayer(ARP): # if there is an ARP packet
            if packet[ARP].op == 2:
                try:
                    real_mac = get_mac(packet[ARP].psrc)
                    response_mac = packet[ARP].hwsrc
                    if real_mac != response_mac:
                        rtxt('[!]', end='')
                        lbtxt(f"    YOU ARE UNDER ATTACK, REAL-MAC : ", end='')
                        rtxt(f'{real_mac.upper()}')
                        lbtxt(f'{" "*29}FAKE-MAC: ', end='')
                        rtxt(f'{response_mac.upper()}', end='\n')
                except Exception as er:
                    print(er)
                    rtxt('[!]   ERROR OCCURRED !')
    def arp_spoofing_detector_runner():
        try:
            ctxt('[~]    ENTER YOUR INTERFACE : (default is Wi-Fi just -> press enter)', end='')
            iface = input('')
            if iface != '':
                pass
            if iface == '' :
                iface = 'Wi-Fi'
            ctxt("[~]    SCANNING STARTED ")
            if iface == 'd':
                sniff(store=False, prn=process)
            else:
                sniff(store=False, prn=process, iface=iface)
        except Exception:
            rtxt('[!]   ERROR OCCURRED !')

except Exception as er:
    print(er)
    rtxt('[!]   Error OCCURRED !')


if __name__ == '__main__':
    try:
        arp_spoofing_detector_runner()
    except Exception:
        rtxt('[!]   Error')