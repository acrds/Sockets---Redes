from socket import * #forma a base de todas as comunicações de rede em Python
serverName = 'localhost' #cadeia contendo ou o endereço IP do servidor (por exemplo, “128.138.32.126”) ou o nome de hospedeiro do servidor (por exem- plo, “cis.poly.edu”
serverPort = 12000  #define a variável inteira serverPort como 12000. (port aleatória)
clientSocket = socket(AF_INET, SOCK_DGRAM)  #cria o socket do cliente, denominado clientSocket. O primeiro parâmetro indica a família do endereço; em particular, AF_INET indica que a rede subjacente está usando IPv4. 
#O segundo parâmetro indica que o socket é do tipo SOCK_DGRAM, o que significa que é um socket UDP (em vez de um socket TCP).

while True:
    message = input("Input lowercase sentence: ")
    clientSocket.sendto(message.encode(),(serverName, serverPort)) 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
    print(modifiedMessage.decode())
    print(f"Server Address: {serverAddress}")