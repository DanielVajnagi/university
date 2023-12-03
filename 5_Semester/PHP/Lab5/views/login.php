<?php

// Перевірка, чи дані введені
if (isset($_POST['username']) && isset($_POST['password'])) {

	$mysqli = new mysqli("localhost", "root", "", "f1site");

	// Перевірка з'єднання
	if ($mysqli->connect_error !=0) {
		die("connection failed: " . $mysqli->connect_error);
	}


    $username = $_POST['username'];
    $password = $_POST['password'];

    // Отримання хешу пароля з бази даних за логіном
    $stmt = $mysqli->prepare("SELECT id, password, role FROM users WHERE login = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->bind_result($user_id, $hashed_password, $role);
    $stmt->fetch();
    $stmt->close();

    // Перевірка чи є користувач та чи співпадає хеш пароля
    if ($user_id && password_verify($password, $hashed_password)) {
        // Якщо вірно, записати дані в сесію
        $_SESSION['user_id'] = $user_id;
        $_SESSION['username'] = $username;
        $_SESSION['role'] = $role;

        // Перенаправити на головну сторінку або вивести посилання
        header("Location: ?action=news");
    } else {
        
        echo "Invalid username or password. Please try again.";
    }

    // Закриття з'єднання
    $mysqli->close();
} else {
    echo "Please enter username and password.";
}
?>







	<h2>Login</h2>
	<form action="?action=login" method="post">
	<label for="username">Username:</label><br>
	<input type="text" name="username"required><br>
	<label for="password">Pasword:</label><br>
	<input type="password" name="password"required><br>
    <input type="submit" value="Login">
	</form>
