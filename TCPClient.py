from socket import *

serverAddress = '127.0.0.1'
serverPort = 50000

# socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect
clientSocket.connect((serverAddress, serverPort))
sentence = input('lowercase into uppercase:')

# send
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())
#close
clientSocket.close()