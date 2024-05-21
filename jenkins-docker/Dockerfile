# Usar la imagen base oficial de Jenkins LTS
FROM jenkins/jenkins:lts

# Ejecutar Jenkins como root para instalar paquetes adicionales si es necesario
USER root

# Instalar Docker dentro del contenedor de Jenkins
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common -y

# Cambiar de nuevo al usuario jenkins
USER jenkins

# Exponer el puerto 8080 para la interfaz web de Jenkins y el puerto 50000 para los agentes
EXPOSE 8080
EXPOSE 50000

