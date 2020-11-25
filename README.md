# app_musica_interativa
Aplicação Websocket com música interativa (API YouTube)
Esta aplicação tem como objetivo a interação dos usuários com músicas com um ambiente simples e prático, utilizando os conceitos da Internet das Coisas Musicais, Websockets e a API do YouTube.

Por meio da solução proposta todos os usuários conseguirão ouvir a mesma música e terão acesso a uma Playlist sincronizada e compartilhada em tempo real, concedendo a todos mecanismos de interação,  como pausar / reproduzir / avançar / voltar as músicas e alterar a barra de reprodução da música em execução.
Contará também com recursos de adicionar vídeos a Playlist e chat para conversas de texto.

A aplicação foi divida em duas partes: a do cliente e a do servidor.

No cliente será utilizando uma página HTML que proverá a interface para os usuários, em que os usuários realizarão ações que serão enviadas para servidor que terá a função de receber esses eventos e entregar para todos os usuários conectados.
Com isso o cliente terá duas funções básicas, uma enviar as ações dos usuários para servidor e, a outra, receber as informações de outros clientes do servidor.

O servidor, por sua vez, tem a função de receber todas as requisições dos clientes, verificar essas informações e enviar para todos os clientes conectados.

Os códigos fontes do cliente e do servidor estão em anexo
