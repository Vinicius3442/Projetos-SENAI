<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora PHP</title>
</head>
<body>
    <h1>Calculadora em PHP</h1>
    <p>Primeiros passo com requisição post</p>
    <form method="POST" action="formscalculo.php">
        <label for="num1">Digite o primeiro número:</label>
        <input type="number" name="num1" required>
        
        <select name="operacao" required>
            <option value="soma">Soma</option>
            <option value="subtracao">Subtração</option>
            <option value="multiplicacao">Multiplicação</option>
            <option value="divisao">Divisão</option>
        </select>

        <label for="num2">Digite o segundo número:</label>
        <input type="number" name="num2" required>

        <button type="submit">Calcular</button>
    </form>

</body>
</html>

