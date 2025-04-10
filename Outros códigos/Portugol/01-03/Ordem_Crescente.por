//Atividade 15 - Vinicius Montuani
programa {
  inclua  biblioteca Matematica --> mat
  funcao inicio() {
    real num1, num2, num3, maior1, maior2, menor1, menor2

    escreva("Digite o primeiro número: ")
    leia(num1)

    escreva("Digite o segundo número: ")
    leia(num2)

    escreva("Digite o terceiro número: ")
    leia(num3)

    maior1 = mat.maior_numero(num1, num2)
    maior2 = mat.maior_numero(maior1, num3)

    menor1 = mat.menor_numero(num1, num2)
    menor2 = mat.menor_numero(maior2, num3)

    //Caso sejam números diferentes
    se(maior2 != num1 e menor2 != num1){
      escreva("Os numeros são: \n", maior2,"\n", num1,"\n", menor2)
    }

    senao se(maior2 != num2 e menor2 != num2){
      escreva("Os numeros são: \n", maior2,"\n", num2,"\n", menor2)
    }

    senao se(maior2 != num3 e menor2!= num3){
      escreva("Os numeros são: \n", maior2,"\n", num3,"\n", menor2)
    }

    //Caso sejam números iguais
    senao se(num1 == num2 e num1 == num3){
      escreva("Os numeros são: \n", num1,"\n", num2,"\n", num3)
    }

    senao se(num1 == num2 e num1 > num3){
      escreva(" Os numeros são: \n", num1,"\n", num2,"\n", num3)
    }
    senao se(num1 == num3 e num1 > num2){
      escreva("Os numeros são: \n", num1,"\n", num3,"\n", num2)
    }

    senao se(num1 == num2 e num1 < num3){
      escreva("Os numeros são: \n", num3,"\n", num1,"\n", num2)
    }
    senao se(num1 == num3 e num1 < num2){
      escreva("Os numeros são: \n", num2,"\n", num1,"\n", num3)
    }

    senao se(num2 == num3 e num2 > num1){
      escreva("Os numeros são: \n", num2,"\n", num3,"\n", num1)
    }
    senao{
     escreva("Os numeros são: \n", num1,"\n", num2,"\n", num3)
    }
  }
}
