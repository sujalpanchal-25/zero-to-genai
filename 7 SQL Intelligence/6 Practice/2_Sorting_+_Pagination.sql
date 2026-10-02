select * from customers;

select * from customers order by age;

select * from customers order by age DESC;

select * from customers order by Name;

select * from customers order by Name asc , age asc;
select id,name,email,age,create_at from customers order by 2,4;

select * from customers order by age limit 5;

select * from customers order by age DESC limit 5;

select * from customers order by age limit 5;
select * from customers order by age offset 5;

select * from customers order by age DESC;
select * from customers order by age DESC offset 5;

select * from customers order by id DESC limit 5 ;