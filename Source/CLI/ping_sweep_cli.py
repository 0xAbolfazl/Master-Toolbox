from subprocess import run, PIPE
from banner_cli import ctxt, rtxt, lbtxt, lmtxt, ytxt
from time import sleep
from scapy.all import ARP, Ether, srp
from tqdm import tqdm


def ping_sweep_method_2():
    try:
        def ping_sweep(network, start, end, timeout):
            active_ips = []
            ctxt('[~]    SCANNING STARTED ...')
            for ip in range(start, end + 1):
                address = f"{network}.{ip}"
                result = run(["ping", "-n", "1", "-w", timeout, address], stdout=PIPE, stderr=PIPE)
                if result.returncode == 0:
                    active_ips.append(address)
                else:
                    pass
                    # ytxt('[!]    NOTHING FOUND')

            if len(active_ips) != 0:
                for i in active_ips:
                    ctxt(f'[~]    {i} IS UP')
                    sleep(1)
            else:
                pass
                    # ytxt('[!]    NOTHING FOUND')


        get_ip = input('[?]    ENTER YOUR FIRST 3 SECTION OF YOUR IP (DEFAULT -> 192.168.1) : ')
        timeout = input('[?]    ENTER TIMEOUT (ms -> DEFAULT IS -> 500 JUST PRESS ENTER) :  ')
        last = (input('[?]    ENTER STAR POINT  (DEFAULT IS 1): '))
        last2 = input('[?]    ENTER END POINT  (DEFAULT IS 254): ')

        if get_ip == "":
            final_ip = '192.168.1'
        else :
            final_ip = get_ip

        if timeout == "":
            timeout = '500'
        else :
            timeout = str(timeout)

        if last == "":
            last = 1
        else:
            last = int(last)

        if last2 == "":
            last2 = 254
        else :
            last2 = int(last2)

        # try:
        #     last, last2 = int(last), int(last2)
        # except Exception:
        #     rtxt('[!]    YOU SHOULD ENTER INT INPUT')
        #     raise TypeError
        
        ping_sweep(network=final_ip, start=last, end=last2, timeout=timeout)
    except Exception as er:
        print(er)
        rtxt('[!]    ERORR OCCURRED IN PING SWEEP [METHOD 2]')
        
def ping_sweep_method_1():

    try:

        get_ip = input('[?]    ENTER YOUR FIRST 3 SECTION OF YOUR IP (DEFAULT -> 192.168.1) : ')
        timeout = input('[?]    ENTER TIMEOUT (ms -> DEFAULT IS -> 500 JUST PRESS ENTER) :  ')
        last = (input('[?]    ENTER STAR POINT  (DEFAULT IS 1): '))
        last2 = input('[?]    ENTER END POINT  (DEFAULT IS 254): ')


        if get_ip == "":
            final_ip = '192.168.1'
        else :
            final_ip = get_ip

        if timeout == "":
            timeout = 500
        else :
            timeout = int(timeout)

        if last == "":
            last = 1
        else:
            last = (last)

        if last2 == "":
            last2 = 254
        else :
            last2 = (last2)

        try:
            last, last2 = int(last), int(last2)
        except Exception:
            rtxt('[!]    YOU SHOULD ENTER INT INPUT')
            raise TypeError
            

        lbtxt("[!]    SCANNING YOUR NETWORK ...", end='\n\n')
        clients = []

        for i in (range(1)):
            for j in tqdm(range(last,last2+1)):
                # target_ip = f"{final_ip[0:int((final_ip.rfind('.')))+1]}{int(final_ip[(int((final_ip.rfind('.')))+1):])+j}"  # IP Address for the destination
                target_ip = f'{final_ip}.{j}'
                # print(final_ip[0:int((final_ip.rfind('.')))+1])
                # print(final_ip[(int((final_ip.rfind('.')))+1)+i])
                arp = ARP(pdst=target_ip) # create ARP packet
                ether = Ether(dst="ff:ff:ff:ff:ff:ff")# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
                packet = ether/arp# stack them
                result = srp(packet, timeout=timeout/1000, verbose=0)[0]
                for sent, received in result:    # for each response, append ip and mac address to `clients` list
                    clients.append(f'       {received.psrc}{(15-len(str(received.psrc)))*" "}        {received.hwsrc}')

        lmtxt("\n[+]    AVAILABLE DEVICE[S] IN YOUR NETWORK:")
        ctxt("       IP" + " "*24+"MAC") # 192.168.100.100
        ctxt('       -----------------------------------------------')
        printed = []
        for i in clients:
            if i not in printed:
                printed.append(i)
                ytxt(i)
                # gtxt(text=' IS ALIVE', end='\n')
            else:
                pass
    except Exception as d:
        rtxt(d)
        rtxt('[!]    ERROR OCCURRED IN PING SWEEP -> METHOD #2')



def ping_sweep_runner():
    try:
        print()
        lbtxt('[~]    SELECT YOUR METHOD,  1 OR 2 (1 IS RECOMMENDED) :', end='')
        ask_method = input()
        if ask_method == '1':
            ping_sweep_method_1()
        elif ask_method == '2':
            ping_sweep_method_2()
        else:
            try:
                rtxt('[!]    JUST PRESS 1 OR 2 !')
            except Exception:
                print('[!]    JUST PRESS 1 OR 2 !')
    except Exception:
        print("[!]    ERORR")


if __name__ == '__main__':
    ping_sweep_runner()

