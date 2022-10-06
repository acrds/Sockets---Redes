from socket import *
serverName = 'localhost'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    N = input("Digite o valor de N: ") 
    N = int(N) # Conversor a string to int

    for i in range(N): 
        i = str(i)  # Conversor to string and to send to server
        clientSocket.sendto(i.encode(),(serverName, serverPort)) 