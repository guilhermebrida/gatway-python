import socket
from threading import Thread
import time
import psycopg2
import os
import logging

logging.basicConfig(level=logging.INFO)

postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_PORT']
postgres_user = os.environ['POSTGRES_USER']
postgres_password = os.environ['POSTGRES_PASSWORD']
postgres_db = os.environ['POSTGRES_DB']

connection = psycopg2.connect(
    host=postgres_host,
    # host="postgres",
    port=postgres_port,
    user=postgres_user,
    password=postgres_password,
    dbname=postgres_db
)

cursor = connection.cursor()

def insertMessage(msg):
    try:
        cursor.execute(f"INSERT INTO public.iridium (received_message) VALUES ('{msg}')")
        connection.commit()
    except Exception as e:
        logging.error("Erro ao inserir mensagem no banco de dados")
        logging.error(e)



def receiveMessage():
    print((host, porta))
    # print(f"Conexão estabelecida com {endereco_cliente}")
    try :
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, porta))
            s.listen()
            print(f"Aguardando conexões em {host}:{porta}...")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    logging.info(" ===================================================================================")
                    logging.info(" == main()")
                    response,addr = sock.recvfrom(1024)
                    if response:
                        # print(" response: ", response.decode())
                        logging.info(" response: " + response.decode())
                        insertMessage(response.decode())
                    time.sleep(2)
    except KeyboardInterrupt:
        logging.error("CRLT + C")            


def main():
    logging.info(" start main()")
    Thread(target=receiveMessage).start()

if __name__ == "__main__":
    try:
        # host = '0.0.0.0'
        host = '172.18.0.3'
        porta = 10116
        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        main()
    except KeyboardInterrupt:
        logging.error("Finalizando")