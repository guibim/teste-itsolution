from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time
import random

faker = Faker('pt_BR')

# Função para gerar CPF válido


def gerar_cpf_valido():
    def random_digit():
        return random.randint(0, 9)

    cpf = [random_digit() for _ in range(9)]

    def calcular_digito(cpf_base):
        peso = len(cpf_base) + 1
        soma = sum([int(cpf_base[i]) * (peso - i)
                   for i in range(len(cpf_base))])
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    digito1 = calcular_digito(cpf)
    digito2 = calcular_digito(cpf + [digito1])

    cpf.append(digito1)
    cpf.append(digito2)

    return ''.join(map(str, cpf))


# Geração de dados via API Faker
random_fname = next(name for name in iter(faker.first_name, None) if len(
    name) >= 4)  # Nome precisa conter 4 letras
random_lname = faker.last_name()
random_email = faker.email()
random_password = faker.password(
    length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
random_num_end = faker.building_number()
cpf_valido = gerar_cpf_valido()
data_nasc = faker.date_of_birth(
    minimum_age=18, maximum_age=70).strftime('%d/%m/%Y')


driver = webdriver.Chrome()

try:
    # Acessar URL base
    base_url = 'https://qastage.buildbox.one/18/cadastro/'
    driver.get(base_url)

    # Espera para o elemento do botão de cadastro aparecer
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="button-btn-enroll"]'))
    ).click()

    # Parte 1 do cadastro
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-firstName"]'))
    ).send_keys(random_fname)

    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-lastName"]').send_keys(random_lname)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-birthDate"]').send_keys(data_nasc)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-cpf"]').send_keys(cpf_valido)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-email"]').send_keys(random_email)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-email-confirm"]').send_keys(random_email)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-password"]').send_keys(random_password)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-password-confirm"]').send_keys(random_password)

    # Selecionar proficiência
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[span[contains(text(), "Selecione a proficiência...")]]'))
    ).click()
    time.sleep(5)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#dropdown-button-1 > .overflow-y-scroll > :nth-child(3)'))
    ).click()

    # Marcar caixas obrigatorias
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-personal-data-lgpd"]').click()
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="button-signup_submit_button_1"]').click()

    # Parte 2 do cadastro
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="input-signup-address-cep"]'))
    ).send_keys('13013161', webdriver.common.keys.Keys.ENTER)

    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="input-signup-address-number"]').send_keys(random_num_end)
    time.sleep(5)
    driver.find_element(
        By.CSS_SELECTOR, '[data-cy="button-signup_submit_button_3"]').click()

    # Login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="button-wide_window_button"]'))
    ).click()

    # Verificação de iframes para o Selenium
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if len(iframes) > 0:
        driver.switch_to.frame(iframes[0])

    # Login
    driver.find_element(By.ID, 'user_login').send_keys(random_email)
    driver.find_element(By.ID, 'user_pass').send_keys(random_password)
    driver.find_element(By.ID, 'wp-submit').click()

    time.sleep(5)

finally:
    driver.quit()
