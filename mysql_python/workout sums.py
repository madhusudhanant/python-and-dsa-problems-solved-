simple queries
1. List full details of all hotels.
mysql> SELECT * FROM hotel;
+----------+-----------------+------------+
| hotel_no | name            | address    |
+----------+-----------------+------------+
| H111     | Grosvenor Hotel | London     |
| H222     | Park Hotel      | London     |
| H333     | Grand Hotel     | Manchester |
| H444     | Royal Hotel     | Birmingham |
| H555     | City Hotel      | London     |
| H666     | Beach Hotel     | Brighton   |
+----------+-----------------+------------+

2. List full details of all hotels in London.

mysql> SELECT * FROM hotel
    -> WHERE address = 'London';
+----------+-----------------+---------+
| hotel_no | name            | address |
+----------+-----------------+---------+
| H111     | Grosvenor Hotel | London  |
| H222     | Park Hotel      | London  |
| H555     | City Hotel      | London  |
+----------+-----------------+---------+

3. List the names and addresses of all guests in
London, alphabetically ordered by name.

mysql> SELECT name, address
    -> FROM guest
    -> WHERE address = 'London'
    -> ORDER BY name ASC;
+---------------+---------+
| name          | address |
+---------------+---------+
| Alice Brown   | London  |
| John Smith    | London  |
| Michael Jones | London  |
| Robert Miller | London  |
| Sophia Moore  | London  |
+---------------+---------+

4. List all double or family rooms with a price
below £40.00 per night, in ascending order of
price.

mysql> SELECT * FROM room
    -> WHERE (type = 'S' OR type = 'D')
    -> AND price < 70.00
    -> ORDER BY price ASC;
+---------+----------+------+-------+
| room_no | hotel_no | type | price |
+---------+----------+------+-------+
| 1       | H222     | S    | 65.00 |
| 2       | H555     | S    | 68.00 |
+---------+----------+------+-------+
2 rows in set (0.00 sec)

5.List the bookings for which no date_to has
been specified.

mysql> SELECT * FROM booking
    -> WHERE date_to IS NULL;
+----------+----------+---------------------+---------+---------+
| hotel_no | guest_no | date_from           | date_to | room_no |
+----------+----------+---------------------+---------+---------+
| H222     | G444     | 2026-08-10 00:00:00 | NULL    | 1       |
+----------+----------+---------------------+---------+---------+
1 row in set (0.00 sec)

Aggregate Functions
1. How many hotels are there?

mysql> SELECT COUNT(*) AS total_hotels
    -> FROM hotel;
+--------------+
| total_hotels |
+--------------+
|            6 |
+--------------+
1 row in set (0.03 sec)

2. What is the average price of a room?
mysql> SELECT ROUND(AVG(price),2) AS avg_price FROM room;
+-----------+
| avg_price |
+-----------+
|     89.51 |
+-----------+
1 row in set (0.02 sec)

3. What is the total revenue per night from
all double rooms?
mysql> SELECT SUM(price) AS Revenue FROM room
    -> WHERE type = "D";
+---------+
| Revenue |
+---------+
|  640.00 |
+---------+

4.How many different guests have made
bookings for August?

mysql> SELECT COUNT(*) FROM booking
    -> WHERE MONTH(date_from) = 08;
+----------+
| COUNT(*) |
+----------+
|        2 |
+----------+

subquerry and join

1. List the price and type of all rooms at the Grosvenor Hotel.
mysql> SELECT r.price, r.type
    -> FROM room r
    -> INNER JOIN hotel h
    -> ON r.hotel_no = h.hotel_no
    -> WHERE h.name = 'Grosvenor Hotel';
+-------+------+
| price | type |
+-------+------+
| 75.60 | s    |
| 85.00 | D    |
| 70.00 | S    |
+-------+------+

2. List all guests currently staying at the Grosvenor Hotel.
mysql> SELECT g.name
    -> FROM guest g
    -> INNER JOIN booking b
    -> ON g.guest_no = b.guest_no
    -> INNER JOIN hotel h
    -> ON h.hotel_no = b.hotel_no
    -> WHERE h.name = 'Grosvenor Hotel'
    -> AND b.date_from <= CURRENT_DATE
    -> AND (b.date_to IS NULL OR b.date_to >= CURRENT_DATE);
+-------------+
| name        |
+-------------+
| Alice Brown |
+-------------+

3.List the details of all rooms at the Grosvenor Hotel,
including the name of the guest staying in the room, if
the room is occupied

Show me every room in Grosvenor Hotel.
For each room, show its room number, type and price.
If someone is currently staying in that room,
also show that person name. If nobody is staying there, show NULL.

mysql> SELECT r.room_no, r.type, r.price, g.name AS guest
    -> FROM hotel h
    -> INNER JOIN room r
    -> ON h.hotel_no = r.hotel_no
    -> LEFT JOIN booking b
    -> ON r.hotel_no = b.hotel_no
    -> AND r.room_no = b.room_no
    -> AND b.date_from <= CURRENT_DATE
    -> AND (b.date_to IS NULL OR b.date_to >= CURRENT_DATE)
    -> LEFT JOIN guest g
    -> ON b.guest_no = g.guest_no
    -> WHERE h.name = 'Grosvenor Hotel';
+---------+------+-------+-------------+
| room_no | type | price | guest       |
+---------+------+-------+-------------+
| 1       | s    | 75.60 | NULL        |
| 2       | D    | 85.00 | Alice Brown |
| 3       | S    | 70.00 | NULL        |
+---------+------+-------+-------------+

4.What is the total income from bookings for the
Grosvenor Hotel today?
mysql> SELECT SUM(r.price) AS tottal_income
    -> FROM room r
    -> INNER JOIN hotel h
    -> ON h.hotel_no = r.hotel_no
    -> INNER JOIN booking b
    -> ON h.hotel_no = b.hotel_no
    -> AND r.room_no = b.room_no
    -> WHERE h.name = 'Grosvenor Hotel'
    -> AND b.date_from <= CURRENT_DATE
    -> AND (b.date_to IS NULL OR b.date_to >= CURRENT_DATE);
+---------------+
| tottal_income |
+---------------+
|         85.00 |
+---------------+

5. List the rooms that are currently unoccupied at the
Grosvenor Hotel.
mysql> SELECT r.room_no
    -> FROM room r
    -> INNER JOIN hotel h
    -> ON r.hotel_no = h.hotel_no
    -> LEFT JOIN booking b
    -> ON r.hotel_no = b.hotel_no
    -> AND r.room_no = b.room_no
    -> AND b.date_from <= CURRENT_DATE
    -> AND (b.date_to IS NULL OR b.date_to >= CURRENT_DATE)
    -> WHERE h.name = 'Grosvenor Hotel'
    -> AND b.room_no IS NULL;
+---------+
| room_no |
+---------+
| 1       |
| 3       |
+---------+

6.What is the lost income from unoccupied rooms at the
Grosvenor Hotel?
mysql> SELECT SUM(r.price) AS lost_income
    -> FROM room r
    -> INNER JOIN hotel h
    -> ON r.hotel_no = h.hotel_no
    -> LEFT JOIN booking b
    -> ON r.hotel_no = b.hotel_no
    -> AND r.room_no = b.room_no
    -> AND b.date_from <= CURRENT_DATE
    -> AND (b.date_to IS NULL OR b.date_to >= CURRENT_DATE)
    -> WHERE h.name = 'Grosvenor Hotel'
    -> AND b.room_no IS NULL;   
+-------------+
| lost_income |
+-------------+
|      145.60 |
+-------------+



GROUPING

1. List the number of rooms in each hotel.
mysql> SELECT hotel_no, COUNT(*) AS Total
    -> FROM room
    -> GROUP BY hotel_no;
+----------+-------+
| hotel_no | Total |
+----------+-------+
| H111     |     3 |
| H222     |     2 |
| H333     |     2 |
| H444     |     2 |
| H555     |     2 |
| H666     |     2 |
+----------+-------+

2. List the number of rooms in each hotel in
London.

mysql> SELECT h.hotel_no, COUNT(*) AS Total_rooms
    -> FROM hotel h
    -> JOIN room r
    -> ON h.hotel_no = r.hotel_no
    -> WHERE h.address = 'London'
    -> GROUP BY h.hotel_no;
+----------+-------------+
| hotel_no | Total_rooms |
+----------+-------------+
| H111     |           3 |
| H222     |           2 |
| H555     |           2 |
+----------+-------------+

3. What is the average number of bookings
for each hotel in August?
mysql> SELECT hotel_no, COUNT(*) AS Total_bookings
    -> FROM booking
    -> WHERE MONTH(date_from) = 8
    -> GROUP BY hotel_no;
+----------+----------------+
| hotel_no | Total_bookings |
+----------+----------------+
| H555     |              1 |
| H222     |              1 |
+----------+----------------+

4. What is the most commonly booked room type for each hotel in London? 
mysql> SELECT h.name, r.type, COUNT(*) AS Most_booked_type
    -> FROM hotel h
    -> INNER JOIN room r
    -> ON h.hotel_no = r.hotel_no
    -> INNER JOIN booking b
    -> ON r.hotel_no = b.hotel_no
    -> AND r.room_no = b.room_no
    -> WHERE h.address = 'London'
    -> GROUP BY h.name, r.type;
+-----------------+------+------------------+
| name            | type | Most_booked_type |
+-----------------+------+------------------+
| Grosvenor Hotel | D    |                2 |
| Park Hotel      | S    |                2 |
| Park Hotel      | D    |                2 |
| City Hotel      | D    |                1 |
| City Hotel      | S    |                1 |
| Grosvenor Hotel | S    |                1 |
+-----------------+------+------------------+

5. What is the lost income from unoccupied
rooms at each hotel today?

mysql> SELECT h.name, SUM(r.price) AS lost_income
    -> FROM room r
    -> INNER JOIN  hotel h
    -> ON r.hotel_no = h.hotel_no
    -> LEFT JOIN booking b
    -> ON r.hotel_no = b.hotel_no
    -> AND r.room_no = b.room_no
    -> AND b.date_from <= CURRENT_DATE
    -> AND (b.date_to IS NULL OR b.date_to >= CURRENT_DATE)
    -> WHERE b.room_no IS NULL
    -> GROUP BY h.name;
+-----------------+-------------+
| name            | lost_income |
+-----------------+-------------+
| Grosvenor Hotel |      145.60 |
| Park Hotel      |       95.00 |
| Grand Hotel     |      190.00 |
| Royal Hotel     |      195.00 |
| City Hotel      |      168.00 |
| Beach Hotel     |      220.00 |
+-----------------+-------------+


























