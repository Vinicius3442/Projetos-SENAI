//Atividade 8 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  funcao inicio() {
    inteiro salario_bruto, salario_liquido, desconto

    escreva("Digite o seu salário BRUTO:\nR$ ")
    leia(salario_bruto)

    desconto = salario_bruto /100

    se(salario_bruto < 2000){
      salario_liquido = salario_bruto - desconto * 10
      escreva("O seu salário líquido é: \nR$ ", salario_liquido)
    }
    senao{
      salario_liquido = salario_bruto - desconto * 20
      escreva("O seu salário líquido é: \nR$ ", salario_liquido)
    }
  }
}
