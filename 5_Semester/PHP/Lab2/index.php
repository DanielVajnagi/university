<?php   include("layout/header.php");?>
<?php
$action = isset($_GET['action']) ? $_GET['action'] : 'main';


// Перевірка чи сторінка є в списку допустимих та чи файл існує
if (file_exists('views/'.$action.'.php')) {
        include('views/'.$action.'.php'); 
}
else{include('views/main.php');}



?>
<?php   include("layout/footer.php");?>

