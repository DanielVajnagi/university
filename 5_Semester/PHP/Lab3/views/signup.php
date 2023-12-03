
<?php


if ($action === 'signup' && $_SERVER['REQUEST_METHOD'] === 'POST') {
    $login = $_POST['login'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $password = $_POST['password'];
    $repeatPassword = $_POST['repeat_password'];
    $username = $_POST['username'];

    $errors = [];

    // Перевірка логіна
    if (!preg_match('/^[a-zA-Zа-яА-Я0-9_-]{4,}$/', $login)) {
        $errors[] = "Некоректний логін.";
    }

    // Перевірка пароля
    if (!preg_match('/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{7,}$/', $password)) {
        $errors[] = "Некоректний пароль.";
    }

    // Перевірка повторення пароля
    if ($password !== $repeatPassword) {
        $errors[] = "Повторний пароль не співпадає з паролем.";
    }

    // Перевірка електронної пошти
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Некоректна електронна пошта.";
    }

    //перевірка пароля
	$phonePattern = '/^(\+\d{1,3}\s?)?(\(\d{1,5}\)\s?)?(\d{1,5}[\s\-\)]?)+$/';

	if (!empty($phone) && strlen($phone) > 30) {
		$errors[] = "Телефон не повинен перевищувати 30 символів.";
	} elseif (!empty($phone) && !preg_match($phonePattern, $phone)) {
		$errors[] = "Некоректний формат телефону.";
	}

    if (!empty($errors)) {
        echo "<div style='color: red;'>";
        foreach ($errors as $error) {
            echo "<p>{$error}</p>";
        }
        echo "</div>";
    } else {
        header('Location: ?action=signup_success');
    }
}
?>
<h2>Sign Up!</h2>
<form method="post" action="index.php?action=signup">
    <label for="login">Login:</label><br>
    <input type="text" name="login" required><br>

    <label for="email">Email:</label><br>
    <input type="text" name="email" required><br>

    <label for="phone">Phone:</label><br>
    <input type="text" name="phone"><br>

    <label for="password">Password:</label><br>
    <input type="password" name="password" size="30" required><br>

    <label for="repeat_password">Repeat Password:</label><br>
    <input type="password" name="repeat_password" size="30" required><br>

    <input type="submit" value="Sign up!">
</form>
