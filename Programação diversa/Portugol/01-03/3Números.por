//Atividade 13 Vinicius Montuani
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    inteiro num1, num2,num3, maior_inicial, maior_final

    escreva("Digite o primeiro número inteiro: ")
    leia(num1)

    escreva("Digite o segundo número inteiro: ")
    leia(num2)

    escreva("Digite o terceiro número inteiro: ")
    leia(num3)

    se(num1 == num2 e num1 == num3 e num2 == num3){
      limpa()
      escreva("Número idênticos")
    }
      senao{
      maior_inicial = mat.maior_numero(num1, num2)
      maior_final = mat.maior_numero(maior_inicial, num3)
      escreva("O maior numero é o ", maior_final)
    }
  }
  }
