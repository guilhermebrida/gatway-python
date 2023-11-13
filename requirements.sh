#!/bin/bash

# Atualizar os pacotes do sistema
sudo apt update

# Instalar dependências
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Adicionar a chave GPG oficial do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Configurar o repositório estável do Docker
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Atualizar novamente após adicionar o repositório
sudo apt update

# Instalar o Docker
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Adicionar o usuário atual ao grupo docker (para usar o Docker sem sudo)
sudo usermod -aG docker $USER

# Instalar o Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Dar permissão de execução ao Docker Compose
sudo chmod +x /usr/local/bin/docker-compose

# Exibir informações sobre as versões instaladas
docker --version
docker-compose --version

