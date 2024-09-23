
import { faker } from '@faker-js/faker';
import { br } from 'faker-br/lib/locales/pt_BR';

describe('Acesso e Cadastro', () => {
    const baseUrl = 'https://qastage.buildbox.one/18/cadastro/';
    const randomFName = faker.person.firstName();
    const randomLName = faker.person.lastName();
    const randomEmail = faker.internet.email();
    const randomNumEnd = faker.string.numeric(3);  // Opção simples de 3 numeros (pode ser usado pra CPF dependendo do programa)
    const randomPassword = faker.internet.password(12, true, /[a-zA-Z0-9!@#$%^&*]/);
    // Randomizando data de nascimento e formatando para DD/MM/YYYY
    const dataNasc  = faker.date.birthdate({ min: 18, max: 70, mode: 'age' });
    const formattedDate = dataNasc.toLocaleDateString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric' 
    });
    // Funcção para gerar CPFS
    function gerarCPFValido() {
        const randomDigit = () => Math.floor(Math.random() * 10);
        let cpf = '';
    
        // Gera os primeiros 9 dígitos
        for (let i = 0; i < 9; i++) {
            cpf += randomDigit();
        }
        // Função para calcular dígito verificador
        const calcularDigito = (cpfBase) => {
            let soma = 0;
            let peso = cpfBase.length + 1;
            for (let i = 0; i < cpfBase.length; i++) {
                soma += cpfBase[i] * peso--;
            }
            const resto = soma % 11;
            return resto < 2 ? 0 : 11 - resto;
        };
        // Calcula os dois dígitos verificadores
        const digito1 = calcularDigito(cpf);
        const digito2 = calcularDigito(cpf + digito1);
    
        // Retorna o CPF completo (9 dígitos base + 2 dígitos verificadores)
        return cpf + digito1 + digito2;
    }
    const cpfValido = gerarCPFValido();


    it('Acesso e Cadastro com Sucesso', () => {
        cy.visit(baseUrl);
        cy.get('[data-cy="button-btn-enroll"]').click();
        cy.log();
        // Parte 1 do cadastro
        cy.get('[data-cy="input-signup-personal-data-firstName"]').type(randomFName);
        cy.get('[data-cy="input-signup-personal-data-lastName"]').type(randomLName);
        cy.get('[data-cy="input-signup-personal-data-birthDate"]').type(formattedDate);
        cy.get('[data-cy="input-signup-personal-data-cpf"]').type(cpfValido);
        cy.get('[data-cy="input-signup-personal-data-email"]').type(randomEmail);
        cy.get('[data-cy="input-signup-personal-data-email-confirm"]').type(randomEmail);
        cy.get('[data-cy="input-signup-personal-data-password"]').type(randomPassword);
        cy.get('[data-cy="input-signup-personal-data-password-confirm"]').type(randomPassword);
        cy.log('Email gerado:', randomEmail);
        cy.log('Senha gerada:', randomPassword);
        cy.contains('button', 'Selecione a proficiência...').click();
        cy.get('#dropdown-button-1 > .overflow-y-scroll > :nth-child(3)').click()
        cy.get('[data-cy="input-signup-personal-data-lgpd"]').click()
        cy.get('[data-cy="button-signup_submit_button_1"]').click();
        // Parte 2 do Cadastro
        cy.get('[data-cy="input-signup-address-cep"]').type('13013161{enter}')
        cy.wait(1000)
        cy.get('[data-cy="input-signup-address-number"]').type(randomNumEnd)
        cy.get('[data-cy="button-signup_submit_button_3"]').click()
        // Parte 3 - Acesso a plataforma
        cy.get('[data-cy="button-wide_window_button"]').click()
        cy.get('#user_login').type(randomEmail);
        cy.get('#user_pass').type(randomPassword);
        cy.get('#wp-submit').click()
        
    });
});