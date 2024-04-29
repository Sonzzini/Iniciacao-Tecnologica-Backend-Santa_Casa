# SANTACASA


- passos AWS:
  
ssh -i ~/.ssh/labsuser.pem ec2-user@54.146.194.209

sudo su

---

yum install docker -y

---

systemctl start docker

systemctl enable docker

systemctl status docker

---

sudo yum update -y

sudo amazon-linux-extras install docker

sudo service docker start

sudo usermod -a -G docker ec2-user

---

sudo curl -L "https://github.com/docker/compose/releases/download/v2.6.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

---

sudo yum install git -y

git clone [URL_DO_SEU_REPOSITÓRIO]

cd [NOME_DO_DIRETÓRIO]

---

docker-compose up --build -d



