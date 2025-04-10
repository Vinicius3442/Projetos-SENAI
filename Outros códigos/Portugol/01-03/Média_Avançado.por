//Atividade 10 Vinicius Montuani
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real nota1, nota2, media, media_arredondada
    cadeia resultado

    escreva("Digite a primeira nota: ")
    leia(nota1)

    escreva("Digite a segunda nota: ")
    leia(nota2)

    media = (nota1 + nota2) /2

    media_arredondada = mat.arredondar(media,1)
    
    se(media >= 7){
      resultado = "Aprovado"
      escreva("Sua média final foi: ", media_arredondada, " você foi: ", resultado)
    }

    senao se(media > 3 e media < 7){
      resultado = "Prova final"
      escreva("Sua média final foi: ", media_arredondada, " você foi para a ", resultado)
    }

    senao{
      resultado = "Reprovado"
      escreva("Sua média final foi: ", media_arredondada, " você foi:  ", resultado)
    }
    }
  }

