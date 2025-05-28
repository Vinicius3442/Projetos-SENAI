//Atividade 2 Vinicius Montuani
programa {
  funcao inicio() {
    cadeia senha, senha_correta
    senha_correta = "Vinicius"

    escreva("Digite sua senha: \n")
    leia(senha)

    enquanto (senha_correta != senha){
      escreva("Senha incorreta, digite novamente: \n")
      leia(senha)
    }
    
    escreva("Senha correta, acesso concedido!")
    
  }
}

