//Atividade 1 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
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


