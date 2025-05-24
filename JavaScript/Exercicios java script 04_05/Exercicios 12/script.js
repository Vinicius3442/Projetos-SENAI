//Vinicius Arcanjo Lobato Montuani N°29 2° DEV B 02/05/25
const menu = prompt("Escolha uma opção:\n\n1 \n\n2 \n\n3");
switch (menu) {
    case "1":
        alert("Você escolheu pizza! Confira nosso cardápio.");
        break;
    case "2":
        alert("Você escolheu hambúrguer! Delícia!");
        break;
    case "3":
        alert("Você escolheu sushi! Que tal um combinado?");
        break;
    default:
        alert("Opção inválida!");
}