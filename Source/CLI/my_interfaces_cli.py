from psutil import net_if_addrs
from banner_cli import ctxt, rtxt, mtxt, lbtxt

def my_interfaces():
    try:
        my_interface = net_if_addrs()
        if len(my_interface) != 0:
            mtxt('-------------------------------')
            lbtxt("## TOTAL INTERFACE : {}".format(len(my_interface)))
            x = 0
            for i in my_interface:
                x+=1
                ctxt('#{} '.format(x)+i)
            mtxt('-------------------------------')
        else:
            print("NOTHING FOUNDED")
    except Exception:
        rtxt('[!]    ERROR OCURRED WHILE GETTING INTERFACES !')

if __name__ == '__main__':
    my_interfaces()