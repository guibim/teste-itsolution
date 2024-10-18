# Projeto de Testes de Cadastro - Treinamento em Python/Selenium e JavaScript/Cypress <br />
Teste ITSolution com geração de dados fake utilizando API Faker <br />

Este repositório contém dois exemplos de automação de testes de cadastro, um utilizando Python com Selenium e outro utilizando JavaScript com Cypress.<br />

💻 ## Tecnologias Utilizadas <br />

VSCode: Editor de código utilizado para desenvolvimento do projeto. <br />
Python: Linguagem utilizada para o exemplo com Selenium. <br />
JavaScript: Linguagem utilizada para o exemplo com Cypress. <br />
Selenium: Framework de automação de testes baseado em Python. <br />
Cypress: Framework de automação de testes baseado em JavaScript. <br />

📂 ## Estrutura do Projeto <br />
O projeto possui dois diretórios principais: <br />
 
teste-qa-itsolution-python: Contém o código em Python utilizando Selenium para automação dos testes de cadastro. <br />
teste-itsolutions.cy.js: Contém o código em JavaScript utilizando Cypress para automação dos testes de cadastro. <br />

📂 ## Gherkin - BDD
Funcionalidade: Cadastro de usuário no sistema <br />

  Cenário: Realizar o cadastro de um novo usuário com sucesso <br />
    Dado que o usuário acessa a página de cadastro <br />
    E clica no botão para iniciar o cadastro <br />
    E preenche os dados pessoais  <br />
    E seleciona a proficiência do usuário <br />
    E aceita os termos de LGPD <br />
    Quando o usuário submete o formulário de cadastro <br />
    E preenche o endereço <br />
    Então o cadastro é finalizado com sucesso <br />
    E o usuário consegue acessar a plataforma com as credenciais cadastradas <br />
