#!/usr/bin/python
import os


#Stop and remove containers if any
def stop_remove_dockerContainers():
    print("Removing Docker Containers")
    print("========================== ")
    os.system('docker ps -q --filter "name=simple-devops-container" | grep -q . && docker stop simple-devops-container && docker rm -fv simple-devops-container')

#Remove Docker images if any
def remove_dockerImages():
    print("\nRemoving Docker images")
    print("====================== ")
    if (os.system('docker images -q') == 0):
        os.system('docker rmi $(docker images -q)')


#Stop docker service if any
def stop_dockerServices():
	print("\nStopping Docker service")
    	print("==========================")
	if (os.system('pgrep dockerd') == 0):
    		os.system('service docker stop')
	else: 
    		print("Dcoker is already in stopped state")

#create docker folder in /opt and copy the required files to build docker images and containers
def env_paths():
	print("\nCreating Env Paths tight in place like /opt/docker etc..")
    	print("========================================================== ")
	if (os.path.exists("/opt/docker")):
    		print("Path is already there")
	else:
    		os.system('mkdir /opt/docker')
	os.chdir('/opt/docker')
	os.system('cp /home/ec2-user/HelloWorld/Dockerfile .')
	os.system("aws s3 cp s3://ananya123/webapp.war .")


#Start the Docker if the service is not started yet if started do nothing
def start_docker_service():
	print("\nStarting Docker services")
    	print("========================")
	if (os.system('pgrep dockerd') == 0):
    		print("Docker is already running")
	else:
    		os.system('service docker start')
	os.system("docker build -t simple-devops-image .")
	os.system("docker run -d --name simple-devops-container -p 8080:8080 simple-devops-image")

stop_remove_dockerContainers()
remove_dockerImages()
stop_dockerServices()
env_paths()
start_docker_service()
