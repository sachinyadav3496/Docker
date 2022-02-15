import os
import subprocess

status, output = subprocess.getstatusoutput('docker ps -a')

first = True
for docker_id in output.split('\n'):
    if first:
        first = False
        continue
    id_ = docker_id.split(' ')[0]
    command = f"docker rm {id_}"
    try:
        status, output = subprocess.getoutput(f"docker stop {id_}")
    except:
        pass
    status, output = subprocess.getstatusoutput(command)
    if status == 0:
        print(f"Container {id_} has been deleted Sucessfully!")

    
