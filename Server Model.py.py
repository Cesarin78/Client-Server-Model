from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('127.0.0.1',serverPort))
#serverSocket.listen(1)
print('We are ready to receive. SEND IT. ')

clients = []
print("connected")
while True:
   sentence, clientAddress = serverSocket.recvfrom(1024)
   if clientAddress not in clients:
    clients.append(clientAddress)

   sentence = sentence.decode() 
   #connectionSocket, addr = serverSocket.accept()
   print("A new client has connected: {clientAddress}")
    
   for client in clients:
        if(client != clientAddress):
            serverSocket.sendto(sentence.encode(), client)
        #connectionSocket.close()
    
