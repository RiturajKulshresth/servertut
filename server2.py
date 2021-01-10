import sys
import time
import errno
import socket 
import threading
import multiprocessing
from multiprocessing import Process

def threaded(conn,addr): 
    try:
        while True: 
            data = conn.recv(1024) 
            oper=data.decode('UTF-8')
            oper1=oper[:len(oper)-1]
            print("Client socket", addr[1], "sent message:",oper1)
            op1=int(oper1[:oper1.find(" ")])
            op2=int(oper1[oper1.rfind(" ")+1:])
            opt=oper1[oper1.find(" ")+1:oper1.rfind(" ")]
            if(opt=="+"):
                cat=op1+op2
            if(opt=="-"):
                cat=op1-op2
            if(opt=="*"):
                cat=op1*op2

            """ Did not convert the answer of division operator to int because a 
            person may want a decimal value"""

            if(opt=="/"):
                cat=op1/op2
            bite=str(cat)
            print ("Sending reply:", bite)
            conn.send(bite.encode('utf-8')) 
            if not data: 
                break
    except:
        pass
    conn.close()
    sys.exit(0)
  
def Main(): 
    HOST = '127.0.0.1'
    PORT=int(sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((HOST, PORT)) 
    s.listen(16) 
    while True: 
        try:
            conn, addr = s.accept()
            p=Process(target=threaded, args=(conn,addr,))
            p.start()
        except socket.error:
            print ("socket error")
        print('Connected with client socket number', addr[1]) 
    s.close() 
if __name__ == '__main__': 
    Main() 