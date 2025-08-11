<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    echo "<h1>Bem-vindo, $username!</h1>";
}

?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>bem vindo</title>
</head>

<body>

    <p>Você está logado com sucesso.</p>
    <p>Seja bem vindo lider supremo</p>
    <a href="index.php">Voltar para o login</a>


    <style>
        body {
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
            font-family: 'Segoe UI', Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        h1 {
            color: #333;
            margin-bottom: 1.5rem;
            text-shadow: 0 2px 8px rgba(250, 168, 104, 0.12);
        }

        p {
            background: #fff;
            padding: 1.2rem 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 16px rgba(253, 160, 133, 0.10);
            color: #444;
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }

        a {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.7rem 1.5rem;
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
            color: #fff;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: bold;
            text-decoration: none;
            box-shadow: 0 2px 8px rgba(253, 160, 133, 0.10);
            transition: background 0.2s;
        }

        a:hover {
             background: linear-gradient(90deg, #ACB6E5 0%, #74ebd5 100%);
        }
    </style>


    </style>
</body>

</html>