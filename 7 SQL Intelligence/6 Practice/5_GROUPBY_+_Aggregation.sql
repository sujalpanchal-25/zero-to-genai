select * from customers;

select count(*) from customers;

select sum(age) as total_age from customers;

select avg(age) as Ave_age from customers;

select round(avg(age),2) as Ave_age from customers;

select min(age) as youngest_age from customers;

select max(age) as youngest_age from customers;

select age, count(age) from customers group by age;
select age, count(age) from customers group by age order by age;

select age, count(age) from customers where age between 18 and 30 group by age;
select age, count(age) from customers where age between 18 and 30 group by age order by age;

select age, count(age) from customers group by age having count(age) > 1;

select age, count(age) as count_of_customers from customers group by age order by count_of_customers DESC;