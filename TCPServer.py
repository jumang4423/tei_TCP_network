from socket import *

serverPort = 50000
serverAddress = '127.0.0.1'
serverSocket = socket(AF_INET, SOCK_STREAM)

# ip adress and port
serverSocket.bind((serverAddress, serverPort))
# connect
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    # get
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    # send
    connectionSocket.send(capitalizedSentence.encode())
    print('Data is correctly sent now.')
    connectionSocket.close()