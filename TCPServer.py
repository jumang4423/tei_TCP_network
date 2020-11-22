# coding: UTF-8
# サーバを作成

from socket import *

serverPort = 50000
serverAddress = '127.0.0.1'
# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
serverSocket = socket(AF_INET, SOCK_STREAM)

# IPアドレスとポートを指定
serverSocket.bind((serverAddress, serverPort))
# 1 接続
serverSocket.listen(1)
print('The server is ready to receive')
# connection するまで待つ
while True:
    # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
    connectionSocket, addr = serverSocket.accept()
    # データを受け取る
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    # クライアントにデータを返す
    connectionSocket.send(capitalizedSentence.encode())
    print('Data is correctly sent now.')
    connectionSocket.close()