import socket
from threading import Thread
import time
import psycopg2
import os

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
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (msg,))
    connection.commit()



def receiveMessage():
    print((host, porta))
    try :
        while True:
            print("===================================================================================")
            print("== main()")
            response,addr = sock.recvfrom(1024)
            if response:
                print(" response: ", response)
                insertMessage(response)
            time.sleep(2)
    except KeyboardInterrupt:
        print("CRLT + C")            


def main():
    print("start main()")
    Thread(target=receiveMessage).start()

if __name__ == "__main__":
    try:
        host = '0.0.0.0'
        porta = 10116
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((host, porta))
        main()
    except KeyboardInterrupt:
        print("Finalizando")