SELECT Workers.Worker_ID, Workers.First_Name, Workers.Last_Name
FROM Workers
WHERE Workers.Position IN (
    SELECT Position_ID
    FROM Positions
    WHERE Positions.Salary > (
        SELECT AVG(Salary)
        FROM Positions
    )
);
