# Projeto de Testes de Cadastro - Treinamento em Python/Selenium e JavaScript/Cypress
Teste ITSolution com geração de dados fake utilizando API Faker

Este repositório contém dois exemplos de automação de testes de cadastro, um utilizando Python com Selenium e outro utilizando JavaScript com Cypress.

💻 Tecnologias Utilizadas
Ferramentas
VSCode: Editor de código utilizado para desenvolvimento do projeto.
Python: Linguagem utilizada para o exemplo com Selenium.
JavaScript: Linguagem utilizada para o exemplo com Cypress.
Selenium: Framework de automação de testes baseado em Python.
Cypress: Framework de automação de testes baseado em JavaScript.

📂 Estrutura do Projeto
O projeto possui dois diretórios principais:

teste-qa-itsolution-python: Contém o código em Python utilizando Selenium para automação dos testes de cadastro.
teste-itsolutions.cy.js: Contém o código em JavaScript utilizando Cypress para automação dos testes de cadastro.

Funcionalidade: Cadastro de usuário no sistema

  Cenário: Realizar o cadastro de um novo usuário com sucesso
    Dado que o usuário acessa a página de cadastro
    E clica no botão para iniciar o cadastro
    E preenche os dados pessoais 
    E seleciona a proficiência do usuário
    E aceita os termos de LGPD
    Quando o usuário submete o formulário de cadastro
    E preenche o endereço
    Então o cadastro é finalizado com sucesso
    E o usuário consegue acessar a plataforma com as credenciais cadastradas
