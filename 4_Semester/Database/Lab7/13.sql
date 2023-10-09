SELECT Clients.Client_ID, Clients.First_Name, Clients.Last_Name
FROM Clients
WHERE Clients.Client_ID IN (
    SELECT Receipts.Client_ID
    FROM Receipts
    WHERE Receipts.Date >= '2022-01-01' AND Receipts.Date <= '2022-12-31'
);
