#Ilham Mansiez
#Kanjeng Userbot
#Tentang AKU DAN DIA
FROM  Aftahbagas/aftah-bagas-kanjeng:kanjeng-userbor

RUN git clone -b Kanjeng-Userbot https://github.com/AftahBagas/-KANJENG /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/AftahBagas/-KANJENG/Petercord-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
