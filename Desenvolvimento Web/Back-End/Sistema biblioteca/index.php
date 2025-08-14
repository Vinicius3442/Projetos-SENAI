<?php
include "conection.php";

// Função de cadastrar

if (isset($_POST["acao"]) && $_POST["acao"] == "cadastrar") {
    $titulo = $_POST["titulo"];
    $autor = $_POST["autor"];
    $ano = $_POST["ano"];
    $prateleira = $_POST["prateleira"];

    $conexao->query("INSERT INTO livros (titulo, autor, ano, prateleira) 
    VALUES ('$titulo', '$autor', '$ano', '$prateleira')");
    echo "<p style='color:green;'>Livro cadastrado com sucesso!</p>";
}

// função de editar

if (isset($_POST["acao"]) && $_POST["acao"] == "editar") {
    $id = $_POST["id"];
    $titulo = $_POST["titulo"];
    $autor = $_POST["autor"];
    $ano = $_POST["ano"];
    $prateleira = $_POST["prateleira"];

    $conexao->query("UPDATE livros 
                     SET titulo='$titulo', autor='$autor', ano='$ano', prateleira='$prateleira' WHERE id=$id");
    echo "<p style='color:blue;'>Livro atualizado com sucesso!</p>";
}

// Função de excluir

if (isset($_GET["excluir"])) {
    $id = $_GET["excluir"];
    $conexao->query("DELETE FROM livros WHERE id=$id");
    echo "<p style='color:red;'>Livro excluído com sucesso!</p>";
}
?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <title>Biblioteca Escolar</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1 class="center">Sistema da Biblioteca <strong id="SESI">SESI</strong></h1>
    <p class="center"><strong>Seja Bem-vindo!</strong> Cadastre, edite ou exclua livros do acervo.</p>
    <img class="center" src="./Livros.jpg" alt="Imagem do Livro">


    <!-- Forms de cadastro -->

    <h2>Cadastrar Novo Livro</h2>
    <form method="POST">
        <input type="hidden" name="acao" value="cadastrar">
        <label>Título:</label><br>
        <input type="text" name="titulo" required><br>
        <label>Autor:</label><br>
        <input type="text" name="autor" required><br>
        <label>Ano:</label><br>
        <input type="number" name="ano" max="2025" required><br>
        <label>Prateleira:</label><br>
        <input type="text" name="prateleira" required><br><br>
        <input type="submit" value="Cadastrar">
    </form>

    <hr>

    <!-- Lista de livros do banco de dados -->

    <h2>Livros já cadastrados</h2>
    <p>Caso precise remover algum livro, clique em "Excluir", e caso precise editar, clique em "Editar".</p>

    <table>
        <tr>
            <th>Id</th>
            <th>Título</th>
            <th>Autor</th>
            <th>Ano</th>
            <th>Prateleira</th>
            <th>Ações</th>
        </tr>
        <?php
        $result = $conexao->query("SELECT * FROM livros");
        while ($livro = $result->fetch_assoc()) {
            echo "<tr>
                <td>{$livro['id']}</td>
                <td>{$livro['titulo']}</td>
                <td>{$livro['autor']}</td>
                <td>{$livro['ano']}</td>
                <td>{$livro['prateleira']}</td>
                <td>
                    <a href='?editar={$livro['id']}'>Editar</a> | 
                    <a href='?excluir={$livro['id']}' onclick='return confirm(\"Tem certeza que quer excluir o livro? A ação é irreversível\")'>Excluir</a>
                </td>
              </tr>";
        }
        ?>
    </table>

    <!-- forms de edit -->

    <?php
    if (isset($_GET['editar'])) {
        $id = $_GET['editar'];
        $livro = $conexao->query("SELECT * FROM livros WHERE id=$id")->fetch_assoc();
        ?>
        <hr>
        <h2>Atualizar as informações</h2>
        <form method="POST">
            <input type="hidden" name="acao" value="editar">
            <input type="hidden" name="id" value="<?php echo $livro['id']; ?>">
            <label>Título:</label><br>
            <input type="text" name="titulo" value="<?php echo $livro['titulo']; ?>" required><br>
            <label>Autor:</label><br>
            <input type="text" name="autor" value="<?php echo $livro['autor']; ?>" required><br>
            <label>Ano:</label><br>
            <input type="number" name="ano" value="<?php echo $livro['ano']; ?>" required><br>
            <label>Prateleira:</label><br>
            <input type="text" name="prateleira" value="<?php echo $livro['prateleira']; ?>" required><br><br>
            <input type="submit" value="Salvar Alterações">
        </form>
        <?php
    }
    ?>
</body>

</html>