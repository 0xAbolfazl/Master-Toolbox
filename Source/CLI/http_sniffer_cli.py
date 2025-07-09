try:
    from scapy.all import sniff, IP, Raw
    from scapy.layers.http import HTTPRequest # import HTTP packet
    from banner_cli import rtxt, gtxt, ctxt
    from time import sleep
except Exception as e:
    print(e)
    rtxt('[!]   Error ocuerred whule importing modules!')

def sniff_packets(iface=None):
    if iface:
        sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
    else:
        sniff(filter="port 80", prn=process_packet, store=False)

def process_packet(packet):

    if packet.haslayer(HTTPRequest):      # if this packet is an HTTP Request
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()    # get the requester's IP Address
        ip = packet[IP].src
        ua = packet[HTTPRequest].User_Agent.decode()  # get the request method
        method = packet[HTTPRequest].Method.decode()
        ctxt(f"\n------------------------------------------------------------\n[+] Method     :   {method}\n    User-Agent :   {ua[0:42]}\n    Sender     :   {ip} \n    Requested  :   {url}")
        if packet.haslayer(Raw) and method == "POST":
            # if show_raw flag is enabled, has raw data, and the requested method is "POST"
            # then show raw
            rtxt(f"\n------------------------------------------------------------\n[+] Method     :   {method}\n    User-Agent :   {ua[0:42]}\n    Sender     :   {ip} \n    Requested  :   {url}\n    [0+0] Some useful Raw data: {packet[Raw].load}")
            sleep(2)


def listen2httpx(inter):
    try:
        # ctxt('[~]    ENTER YOUR INTERFACE : (DEFAULT IS Wi-Fi -> JUST PRESS ENTER)', end='')
        # inter = input()
        # if inter != '':
        #     pass
        # else:
        #     inter = 'Wi-Fi'
        sniff_packets(iface=inter)
    except Exception:
        rtxt('[!]    ERORR OCCURRED IN PACKET SNIFFER (HTTP SNIFFER)')


def http_sniffer_runner():
    ctxt('[~]    ENTER YOUR INTERFACE : (DEFAULT IS Wi-Fi -> JUST PRESS ENTER)', end='')
    inter = input()
    if inter != '':
        pass
    else:
        inter = 'Wi-Fi'
    listen2httpx(inter=inter)



if __name__ == '__main__':
    http_sniffer_runner()

