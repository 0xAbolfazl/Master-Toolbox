from banner_cli import gtxt, rtxt, ctxt
from port_scanner_cli import auto_scan_port
from admin_panel_cli import auto_admin_panel_finder
from directory_cli import auto_diretory_search
from ip_details_cli import ip_information
from subdomain_finder_cli import full_scanner_subdomain_finder


def fullscan():
    try:
        ctxt("[?]    ENTER YOUR URL : [ex. https://www.site.ir] ", end="")
        rsite = input()
        if rsite == '':
            rtxt('[!]    ENTER VALID ADDRESS ')
            raise TypeError
        site = rsite

        del_l = ["https://www.", 'http://www.','https://', 'http://']
        for i in del_l :
            if i in rsite:
                site = rsite.replace(i, "")
                break
        ctxt("[#]    SCANNING STARTED ...")

        # ---------------------------------------------------

        ip_information(rsite)
        auto_scan_port(ip=site)
        auto_admin_panel_finder(site=rsite)
        full_scanner_subdomain_finder(uurl=site)
        auto_diretory_search(site=rsite)



    except Exception as er:
        rtxt("[!]    ERROR")
        print(er)




if __name__ == '__main__':
    fullscan()