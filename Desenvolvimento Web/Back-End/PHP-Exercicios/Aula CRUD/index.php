<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD PHP</title>
</head>

<body>
    <h1>CRUD PHP</h1>

    <?php
    include './config.php';

    $SQL = "SELECT DISTINCT * FROM cliente ORDER BY idCliente ASC";
    $result = $con->query($SQL);

    if ($result->num_rows > 0) {
        echo "<table>";
        echo "<thead>";
        echo "<tr>";
        echo "<th>ID clientes</th>";
        echo "<th>Nome clientes</th>";
        echo "<th>Email clientes</th>";
        echo "</tr>";
        echo "</thead>";
        echo "<tbody>";

        while ($row = $result->fetch_assoc()) {
            echo '<tr>';
            echo '<td>' . $row['idCliente'] . '</td>';
            echo '<td>' . $row['nome'] . '</td>';
            echo '<td>' . $row['email'] . '</td>';
        }
        echo "</tbody>";
        echo '</table>';
    } else {
        echo "<h3>Nenhum cliente encontrado.</h3>";
    }
    ?>

    <style>
        body {
            margin: 20px;
        }

        h1 {
            color: #333;
            text-align: center;
        }

        table {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</body>

</html>