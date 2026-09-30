select name , age from customers;

select lower(name) , age from customers;
select upper(name) , age from customers;

select upper(name) , Length(name) as Name_length from customers;

select name , substring(name,2,4) FROM customers;

select name , left(name,3) FROM customers;

select name , Right(name,3) FROM customers;

select id,name , concat_ws('-',left(name,3),id,age) as code from customers;

select name , replace(name,'a','A') from customers;

select id,name , concat(left(name,3),id) as code from customers;