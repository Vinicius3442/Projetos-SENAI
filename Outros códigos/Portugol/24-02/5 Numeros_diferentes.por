//Atividade 5 Vinicius Arcanjo Lobato Montuani N 29 2 DEV B
programa {
  funcao inicio() {
    inteiro num1, num2
    
    escreva("Digite 2 numeros inteiros diferentes!\n")
    escreva("Digite o primeiro numero: ")
    leia(num1)

    escreva("Digite o segundo numero: ")
    leia(num2)

     se(num1 != num2){
        escreva("Os numeros digitados foram: ", num1," e ", num2)
     }

    enquanto(num1 == num2){
      escreva("Escolha numeros DIFERENTES, tente novamente:\n")
      escreva("Digite o primeiro numero: ")
      leia(num1)
      escreva("Digite o segundo numero: ")
      leia(num2)

      se(num1 != num2){
        escreva("Os numeros digitados foram: ", num1," e ", num2)
      }
    }
    
  }
}
