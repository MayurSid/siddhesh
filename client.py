from Tkinter import *
import time
import socket              # Import socket module
import thread
import subprocess

class Windowing():
    def __init__(self,*args,**kwargs):
        try:
            self.root = Tk()
            self.root.resizable(width=FALSE , height=FALSE)
            try:
                thread.start_new_thread(self.server_sertting,("Server_thread",))
            except Exception as e:
                print e
            self.text = Entry(self.root, bd =10)
            self.Send = Button(self.root, text ="Send", command = self.send_message)
            self.Exit = Button(self.root, text ="Exit", command = self.exit_app)
            self.var = StringVar()
            self.var.set("Chatting")
            self.label = Label(self.root, textvariable=self.var )
            self.var = StringVar()
            self.var.set("Hi")
            self.respond = Label(self.root, textvariable = self.var)
            self.label.pack()
            self.respond.pack()
            self.text.pack()
            self.Send.pack()
            self.Exit.pack()
            self.root.mainloop()
        except Exception as e:
            print e
    
    def exit_app(self):
        sys.exit("Exiting...")

    def get_local_eth0_ip(self):
        temp = subprocess.Popen("ifconfig | awk '{print $2}'| grep \"addr\" | head -n 1 | cut -d':' -f2", stdout = subprocess.PIPE, shell=True)
        IP = temp.communicate()
        return IP[0]

    def send_message(self):
       try:
           self.client_socket = socket.socket()
           self.port  = 12345
           self.client_socket.connect(("10.24.217.13",self.port))
           self.client_socket.send(self.text.get())
           self.text.delete(0,last=len(self.text.get()))
           self.client_socket.close()
       except Exception as e:
            print e
    
    def server_sertting(self,threadName):
        try:
            s = socket.socket()      # Create a socket object
            port = 12345      
            self.ip_addr = self.get_local_eth0_ip()
            s.bind((self.ip_addr, port))        # Bind to the port
            s.listen(5)              # Now wait for client connection.
            while True:
               c, addr = s.accept()  # Establish connection with client.
               msg= c.recv(1024)
               #print msg
               self.var.set(msg)
               c.close()     
        except Exception as e:
            print e

obj = Windowing()
