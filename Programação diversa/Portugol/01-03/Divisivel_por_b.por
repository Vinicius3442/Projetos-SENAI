//Atividade 13 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  funcao inicio() {
    inteiro num_a, num_b

    escreva("Digite o primeiro número inteiro:\n")
    leia(num_a)
    
    escreva("Digite o segundo número inteiro:\n")
    leia(num_b)

    se(num_a % num_b == 0){
      escreva("O numero ", num_a, " é divisivel por ", num_b)
    }
    senao{
      escreva("O numero ", num_a, " não é divisivel por ", num_b)
    }
  }
}
