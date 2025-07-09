import win32serviceutil
import time
from banner_cli import rtxt, ctxt, ytxt, lmtxt


class WService:

    def __init__(self, service, machine=None, verbose=False):
        self.service = service
        self.machine = machine
        self.verbose = verbose
        
    @property
    def running(self):
        return win32serviceutil.QueryServiceStatus(self.service)[1] == 4

    def start(self):
        if not self.running:
            win32serviceutil.StartService(self.service)
            time.sleep(1)
            if self.running:
                if self.verbose:
                    lmtxt(f"[+]    {self.service} STARTED SUCCESSFULLY.")
                return True
            else:
                if self.verbose:
                    rtxt(f"[!]    Cannot start {self.service}")
                return False
        elif self.verbose:
            ytxt(f"[!]    {self.service} is already running.")
    
    def stop(self):
        if self.running:
            win32serviceutil.StopService(self.service)
            time.sleep(0.5)
            if not self.running:
                if self.verbose:
                    lmtxt(f"[+]    {self.service} stopped successfully.")
                    return True
            else:
                if self.verbose:
                    rtxt(f"[!]    Cannot stop {self.service}")
                return False
        elif self.verbose:
            ytxt(f"[!]    {self.service} is not running.")

    def restart(self):
        if self.running:
            win32serviceutil.RestartService(self.service)
            time.sleep(2)
            if self.running:
                if self.verbose:
                    lmtxt(f"[+]    {self.service} restarted successfully.")
                return True
            else:
                if self.verbose:
                    rtxt(f"[!]    Cannot start {self.service}")
                return False
        elif self.verbose:
            rtxt(f"[!]    {self.service} is not running.")


def main(action, service):
    service = WService(service, verbose=True)
    if action == "start":
        service.start()
    elif action == "stop":
        service.stop()
    elif action == "restart":
        service.restart()


def ip_router_runner():
    try:
        ctxt('[+]   1- ENABLE IP ROUTING\n      2- DISABLE IP ROUTING\n      3- RESTART SERVICE', end='\n\n')
        ytxt('[?]   YOUR CHOICE : ', end='')
        user_choice = input('')


        if user_choice == '1':
            main('start', 'RemoteAccess')
        elif user_choice == '2':
            main('stop', 'RemoteAccess')
        elif user_choice == '3':
            main('restart', 'RemoteAccess')
        else:
            rtxt('[!]   YOUR CHOICE MUST BE AN INTEGER BETWEEN (1 2 3) !')
    except Exception:
        rtxt('[!]    ERROR OCCURRED (admin access is required !) !')

# main('start', 'RemoteAccess')


# def _enable_windows_iproute():
#     """
#     Enables IP route (IP Forwarding) in Windows
# """
#     # enable Remote Access service
#     service = WService("RemoteAccess")
#     service.start()

# def enable_ip_route(verbose=True):
#     """
#     Enables IP forwarding
#     """
#     try:
#         if verbose:
#             print("[!] Enabling IP Routing...")
#         _enable_windows_iproute()
#         if verbose:
#             print("[!] IP Routing enabled.")
#     except Exception:
#         rtxt('[!]    Error occurred')


# if __name__ == '__main__' :
#     enable_ip_route()
