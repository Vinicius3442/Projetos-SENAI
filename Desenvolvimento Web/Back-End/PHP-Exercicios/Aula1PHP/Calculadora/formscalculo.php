<?php 

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $num1 = $_POST["num1"];
    $num2 = $_POST["num2"];
    $operacao = $_POST["operacao"];

    switch ($operacao) {
        case 'soma':
            $resultado = $num1 + $num2;
            break;
        case 'subtracao':
            $resultado = $num1 - $num2;
            break;
        case 'multiplicacao':
            $resultado = $num1 * $num2;
            break;
        case 'divisao':
            if ($num2 == 0) {
                $resultado = "Erro: Divisão por zero.";
            } else {
                $resultado = $num1 / $num2;
            }
            break;
        default:
            $resultado = "Operação inválida.";
            break;
    }

    echo "<p>Resultado: $resultado</p>";
} else {
    echo "<h1>Método de requisição inválido.</h1>";
}


?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado da calculadora</title>
</head>
<body>
    <a href="./index.php">Voltar</a>
</body>
</html>