select * from customers;

select round(avg(age)) as avg_age from customers where name like 'A%';

SELECT COUNT(*) AS customer_count
FROM customers
WHERE age BETWEEN 20 AND 30;

select round(avg(age)) as avg_age from customers where age between 20 and 30;

select age,count(age) as age_count from customers group by age having count(age) > 1;

select age_group ,count(age_group) from customers group by age_Group; 

select name ,age from customers where name like 'A%' order by age;

select name , age from customers where name like '%a%' order by age DESC limit 3;

SELECT 
     MIN(age) AS min_age,
     MAX(age) AS max_age
FROM customers
WHERE name LIKE 'A%';

select name , age ,upper(name) , length(name) , age_Group from customers; 

select concat_ws('-',left(name,3),id,age) from customers;

select name , age , age +5 , age*2 from customers;

select id , name , extract('Year' from admission) from customers;

select * from customers;

select round(avg(age)) as avg_age from customers where name like 'A%';

SELECT COUNT(*) AS customer_count
FROM customers
WHERE age BETWEEN 20 AND 30;

select round(avg(age)) as avg_age from customers where age between 20 and 30;

select age,count(age) as age_count from customers group by age having count(age) > 1;

select age_group ,count(age_group) from customers group by age_Group; 

select name ,age from customers where name like 'A%' order by age;

select name , age from customers where name like '%a%' order by age DESC limit 3;

SELECT 
     MIN(age) AS min_age,
     MAX(age) AS max_age
FROM customers
WHERE name LIKE 'A%';

select name , age ,upper(name) , length(name) , age_Group from customers; 

select concat_ws('-',left(name,3),id,age) from customers;

select name , age , age +5 , age*2 from customers;

select id , name , extract('Year' from admission) from customers;

SELECT 
    EXTRACT(MONTH FROM admission) AS month,
    COUNT(*) AS customer_count
FROM customers
GROUP BY month
ORDER BY month;

SELECT 
    EXTRACT(YEAR FROM admission) AS year,
    COUNT(*) AS customer_count
FROM customers
GROUP BY year
ORDER BY year;

select name , admission , EXTRACT(YEAR FROM admission), EXTRACT(MONTH FROM admission) , EXTRACT(QUARTER FROM admission) from customers;