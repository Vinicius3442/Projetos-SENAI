<?php 
$host = 'localhost';
$username = 'root';
$password = '';
$database = 'transportadora';

$con = new mysqli($host,  $username,  $password,$database);

if ($con->connect_error){
    die("Conexão falhou:   $con->connect_error");
}
?>