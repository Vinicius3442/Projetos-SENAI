//Atividade 10 Vinicius Montuani
programa {
  funcao inicio() {
    cadeia estacao, entrada

    escreva("Em qual mês do ano estamos?\n")
    escreva("- Janeiro\n- Fevereiro\n- Março\n- Abril\n- Maio\n- Junho\n- Julho\n- Agosto\n- Setembro\n- Outubro\n- Novembro\n- Dezembro\n")
    leia(entrada)
    
    escolha(entrada) {
      caso "Dezembro":
      caso "Janeiro":
      caso "Fevereiro":
      estacao = "Verão"
      escreva("Estamos na estação: ", estacao)
      pare

      caso "Março" :
      caso "Abril":
      caso "Maio":
      estacao = "Outono"
      escreva("Estamos na estação: ", estacao)
      pare

      caso "Junho":
      caso "Julho":
      caso "Agosto":
      estacao = "Inverno"
      escreva("Estamos na estação: ", estacao)
      pare
      
      caso "Setembro":
      caso "Outubro":
      caso "Novembro":
      estacao = "Primavera"
      escreva("Estamos na estação: ", estacao)
      pare
      caso contrario :
      escreva("Digite um mês válido !")//Para as estações eu usei o https://meteorologia.incaper.es.gov.br/estacoes-do-ano#:~:text=O%20inverno%20meteorológico%20começa%20em,começa%20em%201º%20de%20dezembro. como fonte
      pare
    }
    
  }
}
