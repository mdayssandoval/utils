import argparse
from signal import signal, SIGINT
from sys import exit
import socket

def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

signal(SIGINT, handler)


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="File with hosts to check", required=True)

args=parser.parse_args()


file1 = open(args.file, 'r')

hosts = file1.readlines()

for host in hosts:
	host = host.strip()
	try:
		print(socket.gethostbyname(host))
	except:
		pass

print("Done!")