<?php 

$temperatura_f = 95;

$temperatura_c = ($temperatura_f - 32) * 5 / 9;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de temperatura</title>
</head>
<h1>Conversor de temperatura:</h1>
<p>
    <?php echo "Temperatura em Fahrenheit: $temperatura_f;"?>°F<br>
    <?php echo "Temperatura em Celsius:  $temperatura_c;" ?>°C
</p>
<body>
    
</body>
</html>