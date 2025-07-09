def dti():
    try:
        from socket import gethostbyname
        from banner_cli import ctxt, lbtxt, rtxt, ytxt, lmtxt
        ctxt("ENTER  YOUR ADDRESS : [ex. site.ir] ", end='')
        xurl = input('')
        if xurl == '':
            rtxt("[!]    PLEASE ENTER VALID ADDRESS !")
            raise TypeError
        
        ipadd = gethostbyname(xurl)
        print()
        ytxt(f'  [+]    IP ADDRESS OF ', end='')
        lbtxt(f'{xurl}', end='')
        ytxt(f' IS => ', end='')
        lbtxt(f'{ipadd}')
    except Exception:
        rtxt('[!]   Error occurred [dti]!')



if __name__ == '__main__':
    dti()
