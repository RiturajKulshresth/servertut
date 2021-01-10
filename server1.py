import socket
""" sys is imported to take the port number as command line argument """
import sys 
""" To input the port number replace below line with the next one"""
PORT=int(sys.argv[1])
# PORT = 5001        # Port to listen on (non-privileged ports are > 1023)
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
""" Since python has an issue where backlog can't be less than 1 so backlog will always be there
    Hence I replaced it by restarting the same socket when the connection closes """
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen(0)        
        conn, addr = s.accept()
        ope, two=addr
        """ Socket is closed due to the issue with backlog so that an error is given for further connections
            and the loop continues for the next connection when this one terminates """
        s.close()

        with conn:
            print('Connected with client socket number', two)
            """ In order to catch the errors put the whole block in Try Catch"""
            try: 
                while True:    
                    data = conn.recv(1024)                    
                    oper=data.decode('UTF-8')
                    oper1=oper[:len(oper)-1]
                    print("Client socket", two, "sent message:",oper1)
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
                    conn.sendall(bite.encode('utf-8'))
                    if not data:
                        break
            except:
                pass
        conn.close()
