# coding: UTF-8
# クライアントを作成

from socket import *

serverAddress = '127.0.0.1'
serverPort = 50000

# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
#ソケットの作成(socket)
clientSocket = socket(AF_INET, SOCK_STREAM)

# サーバを指定(connect)
clientSocket.connect((serverAddress, serverPort))
sentence = input('lowercase into uppercase:')

# サーバにメッセージを送る(send)
clientSocket.send(sentence.encode())
# ネットワークのバッファサイズは1024。サーバからの文字列を取得する
modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())
#ソケットをクローズ(close)
clientSocket.close()