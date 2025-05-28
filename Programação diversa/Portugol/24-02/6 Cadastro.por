//Atividade 6 Vinicius Montuani
programa {
  funcao inicio() {
    cadeia nome, email, endereco, cpf, sobrenome, entrada1, entrada2
    logico fim = falso

    escreva("Para efetuarmos o seu cadastro precisaremos de alguns dados\n")
    escreva("Digite o seu primeiro nome: ")
    leia(nome)
    escreva("Digite o seu sobrenome: ")
    leia(sobrenome)
    escreva("Digite o seu endereço: ")
    leia(endereco)
    escreva("Digite o seu CPF: ")
    leia(cpf)
    escreva("Digite o seu email: ")
    leia(email)

    enquanto (fim == falso) {
      limpa()
      escreva("Confirme seus dados: \nNome: ", nome, "\nSobrenome: ", sobrenome, "\nEndereço: ", endereco, "\nCPF: ", cpf, "\nEmail: ", email)
      escreva("\nOs dados estão corretos?\n")
      leia(entrada1)

      escolha (entrada1) {
        caso "Sim":
          fim = verdadeiro
          limpa()
          escreva("Cadastro efetivado")
          pare

        caso "Não":
          escreva("Qual dos dados está errado?\n")
          leia(entrada2)

          escolha (entrada2) {
            caso "Nome":
              escreva("Digite o nome novamente: ")
              leia(nome)
              pare

            caso "Sobrenome":
              escreva("Digite o sobrenome novamente: ")
              leia(sobrenome)
              pare

            caso "Endereço":
              escreva("Digite o endereço novamente: ")
              leia(endereco)
              pare

            caso "CPF":
              escreva("Digite o CPF novamente: ")
              leia(cpf)
              pare

            caso "Email":
              escreva("Digite o email novamente: ")
              leia(email)
              pare
          }
      }
    }
  }
}
//Esse foi difícil heim