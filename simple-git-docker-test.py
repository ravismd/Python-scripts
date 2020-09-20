#!/usr/bin/python
import os
#import docker


#Stop and remove containers if any
os.system('docker ps -q --filter "name=simple-devops-container" | grep -q . && docker stop simple-devops-container && docker rm -fv simple-devops-container')

#Remove Docker images if any
if (os.system('docker images -q') == 0):
    os.system('docker rmi $(docker images -q)')

#Stop docker service if any
if (os.system('pgrep dockerd') == 0):
    os.system('service docker stop')
else: 
    print("Dcoker is already in stopped state")

os.chdir('/opt/docker')
os.system('cp /home/ec2-user/HelloWorld/Dockerfile .')
os.system("aws s3 cp s3://ananya123/webapp.war .")


#Start the Docker if the service is not started yet if started do nothing
if (os.system('pgrep dockerd') == 0):
    print("Docker is already running")
else:
    os.system('service docker start')

os.system("docker build -t simple-devops-image .")
os.system("docker run -d --name simple-devops-container -p 8080:8080 simple-devops-image")
