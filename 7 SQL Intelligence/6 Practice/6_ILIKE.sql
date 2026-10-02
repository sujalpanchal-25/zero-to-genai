select * from customers;

select * from customers where name like 'A%';
select * from customers where name ilike 'a%';

select * from customers where name like 'K%';
select * from customers where name ilike 'K%';

select * from customers where name ilike '%a';

select * from customers where name ilike '%an%';

select * from customers where email ilike '%gmail%';

select * from customers where email ilike '%.com';

select * from customers where name like 'A%' and age<30;
