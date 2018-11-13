Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+


solution1:
select distinct p1.Id as Id from Weather, Weather p2  where p1.Temperature > p2.Temperature 
and To_days(p1.RecordDate) = To_days(p2.RecordDate) + 1


solution2:
select p1.Id as Id from weather p1 join weather p2 on To_days(p1.RecordDate) = To_days(p2.RecordDate) + 1 where 
p1.Temperature > p2.Temperature 
