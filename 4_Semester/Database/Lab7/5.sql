SELECT Items.Item_ID, Items.Item_Name, Receipts_Items.Amount
FROM Items
JOIN Receipts_Items ON Items.Item_ID = Receipts_Items.Item_ID
JOIN Receipts ON Receipts_Items.Receipt_ID = Receipts.Receipt_ID
JOIN Clients ON Receipts.Client_ID = Clients.Client_ID
WHERE Clients.Client_ID = 1;
