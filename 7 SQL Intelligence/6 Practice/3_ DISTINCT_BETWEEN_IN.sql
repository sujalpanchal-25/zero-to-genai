select * from customers;           

select distinct(age) from customers ;
select distinct(age) from customers order by age;

select * from customers where age between 20 and 30;
select * from customers where age between 20 and 30 order by age;

select * from customers where age in(18,20,25,30);
select * from customers where age in(18,20,25,30) order by age;

select * from customers where age not between 20 and 30;
select * from customers where age not between 20 and 30 order by age;

select distinct(age) from customers where age between 20 and 30;


