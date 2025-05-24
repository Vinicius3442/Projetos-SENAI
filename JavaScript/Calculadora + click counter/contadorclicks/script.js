// contadorclicks/contador.js
document.addEventListener('DOMContentLoaded', () => {
  // Elementos
  const display = document.getElementById('display');
  const botaoClique = document.getElementById('botao-clique');
  const botaoReset = document.getElementById('botao-reset');
  let contador = 0;

  // Contador principal
  botaoClique.addEventListener('click', () => {
    contador++;
    display.textContent = contador;
    
    
    // Feedback tátil no botão
    botaoClique.style.transform = 'scale(0.95)';
    setTimeout(() => {
      botaoClique.style.transform = 'scale(1)';
    }, 100);
  });

  // Reset
  botaoReset.addEventListener('click', () => {
    contador = 0;
    display.textContent = contador;
    
    // Efeito especial de reset
    display.style.color = 'var(--amarelo-primario)';
    setTimeout(() => {
      display.style.color = 'var(--azul-primario)';
    }, 500);
  });

  // Inicialização
  display.style.opacity = '0';
});

