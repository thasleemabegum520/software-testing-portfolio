-- Retrieve all the rows and columns
SELECT * FROM ORDERS;

--Retrieve order id and product name column from table orders
SELECT ORDER_ID,PRODUCT_NAME FROM ORDERS;

--Retrieve data of orders who purchased laptop
SELECT * FROM ORDERS
WHERE PRODUCT_NAME="LAPTOP";

--Retrieve product name and no of orders to that product
SELECT PRODUCT_NAME,COUNT(*) FROM ORDERS GROUPBY PRODUCT_NAME;

