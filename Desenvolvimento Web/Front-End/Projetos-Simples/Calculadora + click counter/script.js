
document.getElementById("botao").addEventListener("click", calcularViagem);

function calcularViagem() {
  const numPessoas = parseInt(document.getElementById("pessoas").value);
  const custoPassagem = parseFloat(document.getElementById("custo").value);

  if (isNaN(numPessoas) || isNaN(custoPassagem) || numPessoas <= 0 || custoPassagem <= 0) {
    Swal.fire({
      icon: "error",
      title: "Erro!",
      text: "Por favor, insira valores válidos para o número de pessoas e o custo da passagem.",
    });
    return;
  }

  const custoTotal = numPessoas * custoPassagem;

  Swal.fire({
    icon: "success",
    title: "Custo Total da Viagem",
    text: `O custo total da viagem para ${numPessoas} pessoas é de R$ ${custoTotal.toFixed(2)}`,
  });
}
