import socket, sys
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])
conn.connect((host, port))
print("Connected to host " + sys.argv[1])
td = 1
while td == 1:
   msg = input('MSG:  ')
   print('sending: {}'.format(msg))
   conn.sendall(msg.encode())
   print('sent: {}'.format(msg))
   if msg == 'killsrv':
       print('disconnecting client session')
       break

conn.close()
