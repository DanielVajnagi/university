<?php
session_start();

// Видалення всіх даних сесії
session_unset();
session_destroy();

header("Location: ?action=main");
?>
