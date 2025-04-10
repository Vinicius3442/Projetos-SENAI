//Atividade 2 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  inclua biblioteca Texto --> tx
  funcao inicio() {
    cadeia senha, entrada
    logico fim
    senha = "PORTUGOL"

    escreva("Digite sua senha:\n")
    leia(entrada)
    entrada = tx.caixa_alta(entrada)//Usei o manual para achar essa função
    se(senha != entrada){
      limpa()
      escreva("Senha inválida")
    }
    senao{
      limpa()
      escreva("Senha válida")
    }
    }
  }
