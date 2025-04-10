//Atividade 12 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  funcao inicio() {
    inteiro entrada

    escreva("Digite um número inteiro: ")
    leia(entrada)

    se(entrada % 3 == 0){
      escreva("O número é divisivel por 3\n")
    }
    senao se(entrada % 3 == 1){
      escreva("O número não é divisivel por 3\n")
    }

    se(entrada % 7 == 0){
      escreva("O número é divisivel por 7")
    }

    senao se(entrada < 7){
      escreva("O número não é divisivel por 7")
    }

    senao se(entrada % 7 == 1){
      escreva("O número não é divisivel por 7")
    }
  }
}
