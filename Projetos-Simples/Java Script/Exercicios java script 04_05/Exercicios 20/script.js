//Vinicius Arcanjo Lobato Montuani N°29 2° DEV B 02/05/25
function dificuldade() {
    const dificuldade = prompt("Qual a dificuldade do jogo? (fácil, médio ou difícil)");
    if (dificuldade === "fácil") {
        document.write("Você escolheu o nível fácil!");
    }
    else if (dificuldade === "médio") {
        document.write("Você escolheu o nível Médio");
    }
    else if (dificuldade === "difícil") {
        document.write("Você escolheu o nível Difícil.");
    }
    else {
        alert("Dificuldade inválida..");
    }
}