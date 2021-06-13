#Ilham Mansiez
#Petercord Userbot
#Tentang AKU DAN DIA
FROM  ilhammansiz17/ilham-mansiez-petercord:Petercord-Userbot

RUN git clone -b Kanjeng https://github.com/AftahBagas/Kanjeng_ /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/AftahBagas/Kanjeng_/Kanjeng/requirements.txt

CMD ["python3","-m","userbot"]
