#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost',1234))

mySocket.listen(5)

try:
	while True:

		numRand = str(random.randrange(999999999))
		newUrl = "http://localhost:1234/" + numRand

		print("Waiting for connections")
		(recvSocket,address) = mySocket.accept()
		print("HTTP request received:")
		print(recvSocket.recv(1024))
		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
        	         	"<html><body><h1>Hola. </body></h1></html>" + "<a href=" + newUrl + ">Dame otra.</a>" +
            	        "\r\n","utf-8"))
		recvSocket.close()

except KeyboardInterrupt:
	print("Connection interrupted")