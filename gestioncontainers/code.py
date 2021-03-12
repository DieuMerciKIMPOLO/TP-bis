#!/usr/bin/python3
import docker
import sys

mon_fichier = open("Dockerfile", "w")
mon_fichier.write(
                "\nFROM ubuntu:latest"
                "\nMAINTAINER nsimpore <simporenaimatou97@gmail.com>\n"
                "\nENV TZ=Europe/Paris\n"
                "\nRUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone\n"
                "\nRUN apt-get update\n"
                "\nRUN apt-get -y upgrade\n"
                "\nRUN apt-get install -y git\n"
                "\nRUN apt-get -y install apache2\n"
                "\nRUN mkdir /var/www/html/medibed\n"
                
                
                "\nRUN git clone "+sys.argv[1] +" /var/www/html/medibed\n"
                "\nENV APACHE_RUN_USER www-data\n"
                "\nENV APACHE_RUN_GROUP www-data\n"
                "\nENV APACHE_LOG_DIR /var/log/apache2\n"
                "\nENV APACHE_LOCK_DIR /var/lock/apache2\n"
                "\nENV APACHE_PID_FILE /var/run/apache2.pid\n"
                "\nEXPOSE 80\n"
                "\nCMD /usr/sbin/apache2ctl -D FOREGROUND")


mon_fichier.close()
"""user = sys.argv[2]
passw = sys.argv[3]"""
name = sys.argv[2]
client = docker.from_env()
print("Start Building your docker image...")
client.images.build(path = "./",tag = name)
#print("start pushing your docker image to docker hub")
#client.login(username= user, password= passw)
#for line in client.images.get(name):
print("verification de la creation de"+name)
print(client.images.get(name))
print("End ok")