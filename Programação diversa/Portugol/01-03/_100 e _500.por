//Atividade 3 Vinicius Montuani
programa {
  funcao inicio() {
    inteiro entrada

    escreva("Digite um número inteiro qualquer:\n")
    leia(entrada)

    se(entrada < 100 ou entrada > 500){
    escreva("O numero digitado foi: ", entrada, " o numero esta FORA do intervalo de 100 e 500")
    }
    senao{
      escreva("O numero digitado foi: ", entrada, " o numero esta DENTRO do intervalo de 100 e 500")
    }

  }
}
