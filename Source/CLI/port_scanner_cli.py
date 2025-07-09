import socket
from banner_cli import ctxt, rtxt, lbtxt, lmtxt, mtxt
from tqdm import tqdm

def auto_scan_port(ip='empty'):
    ports = [21, 22, 23, 25, 53, 80, 110, 115, 111, 135, 137, 138, 139,
                        143, 194, 443, 445, 548, 587, 993, 995, 1701, 1723, 2083,
                        1433, 3306, 3389, 5632, 5432, 8008, 8080, 8443,5900, 25565,
                        515, 631, 3282, 5190, 5050, 4443, 1863, 6891, 1503, 5631, 5632, 6667]
    opens = list()
    final_opens = list()
    if ip != 'empty':
        addr = ip
    elif ip == 'empty':
        ctxt('[?]    ENTER YOUR ADDRESS : [ex. site.ir] ', end='')
        addr = input('')
    if addr == '':
        rtxt('[!]    ENTER VALID ADDRESS !')
        raise TypeError
    address = socket.gethostbyname(addr)
    mtxt('[+]    SCANNING STARTED ON  # ADDRESS : {}\n\t\t\t\b     # IP\t\b\b: {}\n\t\t\t\b     # TIMEOUT : {}\n\t\t\t\b     # PORT[S] : DEFAULT'.format(addr, address, '500ms'))
    for i in range(1):
        for port in tqdm(ports):
            try:
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.5)
                result = tcp.connect_ex((address, port))
                if result == 0:
                    opens.append(port)
                    # print(str(port)+' is open')
                    tcp.close()
            except Exception as er:
                rtxt('[!]    Error occurred in port scanner !')
                print(er)
            
    for i in opens:
        if i not in final_opens:
            final_opens.append(i)
    lbtxt("THESE ARE OPEN ON {} : ".format(addr))
    lmtxt(final_opens)

def custom_scan_port():
    ctxt("[?]    ENTER START PORT : ", end='')
    start = input('')
    ctxt("[?]    ENTER END PORT : ", end='')
    end = input('')
    ctxt("[?]    ENTER TIMEOUT (ms) : ", end='')
    timeout = input('')
    timeout2 = float(timeout)/1000
    ports = range(int(start), int(end)+1)
    opens = list()
    final_opens = list()
    ctxt('[?]    ENTER YOUR ADDRESS : [ex. site.ir] ', end='')
    addr = input('')
    if addr == '':
        rtxt('[!]    ENTER VALID ADDRESS !')
        raise TypeError
    address = socket.gethostbyname(addr)
    mtxt('###################################################')
    mtxt('[+]    SCANNING STARTED ON  # ADDRESS : {}\n\t\t\t\b     # IP\t\b\b: {}\n\t\t\t\b     # TIMEOUT : {}ms\n\t\t\t\b     # PORT[S] : RANGE {} - {}'.format(addr, address, timeout, start, end))
    for i in range(3):
        for port in tqdm(ports):
            try:
                socket.setdefaulttimeout((timeout2))
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = tcp.connect_ex((address, port))
                if result == False:
                    opens.append(port)
                    # print(str(port)+' is open')
                    tcp.close()
            except Exception as er:
                rtxt('[!]    Error occurred in port scanner !')
                print(er)
            
    for i in opens:
        if i not in final_opens:
            final_opens.append(i)
    lbtxt("THESE ARE OPEN ON {} : ".format(addr))
    lmtxt(final_opens)


def specific_scan_port():
    ctxt("[?]    ENTER PORT : [ex. site.ir] ", end='')
    port = int(input(''))
    ctxt("[?]    ENTER TIMEOUT (ms) : ", end='')
    timeout = input('')
    timeout2 = float(timeout)/1000
    opens = list()
    final_opens = list()
    ctxt('[?]    ENTER YOUR ADDRESS : ', end='')
    addr = input('')
    if addr == '':
        rtxt('[!]    ENTER VALID ADDRESS !')
        raise TypeError
    address = socket.gethostbyname(addr)
    mtxt('###################################################')
    mtxt('[+]    SCANNING STARTED ON  # ADDRESS : {}\n\t\t\t\b     # IP\t\b\b: {}\n\t\t\t\b     # TIMEOUT : {}ms\n\t\t\t\b     # PORT[S] : {}'.format(addr, address, timeout, port))
    for i in range(3):
        try:
            socket.setdefaulttimeout((timeout2))
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = tcp.connect_ex((address, port))
            if result == False:
                opens.append(port)
                # print(str(port)+' is open')
                tcp.close()
        except Exception as er:
            rtxt('[!]    Error occurred in port scanner !')
            print(er)
            
    for i in opens:
        if i not in final_opens:
            final_opens.append(i)
    if len(final_opens) != 0:
        lbtxt("[+]    PORT", end='')
        ctxt(f" {final_opens[0]}", end='')
        lbtxt(" IS OPEN ON", end='')
        ctxt(f" {addr}", end='')
    




def port_scanner_runner():
    ctxt("[~]    1- AUTO SCAN\n\t\b2- CUSTOM SCAN\n\t\b3- SPECIFIC PORT SCAN")
    user_choice_port = input('[?]    YOUR CHIOCE : ')
    try:
        if user_choice_port == '1':
            auto_scan_port()
        elif user_choice_port == '2':
            custom_scan_port()
        elif user_choice_port == '3':
            specific_scan_port()
        else:
            rtxt('[!]    YOUR CHOICE SHOULD BE 1, 2, OR 3 !')
    except Exception:
        pass







if __name__ == '__main__':
    port_scanner_runner()