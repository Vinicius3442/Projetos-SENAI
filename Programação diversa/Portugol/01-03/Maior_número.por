//Atividade 7 Vinicius Montuani
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    inteiro num1, num2, maior

    escreva("Digite um número inteiro: ")
    leia(num1)

    escreva("Digite outro número inteiro: ")
    leia(num2)

    se(num1 == num2){
      limpa()
      escreva("Escreva 2 números DIFERENTES!")
    }
    senao{
      limpa()
      maior = mat.maior_numero(num1, num2)
      escreva("O maior numero é o ", maior)
    }
  }
}
