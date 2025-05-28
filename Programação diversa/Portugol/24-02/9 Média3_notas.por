//Atividade 9 Vinicius Montuani
programa{
  inclua biblioteca Matematica-->mat
  funcao inicio() {
    real nota1, nota2, nota3, media, media_arredondada

    escreva("Digite as notas abaixo:\n")
    escreva("Digite a primeira nota: ")
    leia(nota1)
    escreva("Digite a segunda nota: ")
    leia(nota2)
    escreva("Digite a terceira nota: ")
    leia(nota3)

    media = (nota1 + nota2 + nota3) / 3

    media_arredondada = mat.arredondar(media,1) //Aprendi a limitar as casas decimais vendo este vídeo: https://youtu.be/Jjo0PvauNJg?si=YUgKEyHtZTnFh02x
     escreva("Sua média final é: ", media_arredondada) 
  }
  }
