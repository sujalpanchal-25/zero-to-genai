select * from customers;

update customers set name = 'Aena' where id = 1;

select * from customers order by id;

update customers set age = 25  where id =5;

select * from customers order by id;

alter table customers 
add column country varchar(20) ;

update customers set country = 'india';

select * from customers order by id;

alter table customers 
add column is_active boolean default true;

update customers set is_active = False where age>35;

update customers set is_active = False where name like 'A%';

update customers set phone = '9402514255' where id = 3;
