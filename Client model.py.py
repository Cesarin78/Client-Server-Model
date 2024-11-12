from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = input('Send your message in lowercase sentences: ')

while (sentence != 'quit'):

    clientSocket.connect((serverName,serverPort))
    clientSocket.send(sentence.encode())
    modifiedSentence, serveraddress = clientSocket.recvfrom(1024)
    #int ("Them: "+modifiedSentence.decode())
    #sentence = input('Your turn: ')
    clientSocket.close()
            