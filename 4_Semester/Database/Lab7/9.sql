SELECT Clients.Client_ID, Clients.First_Name, Clients.Last_Name, COUNT(Receipts.Receipt_ID) AS OrderCount
FROM Clients
JOIN Receipts ON Clients.Client_ID = Receipts.Client_ID
GROUP BY Clients.Client_ID, Clients.First_Name, Clients.Last_Name
ORDER BY Clients.Client_ID ASC;
