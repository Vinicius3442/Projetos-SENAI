//Atividade 9 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  funcao inicio() {
    real valor_inc, valor_fin, desconto

    escreva("Digite o valor da compra:\nR$ ")
    leia(valor_inc)


    se(valor_inc < 200){
      desconto = valor_inc /100
      valor_fin = valor_inc + desconto * 50
      escreva("O valor de venda é: \nR$ ", valor_fin)
    }
    senao{
      desconto = valor_inc /100
      valor_fin = valor_inc + desconto * 30
      escreva("O valor de venda é: \nR$ ", valor_fin)
  }
  }
}
