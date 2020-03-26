# Service

Neste documento veremos como criar um serviço no linux, para rodar nosso
algortimo toda vez que o sistema for iniciado.

## Criando o serviço

Primeiramente devemos criar o nosso serviço com o seguinte comando:

    nano /etc/systemd/system/qrcode.service


## Programação do serviço

Aqui indicamos o serviço e qual o caminho do script que deve ser rodado

    [Unit]
    Description=Reconhecimento de carreta
    
    [Service]
    Type=simple
    ExecStart=/usr/bin/python /root/prod/rec-carreta/Alice.py
    
    [Install]
    WantedBy=multi-user.target

## Reinicie os serviços

Utilize o comando abaixo para recarregar os serviços:

    systemctl daemon-reload


## Inicie o serviço

Habilite o serviço e logo após inicie o mesmo:
    
    systemctl enable qrcode.service
    systemctl start qrcode.service


## Verifique o status do serviço 

Para verificar se o serviço está de pé execute o seguinte comando:

    systemctl status qrcode.service

## Parando o serviço
    
Utilize os comandos abaixo para parar, iniciar ou reiniciar o serviço:

    sudo systemctl stop qrcode.service      
    sudo systemctl start qrcode.service 
    sudo systemctl restart qrcode.service   