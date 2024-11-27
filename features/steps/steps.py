from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given(u'Entro na Página de contato do Instituto Joga Junto')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.jogajuntoinstituto.org/#Contato")


@when(u'Insiro meus dados')
def step_impl(context):
    context.driver.find_element(By.ID , "nome").send_keys("Cesar Kael")
    context.driver.find_element(By.ID , "email").send_keys("Kael@teste.com")
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN)
    context.driver.find_element(By.ID , "assunto").send_keys(Keys.ARROW_DOWN , Keys.TAB)


@when(u'"Envio a mensagem "Teste - Oi!"')
def step_impl(context):
    context.driver.find_element(By.ID, "mensagem").send_keys("Teste - Oi!")

@when(u'Clico no botão de envio')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="Contato"]/div[1]/form/button').click()
    context.driver.click()

    
@then (u"Fechar o navegador")
def step_impl(context):
  context.driver.quit()
