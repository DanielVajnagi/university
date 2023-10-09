SELECT Clients.Client_ID, Clients.First_Name, Clients.Last_Name, COUNT(Receipts.Receipt_ID) AS OrderCount
FROM Clients
JOIN Receipts ON Clients.Client_ID = Receipts.Client_ID
WHERE Receipts.Date >= '2022-01-01' AND Receipts.Date <= '2023-12-31'
GROUP BY Clients.Client_ID, Clients.First_Name, Clients.Last_Name
HAVING COUNT(Receipts.Receipt_ID) > 4
ORDER BY Clients.Client_ID ASC;
