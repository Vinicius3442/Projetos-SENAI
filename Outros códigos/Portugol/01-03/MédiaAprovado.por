//Atividade 4 Vinicius Arcanjo Lobato Montuani N°29 2°DEV B
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
    real nota1, nota2, media, media_arredondada
    

    escreva("Digite a primeira nota:\n")
    leia(nota1)
    
    escreva("Digite a segunda nota:\n")
    leia(nota2)

    media =(nota1 + nota2) /2

    media_arredondada = mat.arredondar(media,1)

    se(media >= 7){
      escreva("Sua média foi: ", media_arredondada,"\n Você foi APROVADO")
    }   
    senao{
      escreva("Sua média foi: ", media_arredondada,"\n Você foi REPROVADO")
    }
  }
}
