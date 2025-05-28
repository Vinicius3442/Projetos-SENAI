//Atividade 1 Vinicius Montuani N°29
programa {
  funcao inicio() {
    inteiro entrada

    escreva("Digite um número qualquer: ")
    leia(entrada)

    se (entrada > 100) {
      escreva("O numero é MAIOR que 100")
    }
    senao se (entrada < 100) {
      escreva("O numero é MENOR que 100")
    }
    senao {
      escreva("O numero é IGUAL a 100")
    }
  }
}


