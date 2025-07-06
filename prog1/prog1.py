import socket
import json
import numpy as np
import sys
import time
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

# Função para parsear argumentos da linha de comando
def parse_args():
    return dict(arg.split('=', 1) for arg in sys.argv[1:])

# Parâmetros recebidos via CLI
args = parse_args()
HOST = 'prog2'
PORT = int(args.get('port', 5001))
m = int(args['m'])
n = int(args['n'])
f = float(args['f'])

print({'args': args})

# Envio das matrizes
for _ in range(m):
    matrix = np.random.rand(n, n).tolist()
    payload = {
        'matrix': matrix,
        'initial-time': time.time()
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logging.info(f'Sending matrix to {HOST} on port: {PORT}')
        s.connect((HOST, PORT))
        s.sendall(json.dumps(payload).encode('utf-8'))

    time.sleep(1 / f)