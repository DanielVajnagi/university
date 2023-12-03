<!DOCTYPE html>
<?php
session_start();
?>
<html>
<head>
    <meta charset="utf-8" />
    <title>Головна</title>
    <link rel="stylesheet" href="css/style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
<header>
    <nav> 
    <img src="img/f1_logo_white.png" id="f1_logo">
    <a href="?action=">Main</a>
    <a href="?action=news">News</a>
    <a href="?action=survey">Survey</a>
    <a href="?action=calendar">Calendar</a>
    <a href="?action=standings">Standings</a>
    <a href="?action=drivers">Drivers</a>
    <?php
    // Перевірка чи користувач авторизований
    if (isset($_SESSION['user_id'])) {
        echo '<a href="?action=logout">Logout </a>';
    } else {
        echo '<a href="?action=login">Login </a>';
        echo '<a href="?action=signup">Sign up</a>';
    }
    ?>
    
    
    </nav>
</header>