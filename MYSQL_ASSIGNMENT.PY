Assignment MySQLTable


1: SalesPeopleSnum 
is Primary keySname 
is Unique constraint
Snum Sname City Comm
1001 Peel. London .12
1002 Serres Sanjose .13
1004 Motika London .11
1007 Rifkin Barcelona .15
1003 Axelrod Newyork .10

Syntax:
CREATE TABLE salespeople (
Snum INT PRIMARY KEY,
Sname VARCHAR(30) UNIQUE,
City VARCHAR(30),
Comm INT
);

mysql> select * from salespeople;
+------+---------+-----------+------+
| Snum | Sname   | City      | Comm |
+------+---------+-----------+------+
| 1001 | Peel    | London    |   12 |
| 1002 | Sserress| Sanjose   |   13 |
| 1003 | Axelrod | Newyork   |   10 |
| 1004 | Motika  | London    |   11 |
| 1007 | Rifkin  | Barcelona |   15 |
+------+---------+-----------+------+
5 rows in set (0.00 sec) 

mysql> desc salespeople;

+-------+-------------+------+-----+--------+-------+
| Field | Type        | Null | Key | Default| Extra |
+-------+-------------+------+-----+--------+-------+
| Snum  | int         | N0   | PRI | NULL   |       |
| Sname | varchar(30) | YES  | UNI | NULL   |       |
| City  | varchar(30) | YES  |     | NULL   |       |
| Comm  | int         | YES  |     | NULL   |       |
+-------+-------------+------+-----+--------+-------+
4 rows in set (0.27 sec)


Table 2: Customers
Cnum is Primary Key
City has not null constraint.
Snum is foreign key constraint refers Snum column
of SalesPeople table.
Cnum Cname City Snum
2001 Hoffman London 1001
2002 Giovanni Rome 1003
2003 Liu Sanjose 1002
2004 Grass Berlin 1002
2006 Clemens London 1001
2008 Cisneros Sanjose 1007
2007 Pereira Rome 1004

Syntax:
Create Table Customers(Cnum INT PRIMAY KEY,
Cname VARCHAR(30),
City VARCHAR(30) NOT NULL,
Snum INT,
FOREIGN KEY (Snum) REFERENCES Salespeople(Snum) 
);

mysql> desc customers;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| Cnum  | int         | N0   | PRI | NULL    |       | 
| Cname | varchar(30) | YES  |     | NULL    |       |
| City  | varchar(30) | NO   |     | NULL    |       |
| Snum  | int         | YES  | MUL | NULL    |       | 
+-------+-------------+------+-----+---------+-------+
rows in set (0.10 sec)

mysql> select * from customers;
+------+----------+---------+------+
| Cnum | Cname    | City    | Snum |
+------+----------+---------+------+
| 2001 | Hoffman  | London  | 1001 |
| 2002 | Giovanni | Rome    | 1003 |
| 2003 | Liu      | Sanjose | 1002 |
| 2004 | Grass    | Berlin  | 1002 | 
| 2006 | Clemens  | London  | 1001 | 
| 2007 | Pereira  | Rome    | 1004 |
| 2008 | Cisneros | Sanjose | 1007 |
+------+----------+---------+------+
rows in set (0.12 sec)


Table 3: Orders

Onum is Primary key
Cnum is foreign key refers to Cnum column of 
Customers table. Snum is foreign key refers Snum
column of SalesPeople table.
Onum Amt Odate Cnum Snum
3001 18.69 3-10-1990 2008 1007
3003 767.19 3-10-1990 2001 1001
3002 1900.10 3-10-1990 2007 1004
3005 5160.45 3-10-1990 2003 1002
3006 1098.16 3-10-1990 2008 1007
3009 1713.23 4-10-1990 2002 1003
3007 75.75 4-10-1990 2004 1002
3008 4273.00 5-10-1990 2006 1001
3010 1309.95 6-10-1990 2004 1002
3011 9891.88 6-10-1990 2006 1001


Syntax:CREATE TABLE orders (
Onum INT PRIMARY KEY,
Amt decimal(ff,2),
Odate VARCHAR(10) NOT NULL,
Cnum INT NOT NULL,
Snum INT NOT NULL,
    FOREIGN KEY (Cnum) REFERENCES 
Customers(Cnum),      
    FOREIGN KEY (Snum) REFERENCES 
Salespeople(Snum)
);

mysql> desc orders;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| Onum  | int          | NO   | PRI | NULL    |       |
| Amt   | decimal(6,2) | YES  |     | NULL    |       |
| Odate | varchar(10)  | NO   |     | NULL    |       | 
| Cnum  | int          | NO   | MUL | NULL    |       |
| Snum  | int          | NO   | MUL | NULL    |       | 
+-------+--------------+------+-----+---------+-------+

mysql> select * from orders;
+------+---------+-----------+------+------+
| Onum | Amt     |Odate     | Cnum  | Snum |
| 3001 |   18.69 | 3-10-1990| 2008  | 1007 |
| 3002 | 1900.10 | 3-10-1990| 2007  | 1004 |
| 3003 |  767.19 | 3-10-1990| 2001  | 1001 |
| 3005 | 5160.45 | 3-10-1990| 2003  | 1002 |
| 3006 | 1098.16 | 3-10-1990| 2008  | 1007 |
| 3007 |  75.75  | 4-10-1990| 2004  | 1002 |
| 3008 | 4273.00 | 5-10-1990| 2006  | 1001 | 
| 3009 | 1713.23 | 4-10-1990| 2002  | 1003 |
| 3010 | 1309.95 | 6-10-1990| 2004  | 1002 |
| 3011 | 9891.88 | 6-10-1990| 2006  | 1001 |
+------+---------+----------+-------+------+
10 rows in set (0.00 sec)

On the basis of above tables specific tasks has been 
performed according to the questions:


1) count the number of salesperson whose name begin
with 'a'/'A'

mysql> select count(*) from SalesPeople where Sname like 'a%' or Sname lika 'A%'
+----------+
| count(*) |
+----------+
|        1 |
+----------+
1 row in set (0.44 sec)


2) Display all the SalesPerson whose all the orders worth is more than Rs 2000

mysql> select SalesPerson.Sname from SalesPerson inner join orders on SalesPerson. Snum=orders.Snum;
+---------+
| Sname   |
+---------+
| axelrod |
| Motika  |
| Peel    |
| Peel    |
| Peel    |
| Rifkin  |
| Rifkin  |
| Sserres |
| Sserres |
| Sserres |
+---------+
10 rows in set (0.00 sec)


3) count the number of salesperson belonging to Newyork.

mysql> select Sname from SalesPerson where City= 'Newyork';
+---------+
| Sname   |
+---------+
| Axelrod |
+---------+
1 row in set (0.00 sec)

4) Display the number of salesperson belonging to london and belonging to paris.

mysql> select count(Sname) from SalesPerson where City= 'London' and City= 'paris';
+--------------+
| count(Sname) |
+--------------+
|            0 |
+--------------+
1 row in set(0.00 sec)

5) Display the number of orders taken by each Salesperson and their date of orders.

mysql> SELECT Odate,Snum,COUNT(*)
    -> FROM orders
    -> GROUP BY Odate,Snum;
+-----------+------+----------+
| Odate     | Snum | COUNT(*) |
+-----------+------+----------+
| 3-10-1990 | 1007 |       2  |
| 3-10-1990 | 1004 |       1  |
| 3-10-1990 | 1001 |       1  |
| 3-10-1990 | 1002 |       1  |
| 4-10-1990 | 1002 |       1  |
| 5-10-1990 | 1001 |       1  |
| 4-10-1990 | 1003 |       1  | 
| 6-10-1990 | 1002 |       1  |
| 6-10-1990 | 1001 |       1  |
+-----------+------+----------+
9 rows in set (0.03 sec)
