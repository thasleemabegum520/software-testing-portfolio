-- Retrieve all the rows and columns
SELECT * FROM ORDERS;

--Retrieve order id and product name column from table orders
SELECT ORDER_ID, PRODUCT_NAME
FROM ORDERS;

--Retrieve data of orders who purchased laptop
SELECT * FROM ORDERS
WHERE PRODUCT_NAME='LAPTOP';

--Retrieve product name and no of orders to that product
SELECT PRODUCT_NAME, COUNT(*)
FROM ORDERS
GROUP BY PRODUCT_NAME;

--Retrieve customer names,orderid  who purchased laptops
SELECT C.CUSTOMER_NAME, C.ORDER_ID
FROM ORDERS S INNER JOIN CUSTOMERS C
ON S.ORDER_ID=C.ORDER_ID;

--Retrieve product name and no of sales of that product with price more than 1000
SELECT PRODUCT_NAME,COUNT(*) FROM ORDERS GROUP BY PRODUCT_NAME HAVING PRICE>1000;