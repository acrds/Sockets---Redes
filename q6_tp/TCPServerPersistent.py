from socket import *
serverPort = 12006

serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)
print('Server on!')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Conected in: {addr}")
    
    connectionSocket.recv(1024)     # Aguarda first message
    welcome = "Olá! Bem-vindo! Qual seu nome?"
    connectionSocket.send(welcome.encode())

    name = connectionSocket.recv(1024).decode() #Aguarda name
    
    services = f"""
    Certo, {name}! Como posso te ajudar?
    Digite o número que corresponde à opção desejada:

    1 - Agendar um horário de monitoria
    2 - Listar as próximas atividades da disciplina
    3 - E-mail do professor
    """
    connectionSocket.send(services.encode())

    number = connectionSocket.recv(1024).decode()

    message = ""
    if number == "1":
        message = "Para agendar uma monitoria, basta enviar um email para cainafigueiredo@poli.ufrj.br"
    elif number == "2":
        message = """
        Fique atento para as datas das próximas atividades. Confira o que vem por aí!

        P1: 26 de Maio de 2022
        Lista 3: 29 de Maio de 2022
        """
    elif number == "3":
        message = """
        Quer falar com o professor?
        O email dele é sadoc@ic.ufrj.br
        """

    goodbye = "\nObrigado por utilizar nossos serviços! Até logo!"
    message = message + goodbye
    connectionSocket.send(message.encode())
    
    connectionSocket.close()