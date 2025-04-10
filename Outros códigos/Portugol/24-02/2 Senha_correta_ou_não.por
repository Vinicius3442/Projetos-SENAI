//Atividade 2 Vinicius Montuani
programa {
  funcao inicio() {
    cadeia senha, senha_correta
    senha_correta = "Vinicius"

    escreva("Digite sua senha: \n")
    leia(senha)

    enquanto (senha_correta != senha) //Fiquei um tempo enorme quebrando a cabeça para descobrir porque não estava funcionado, no portugol Web o "diferente" é != e não <>.
    {
      escreva("Senha incorreta, digite novamente: \n")
      leia(senha)
    }
    
    escreva("Senha correta, acesso concedido!")
    
  }
}

