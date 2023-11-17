import socket
import threading
import os
import psycopg2
import logging


#Variables for holding information about connections
connections = []
total_connections = 0

#Client class, new instance created for each connected client
#Each instance has the socket and address that is associated with items
#Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        postgres_host = "localhost"
        postgres_port = os.environ['POSTGRES_PORT']
        postgres_user = os.environ['POSTGRES_USER']
        postgres_password = os.environ['POSTGRES_PASSWORD']
        postgres_db = os.environ['POSTGRES_DB']

        self.connection = psycopg2.connect(
            host=postgres_host,
            # host="postgres",
            port=postgres_port,
            user=postgres_user,
            password=postgres_password,
            dbname=postgres_db
        )

        self.cursor = self.connection.cursor()
    
    def __str__(self):
        return str(self.id) + " " + str(self.address)
    
    #Attempt to get data from client
    #If unable to, assume client has disconnected and remove him from server data
    #If able to and we get data back, print it in the server and send it back to every
    #client aside from the client that has sent it
    #.decode is used to convert the byte data into a printable string
    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(32)
            except:
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                # try:
                #     connections.remove(self)
                # except Exception as e:
                #     logging.error("Erro ao remover conexão da lista de conexões")
                #     logging.error(e)
                break
            if data != "":
                print("ID " + str(self.id) + ": " + str(data.decode("utf-8")))
                self.insertMessage(data.decode("utf-8"))
                for client in connections:
                    if client.id != self.id:
                        client.socket.sendall(data)
                


    def insertMessage(self,msg):
        try:
            self.cursor.execute(f"INSERT INTO public.iridium (received_message) VALUES ('{msg}')")
            self.connection.commit()
        except Exception as e:
            logging.error("Erro ao inserir mensagem no banco de dados")
            logging.error(e)
# #Wait for new connections
# def newConnections(socket):
#     while True:
#         sock, address = socket.accept()
#         global total_connections
#         connections.append(Client(sock, address, total_connections, "Name", True))
#         connections[len(connections) - 1].start()
#         print("New connection at ID " + str(connections[len(connections) - 1]))
#         total_connections += 1

# def main():
#     #Get host and port
#     host = "0.0.0.0"
#     port = 10116

#     #Create new server socket
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind((host, port))
#     sock.listen(5)

#     #Create new thread to wait for connections
#     newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
#     newConnectionsThread.start()
    
# main()