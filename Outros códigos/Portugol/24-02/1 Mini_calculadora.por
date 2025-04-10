//Atividade 1 Vinicius Arcanjo Lobato Montuani N 29 2 DEV B
programa {
  funcao inicio() {
    cadeia operacao
    real num1, num2

    escreva("Digite o primeiro numero: ")
    leia(num1)

    escreva("Digite o segundo numero: ")
    leia(num2)

    escreva("Escolha a operação matemática:\n")
    escreva("+ \n")
    escreva("- \n")
    escreva("* \n")
    escreva("/ \n")
    leia(operacao)

    escolha(operacao){
      caso "+" :
      escreva("O resultado da soma é: \n", num1 + num2)
      pare

      caso "-" :
      escreva("O resultado da subtração é: \n", num1 - num2)
      pare

      caso "*" :
      escreva("O resultado da multiplcação é: \n", num1 * num2)
      pare

      caso "/" :
      escreva("O resultado da divisão é: \n", num1 / num2)
      pare

      caso contrario :
      escreva("Opção Inválida")
      pare
    }
  }
}
