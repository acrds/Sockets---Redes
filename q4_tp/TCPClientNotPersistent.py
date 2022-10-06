from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

while(True):
    N = input("Digite o valor de N: ")
    N = int(N)     # Conversor a string to int

    for i in range(N):
        i = str(i)
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort)) 
        clientSocket.send(i.encode()) 
        clientSocket.close()