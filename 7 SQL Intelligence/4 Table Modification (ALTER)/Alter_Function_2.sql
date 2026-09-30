
Alter Table customers
add Column Phone varchar(15) unique;

select * from customers;

Alter table customers
add column is_active Boolean Default True;

update customers set phone = 965874