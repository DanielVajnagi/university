SELECT Workers.First_Name, Workers.Last_Name, Positions.Position_Name
FROM Workers
JOIN Positions ON Workers.Position = Positions.Position_ID;
