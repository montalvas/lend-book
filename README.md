# lend-book
Sistema de gestão para empréstimo de livros em django.

## Stage one:

* Iniciado o projeto e feitas as configurações iniciais
* Criado o app books
* Criado os modelos book e loan
* Definidas as urls, views e o template inicial
* Criado o super usuário
* Feitas algumas correções no modelo book

## Stage two:

* Criado o app users
    - Para que seja feita restrição de acesso por usuário
* Configurado em settings para reconhecer o diretório do projeto
* Adicionado bootstrap no template base
* Criado o template de cadastro de usuário
* Padrão de views como functions based views
* Configurada a view e o template de cadastro de usuário
* Configurada a validação de cadastro e login

## Stage three:

* Criado a model Category e adicionada a chave estrangeira na model Book
* Restrição de acesso aos livros por usuário
* Estilizar a home
* Criar a url dinâmica para acesso às informações do livro
* Estilizar a página de detalhes

## Stage Four

* Corrigido problemas de autenticação (detalhes do livro)
* Criado o formulário de informação do livro
* Modificado o model categoria para incluir o usuário como foreignkey
* Configurado o model empréstimo
* Criado no template a tabela de empréstimos
* Add link de logout

## Stage Five

* Alterado o design dos botões de login e cadastro
* add o link de logout na nav
* Criado o filtro para calcular os dias emprestados
* Criado um modal em base para cadastro de novo livro
* Criado formulario de cadastro em django forms

## Stage Six

* Add o botão de excluir

## Heroku

[Link](https://montalvas-lendbook.herokuapp.com/)
