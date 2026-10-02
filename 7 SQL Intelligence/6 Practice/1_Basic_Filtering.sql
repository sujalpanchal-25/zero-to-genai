select * from customers;

select * From customers where age>25;
select * From customers where age>25 order by age;

select * from customers where age< 30;
select * from customers where age< 30 order by age;

select * from customers where age in(20);
select * from customers where age = 20;

select * from customers where age between 26 and 39;
select * from customers where age >25 and age < 40;
select * from customers where age between 26 and 39 order by age;
select * from customers where age >25 and age < 40 order by age;

select * from customers where age != 20;

select * from customers where age <25 and name ilike 'a%';
select * from customers where age <25 and name like 'A%';

select * from customers where age >30 and name ilike 'a%';
select * from customers where age >30 and name like 'A%';

