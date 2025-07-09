def cli_v():
    try:
        from banner_cli import ctxt, lmtxt, rtxt, lbtxt, mtxt, gtxt, back_color
        from syn_flood_cli import syn_flood_function
        from ping_sweep_cli import ping_sweep_runner
        from arp_spoofing_cli import arp_sp
        from arp_spoofing_detector_cli import arp_spoofing_detector_runner 
        from http_sniffer_cli import http_sniffer_runner
        from packet_sniffer_cli import packet_sniffer
        from domain_to_ip_cli import dti                                       # socket
        from ip_routing_cli import ip_router_runner                            # win32serviceutil
        from port_scanner_cli import port_scanner_runner                       # tqdm - socket
        from my_mac_table_cli import my_mac_table as mc                        # subprocess
        from my_interfaces_cli import my_interfaces                            # psutil
        from wifi_tools_cli import wifi_runner                                 # pywifi - tqdm
        from directory_cli import diretory_search
        from admin_panel_cli import admin_panel_finder
        from full_scanner_cli import fullscan
        from subdomain_finder_cli import ssubdomain_func
        from ip_details_cli import ip_information_runner
        from syn_flood_detector_cli import syn_flood_detector_runner

    except Exception :
        pass

    banner = '''
    #####  |+|-------------------------------------|+|  #####
    #####  |||-/                                 \-|||  #####
    #####  |||   [  /\/\ @ $ T E R - T00L B0X  ]   |||  #####
    #####  |||   [   KHARAZMI 10th FESTIVAL    ]   |||  #####
    #####  |||   [       VERSIONS 2.2.0        ]   |||  #####
    #####  |||-\                                 /-|||  #####
    #####  |+|-------------------------------------|+|  #####
    '''

    x = 100
    colora=lmtxt

    colorc=mtxt
    colord=lbtxt
    ctxt(banner)
    ytxt=print


    back_color(' #---- BASED ON WIFI ATTACK -----------------', end='\n\n')
    ctxt('     + ATTACK +')
    banner_wifi = ['SYN FLOOD (ADSL ROUTER)']
    for i in banner_wifi:
        ctxt(f'       {x+(banner_wifi.index(i))}-  [+] ', end='');ytxt(i)
    print('')
    ctxt('     + DEFENCE +')
    banner_detector_wifi = ['SYN FLOOD DETECTOR (MONITORING MODE IS REQUIRED)']
    for i in banner_detector_wifi:
        ctxt(f'       {x+(banner_detector_wifi.index(i)+50)}-  [+] ', end='');ytxt(i)
    # ----------------------------------------------------------
    print('')
    back_color(' #---- MAN IN THE MIDDLE --------------------', end='\n\n')
    ctxt('     + ATTACK +')
    mitm_cli = ['ARP SPOOFING']
    for i in mitm_cli:
        ctxt(f'       {x+(mitm_cli.index(i)+100)}-  [+] ', end='');ytxt(i)
    print('')
    ctxt('     + DEFENCE +')
    mitm_cli = ['ARP SPOOFING DETECTOR']
    for i in mitm_cli:
        ctxt(f'       {x+(mitm_cli.index(i)+150)}-  [+] ', end='');ytxt(i)
    # ----------------------------------------------------------
    print('')
    # ----------------------------------------------------------
    back_color(' #---- BASED ON NETWORK ---------------------', end='\n\n')
    banner_cli = ['PING SWEEP', 'HTTP SNIFFER', 'PACKET SNIFFER', 'DOMAIN TO IP'
                ,'IP ROUTING (admin access is required !)', "PORT SCANNER", 'MY MAC TABLE', "MY INTERFACES", 'WIFI TOOLS']
    for i in banner_cli:
        ctxt(f'       {x+(banner_cli.index(i)+200)}-  [+] ', end='');ytxt(i)
    # ----------------------------------------------------------
    print('')
    wp_banner = ['DIRECTORY SEARCHER']
    back_color(' #---- BASED ON WORDPRESS -------------------', end='\n\n')
    for i in wp_banner:
        ctxt(f'       {(x+(wp_banner.index(i)))+300}-  [+] ', end='');ytxt(i)

    # ----------------------------------------------------------
    print('')
    web_banner = ['SUBDOMAIN FINDER', 'ADMIN PANEL FINDER', 'URL INFO', 'FULL SCAN (RECOMMENDED)']
    back_color(' #---- BASED ON WEB -------------------------', end='\n\n')
    for i in web_banner:
        ctxt(f'       {(x+(web_banner.index(i)))+400}-  [+] ', end='');ytxt(i)



    print('\n\n')


    # print('---------- test color ---------')
    # ctxt(' this is test of ctxt')
    # mtxt(' this is test of mtxt')
    # lmtxt(' this is test of lmtxt')
    # lbtxt(' this is test of lbtxt')
    # ytxt(' this is test of ytxt')
    # rtxt(' this is test of rtxt')

    while True:
        user_choice = (input("[~]  Enter your choice : "))
        y = 100

        try:
            user_choice = int(user_choice)
        except Exception:
            user_choice = str(user_choice)

        if user_choice == 100:
            syn_flood_function()
        elif user_choice == 150:
            syn_flood_detector_runner()



        elif user_choice == 100+y:
            arp_sp()
        elif user_choice == 150+y:
            arp_spoofing_detector_runner()



        elif user_choice == 200+y:
            ping_sweep_runner()
        elif user_choice == 201+y:
            http_sniffer_runner()
        elif user_choice == 202+y:
            packet_sniffer()
        elif user_choice == 203+y:
            dti()
        elif user_choice == 204+y:
            ip_router_runner()
        elif user_choice == 205+y:
            port_scanner_runner()
        elif user_choice == 206+y:
            mc()
        elif user_choice == 207+y:
            my_interfaces()
        elif user_choice == 208+y:
            wifi_runner()


        elif user_choice == 300+y:
            diretory_search()


        elif user_choice == 400+y:
            ssubdomain_func()
        elif user_choice == 401+y:
            admin_panel_finder()
        elif user_choice == 402+y:
            ip_information_runner()
        elif user_choice == 403+y:
            fullscan()



        elif user_choice == "q":
            break

        else:
            print("INCORRECT INPUT")



if __name__ == '__main__' : 
    cli_v()