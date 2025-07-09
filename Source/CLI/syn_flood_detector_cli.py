def syn_flood_detector_runner():
    try:
        from scapy.all import TCP, IP, Ether, sniff
        from collections import defaultdict
        from time import sleep
        from banner_cli import rtxt, ctxt, lbtxt, ytxt

        ytxt('[!]    THIS PROGRAM ONLY CHEACKS THE TRAFFIC BETWEEN YOU AND YOUR ROUTER\n       TO CHECK THE TRAFFUC OF THE ENITRE ROUTER NETWORK,YOU NEED TO \n       ACTIVE PORT MIRRORING ON YOUR ROUTER ')


        syn_packets = defaultdict(int)
        THRESHOLD = 20
        TIME_WINDOW = 3

        def detect_syn_flood(pkt):
            if pkt.haslayer(TCP) and pkt[TCP].flags == 'S':  
                src_ip = pkt[IP].src
                if pkt.haslayer(Ether):
                    src_mac = pkt[Ether].src  
                else:
                    src_mac = 'UNKNOWN'

                syn_packets[(src_ip, src_mac)] += 1

                if syn_packets[(src_ip, src_mac)] > THRESHOLD:
                    rtxt(f"[!]    POSSIBLE [SYN FLOOD] ATTACK DETECTED FROM ", end='')
                    ctxt(f'IP          : {src_ip}')
                    ctxt(f'{" "*49}MAC ADDRESS : {src_mac}')
                    syn_packets[(src_ip, src_mac)] = 0 

        def reset_counters():
            while True:
                sleep(TIME_WINDOW)
                syn_packets.clear()


        import threading
        threading.Thread(target=reset_counters, daemon=True).start()


        lbtxt("[+]    LISTENING FOR [SYN] PACKETS ...")
        sniff(prn=detect_syn_flood, store=0)
    except Exception:
        rtxt('[!]    ERROR OCCURRED IN [SYN-FLOOD-DETECTOR]')



if __name__ == '__main__':
    syn_flood_detector_runner()




# from scapy.all import TCP, IP, Ether, sniff
# from time import sleep
# from banner import rtxt, ctxt, lbtxt
# from threading import Thread

# def get_mac(ip): #  CONVERT IP 2 MAC ADDRESS
#     try:
#         from scapy.all import ARP, Ether, srp
#         packet = Ether(dst = 'ff:ff:ff:ff:ff:ff') / ARP(pdst = ip)
#         response = srp(x=packet, verbose=False)
#         return response[0][0][1].hwsrc
#     except Exception:
#         return 'None'
    

# syn_packets = []
# # global x
# x = 0
# THRESHOLD = 20



# def detect_syn_flood(pkt):
#     if TCP in pkt and pkt[TCP].flags == 'S':  
#         src_ip = pkt[IP].src
#         src_mac = pkt[Ether].src 

        
#         syn_packets.append(src_ip)
#         # print(f'{x} : {src_ip}')
#         # x = x + 1

#         if len(syn_packets) > THRESHOLD:
#             rtxt(f"[!]    POSSIBLE [SYN FLOOD] ATTACK DETECTED FROM IP          : ", end='')
#             ctxt(f'{src_ip}')
#             ctxt(f'{" "*49}MAC ADDRESS : {src_mac}')
#             syn_packets.clear()
        
#         elif src_mac != get_mac(src_ip):
#             print("something is wrong")

#         print(src_mac)
#         x = get_mac(src_ip)
#         print(x)
#         print(src_ip)

# def reset_counters():
#     while True:
#         sleep(5)
#         syn_packets.clear()



# Thread(target=reset_counters, daemon=True).start()


# lbtxt("[+]    LISTENING FOR [SYN] PACKETS ...")
# sniff(prn=detect_syn_flood, filter="tcp", store=0)























# from scapy.all import TCP, IP, Ether, sniff
# from collections import defaultdict
# import time
# from banner import rtxt, ctxt, lbtxt
# from threading import Thread


# syn_packets = []
# THRESHOLD = 30
# TIME_WINDOW = 3

# def detect_syn_flood(pkt):
#     if TCP in pkt and pkt[TCP].flags == 'S':  # is SYN PACKET
#         src_ip = pkt[IP].src
#         src_mac = pkt[Ether].src  # extract MAC address
#         syn_packets.append(src_ip)

#         if len(syn_packets) > 40:
#             print('ATACKKKKKKKKKKKKKKKKKKKKKKKKK')
#         # if syn_packets[(src_ip, src_mac)] > THRESHOLD:
#         #     rtxt(f"[!]    POSSIBLE [SYN FLOOD] ATTACK DETECTED FROM IP          : ", end='')
#         #     ctxt(f'{src_ip}')
#         #     ctxt(f'{" "*49}MAC ADDRESS : {src_mac}')
#         #     print(syn_packets)
#         #     syn_packets[(src_ip, src_mac)] = 0

# def reset_counters():
#     while True:
#         time.sleep(TIME_WINDOW)
#         syn_packets = []


# lbtxt("[+]    LISTENING FOR [SYN] PACKETS ...")


# sniff(prn=detect_syn_flood, filter="tcp", store=0)
# Thread(target=reset_counters, daemon=True).start()
