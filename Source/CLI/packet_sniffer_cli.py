def packet_sniffer():
    try:
        from banner_cli import rtxt, ctxt
        from scapy.all import sniff
        from http_sniffer_cli import listen2httpx
        # sniff(filter="ip", prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}"))
        ctxt('[~]    ENTER YOUR INTERFACE (DEFAULT IS Wi-Fi -> JUST PRESS ENTER) : ', end='')
        inter = input()
        if inter != '':
            pass
        else:
            inter = 'Wi-Fi'
        ctxt(f'[?]    WHICH TYPE OF PACKET YOU WANT TO SNIFF ? 1- HTTP SINFFER\n{48*" "}2- ALL PACKET\n{48*" "}3- SOMETHING OTHER')
        uc = input('...    YOUR SELECT : ')
        if uc == '1':
            listen2httpx(inter=inter)
        elif uc == '2':
            ctxt("SNIFFING STARTED ...")
            sniff(prn=lambda x:x.summary(),filter='', iface = inter)
        elif uc == '3':
            ctxt("[?]    ENTER YOUR FILTER : ", end='')
            ucc = input('')
            ctxt("SNIFFING STARTED ...")
            sniff(prn=lambda x:x.summary(), filter=ucc, iface = inter)
        else:
            rtxt('[!] YOUR CHOICE SHOULD BE BETWEEN 1, 2 OR 3 !')

    except Exception:
        rtxt('[!]   Error ocurred !')



if __name__ == '__main__':
    packet_sniffer()