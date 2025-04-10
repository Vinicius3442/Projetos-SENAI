//Atividade 3 Vinicius Arcanjo Lobato Montuani N 29 2 DEV B
programa {
  inclua biblioteca Util
  funcao inicio() {
    inteiro contagem_regr
    escreva("Insira um numero inteiro: ")
    leia(contagem_regr)
    enquanto(contagem_regr > -1)
    {
      escreva("Contagem regressiva: ", contagem_regr, "\n")
      contagem_regr = contagem_regr - 1
      Util.aguarde(1000)
    }
    limpa()
    escreva("fim da contagem :) ")

  }
}
