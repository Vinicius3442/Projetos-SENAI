//Atividade 16 - Vinicius Montuani
programa {
  inclua biblioteca Matematica --> mat
  funcao inicio() {
     cadeia municipio, sim_nao
     real votos, seg_turno1, seg_turno2, eleitores

     escreva("Digite o nome do municipio:\n")
     leia(municipio)

     escreva("Digite o número de eleitores:\n")
     leia(eleitores)

     escreva("Digite o número de votos do candidato mais votado: \n")
     leia(votos)

     seg_turno1 = (votos / eleitores ) * 100
     seg_turno2 = mat.arredondar(seg_turno1,2)
     se(eleitores > 200000 e seg_turno2 < 50){
      limpa()
      sim_nao = "Sim"
      escreva("Municipio: ", municipio, "\nNúmero de eleitores: ",eleitores, "\nNúmero de votos do candidato mais votado: ", votos, "\n% de votos: ",seg_turno2, "%", "\n2° Turno: ", sim_nao)
     }
     senao{
      limpa()
      sim_nao = "Não"
      escreva("Municipio:", municipio, "\nNúmero de eleitores: ",eleitores, "\n Número de votos do candidato mais votado: ", votos, "\n % de votos: ",seg_turno2, "%","\n 2° Turno: ", sim_nao)
     }
  }
}
