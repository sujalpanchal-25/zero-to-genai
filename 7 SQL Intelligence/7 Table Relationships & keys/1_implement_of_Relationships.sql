create table customers(
 customer_id serial primary key,
 first_name varchar(50) not null,
 last_name  varchar(50) not null,
 email      varchar(50) unique,
 phone 		varchar(50)
)

create table products(
product_id serial primary key,
product_name varchar(100) not null,
category  varchar(50),
unit_price  numeric(10,2) not null
)

create table locations(
location_id serial primary key,
city 		varchar(50) not null,
state 		varchar(50) ,
country   	varchar(50) not null
)

-- =========================================
-- CUSTOMERS - 10 RECORDS
-- =========================================

INSERT INTO customers (first_name, last_name, email, phone)
VALUES
('Rahul', 'Sharma', 'rahul@gmail.com', '9876543210'),
('Amit', 'Patel', 'amit@gmail.com', '9876543211'),
('Priya', 'Mehta', 'priya@gmail.com', '9876543212'),
('Neha', 'Shah', 'neha@gmail.com', '9876543213'),
('Rohan', 'Desai', 'rohan@gmail.com', '9876543214'),
('Anjali', 'Joshi', 'anjali@gmail.com', '9876543215'),
('Vivek', 'Patel', 'vivek@gmail.com', '9876543216'),
('Pooja', 'Rana', 'pooja@gmail.com', '9876543217'),
('Karan', 'Verma', 'karan@gmail.com', '9876543218'),
('Sneha', 'Kapoor', 'sneha@gmail.com', '9876543219');


-- =========================================
-- PRODUCTS - 10 RECORDS
-- =========================================

INSERT INTO products (product_name, category, unit_price)
VALUES
('Laptop', 'Electronics', 65000.00),
('Smartphone', 'Electronics', 30000.00),
('Headphones', 'Electronics', 2500.00),
('Keyboard', 'Electronics', 1800.00),
('Mouse', 'Electronics', 900.00),
('Office Chair', 'Furniture', 8500.00),
('Backpack', 'Accessories', 1800.00),
('Running Shoes', 'Sports', 4500.00),
('T-Shirt', 'Clothing', 1200.00),
('Water Bottle', 'Sports', 700.00);


-- =========================================
-- LOCATIONS - 10 RECORDS
-- =========================================

INSERT INTO locations (city, state, country)
VALUES
('Ahmedabad', 'Gujarat', 'India'),
('Mumbai', 'Maharashtra', 'India'),
('Delhi', 'Delhi', 'India'),
('Pune', 'Maharashtra', 'India'),
('Bangalore', 'Karnataka', 'India'),
('Chennai', 'Tamil Nadu', 'India'),
('Jaipur', 'Rajasthan', 'India'),
('Surat', 'Gujarat', 'India'),
('Vadodara', 'Gujarat', 'India'),
('Hyderabad', 'Telangana', 'India');

select * from customers;
select * from products;
select * from locations;
