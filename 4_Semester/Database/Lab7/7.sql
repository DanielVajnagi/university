SELECT Worker_ID, First_Name, Last_Name, TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) AS Age
FROM Workers;
