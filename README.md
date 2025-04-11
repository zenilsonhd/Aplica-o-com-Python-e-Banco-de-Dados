# Aplica-o-com-Python-e-Banco-de-Dados
.Introdução:

Este projeto tem como objetivo desenvolver uma aplicação web utilizando Flask e SQLite, que permita o gerenciamento de um cadastro de usuários por meio de operações CRUD — Criar, Listar, Atualizar e Deletar registros. A proposta também incluiu a criação de uma interface visual e funcionalidades interativas, como o botão para mostrar a lista de usuários.


. Estrutura do Banco de Dados:
 
Utilizamos o SQLite como banco de dados local. A aplicação cria um arquivo chamado meubanco.db, onde está armazenada a seguinte tabela:

 Tabela: usuarios
Campo	Tipo	Descrição
id	INTEGER	Chave primária, autoincrementável
nome	TEXT	Nome do usuário
email	TEXT	E-mail do usuário


 Bibliotecas Utilizadas:
 
Flask	- Framework web usado para criar as rotas, views e renderizar HTML;
SQLite3	- Biblioteca padrão para banco de dados relacional local;
HTML/CSS - Criação da interface;
JavaScript - Funcionalidade para mostrar e ocultar a lista de usuários.


 Funcionalidades Implementadas:
 
 Cadastro de usuário (nome e email);
 Listagem de todos os usuários;
 Atualização dos dados de um usuário;
 Exclusão de um usuário específico;
 Busca de usuários por nome;
 Interface visual;
 Botão para mostrar a lista de usuários.
