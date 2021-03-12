from django.shortcuts import render
from django.http import HttpResponseRedirect
import docker
import os
from .formulaire import MonFormulaire
from .models import *
def traitement(request):
    if request.method == 'POST':
        form = MonFormulaire(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            mon_fichier = open("Dockerfile", "w")
            mon_fichier.write(
                            "\nFROM ubuntu:latest"
                            "\nMAINTAINER "+data["nom"]+" <"+data["email"]+">\n"
                            "\nENV TZ=Europe/Paris\n"
                            "\nRUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone\n"
                            "\nRUN apt-get update\n"
                            "\nRUN apt-get -y upgrade\n"
                            "\nRUN apt-get install -y git\n"
                            "\nRUN apt-get -y install apache2\n"
                            "\nRUN mkdir /var/www/html/medibed\n"
                            
                            
                            "\nRUN git clone "+data["git_url"] +" /var/www/html/medibed\n"
                            "\nENV APACHE_RUN_USER www-data\n"
                            "\nENV APACHE_RUN_GROUP www-data\n"
                            "\nENV APACHE_LOG_DIR /var/log/apache2\n"
                            "\nENV APACHE_LOCK_DIR /var/lock/apache2\n"
                            "\nENV APACHE_PID_FILE /var/run/apache2.pid\n"
                            "\nEXPOSE 80\n"
                            "\nCMD /usr/sbin/apache2ctl -D FOREGROUND")


            mon_fichier.close()
            name = data["nom_image"]
            client = docker.from_env()
            client.images.build(path = "./",tag = name)
            os.system("docker login --username="+data["username"]+" --password="+data["password"])
            os.system("docker push  "+data["nom_image"])

        else:
            print(form.errors)
    else:
        form = MonFormulaire()

    return render(request, 'formulaire.html', {'form': form})