select * from customers;

Alter table customers 
add column phone varchar(15);

alter table customers
add column is_active boolean default True;

select * from customers; 

alter table customers
add column Country varchar(20) not null default 'India';

alter table customers
rename create_at to Admission;

alter table customers
alter age type Int;

alter table customers
alter phone set default 'N/A';

alter table customers
alter phone drop default;

alter table customers
add constraint phone unique(phone);

alter table customers
drop constraint phone;

alter table customers
drop is_active;

alter table customers
drop Country;

select * from customers;

