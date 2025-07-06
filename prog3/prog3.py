import socket
import json
import sys
import time
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

# Classe do servidor
class Server:
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        logging.info(f'Listening on: {host}:{port}')

    def wait_connection(self):
        return self.server.accept()

    def receive_data(self, conn):
        buffer = b''
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break
            buffer += chunk
        conn.close()
        data = json.loads(buffer.decode('utf-8'))
        data['final-time'] = time.time()
        return data

# Parse de argumentos da CLI
def parse_args():
    return dict(arg.split('=', 1) for arg in sys.argv[1:])

# Execução principal
args = parse_args()
port = int(args.get('port', 5001))

server = Server(host='0.0.0.0', port=port)

while True:
    conn, addr = server.wait_connection()
    package = server.receive_data(conn)

    logging.info('-------------Received matrix------------')

    if 'det' in package:
        logging.info(f'Determinant: {package["det"]}')
        interval = package['final-time'] - package['initial-time']
        logging.info(f'Time interval: {interval:.6f} seconds')