//Atividade 4 Vinicius Montuani
programa {
  inclua biblioteca Util --> u

  funcao inicio() {
    inteiro numero_aleatorio, entrada

    numero_aleatorio = u.sorteia(0, 100) //https://youtu.be/Co-oTgSPvAA?si=SOwSk2wDmA9d2z8O aprendi a fazer o sorteio com esse vídeo

    escreva("Vamos brincar de adivinhação!\nEscolha um número entre 0 e 100: ")

    enquanto (numero_aleatorio != entrada) {
      leia(entrada)

      se (entrada < numero_aleatorio) {
        escreva("Maior! \nTente novamente: ")
      }
      se (entrada > numero_aleatorio) {
        escreva("Menor! \nTente novamente: ")
      }
      se (entrada == numero_aleatorio) {
        escreva("Muito bem, você acertou, o número correto é: ", numero_aleatorio)
      }
    }
  }
}
