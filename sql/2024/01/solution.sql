DROP TABLE IF EXISTS #Data;
CREATE TABLE #Data (
   L varchar(max)
  ,R varchar(max)
);

BULK INSERT #Data
FROM '$PATH\input.txt'
WITH
(
	ROWTERMINATOR = '0x0A',
  FIELDTERMINATOR = ' ',
	FIRSTROW = 1
)
GO

WITH Ints AS 
(
  SELECT
     CONVERT(int, L) AS L
    ,CONVERT(int, R) AS R
    ,ROW_NUMBER() OVER(ORDER BY CONVERT(int, L) ASC) AS RN_L
    ,ROW_NUMBER() OVER(ORDER BY CONVERT(int, R) ASC) AS RN_R
  FROM #Data
),
Part1 AS 
(
  SELECT 
     SUM(ABS(l.L - r.R)) AS Answer
  FROM Ints l
  LEFT JOIN Ints r ON r.RN_R = l.RN_L
), Counts AS
(
  SELECT 
     src.L
    ,COUNT(cnt.R) AS Antal 
  FROM Ints src
  LEFT JOIN Ints cnt ON cnt.R = src.L
  GROUP BY src.L
), Part2 AS
(
  SELECT
     SUM(L * Antal) AS Answer
  FROM Counts
)
SELECT 1 AS Part, Answer
FROM Part1
UNION ALL
SELECT 2 AS Part, Answer
FROM Part2;