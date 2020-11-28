# WEB APIs

## Gitlab
Para buscar usuários por nome de usuário, por exemplo:  
`curl -X GET https://gitlab.com/api/v4/users?username=jack_smith`

## CEP
Para buscar o endereço do CEP, por exemplo:  
`curl -X GET https://cep.awesomeapi.com.br/json/05424020`

## Short Link
Para encurtar uma URL longa, por exemplo:  
`curl -X POST -d 'url=https://www.google.com' 'https://cleanuri.com/api/v1/shorten'`
