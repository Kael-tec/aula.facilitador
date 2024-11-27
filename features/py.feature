Feature: Formulario de Contato


  Scenario: Enviar Mensagem
    Given Entro na Página de contato do Instituto Joga Junto
     When Insiro meus dados
      And "Envio a mensagem "Teste - Oi!"
      Then Fechar o navegador