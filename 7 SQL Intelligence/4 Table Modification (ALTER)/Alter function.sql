Alter Table customers
add Column Phone varchar(15) unique;

select * from customers order by id;

Alter table customers
add column is_active Boolean Default True;

update customers set name = 'Aaravv' where id = 1

alter table customers 
add column country varchar(20) default 'India' Not null;

alter table customers drop column phone;
alter table customers drop column is_active;
alter table customers drop column country;


alter table customers 
rename column create_at to Admission;


alter table customers alter column age Type int;

alter table customers add column Phone varchar(20);

alter table customers alter column Phone set default 'N/A';

insert into customers (name,email,age) values 
('Kashish', 'kashish232@reddit.com' , 20);

alter table customers alter column phone drop default;

alter table customers add constraint phone unique(phone);
alter table customers drop constraint phone ;