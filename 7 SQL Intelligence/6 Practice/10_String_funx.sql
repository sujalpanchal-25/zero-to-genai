select * from customers;

select name , lower(name) from customers; 

select name , upper(name) from customers; 

select name , length(name) from customers;

select name ,length(name) as length_name from customers
where length(name) > 4 order by length_name;

select left(name,3) from customers; 

select Right(name,3) from customers; 

select name,substring(name,2,5) from customers;

select id, name, concat(left(name,3),'-',id) from customers;

select id, name,age, concat_ws('-',left(name,3),id,age) from customers;

select name , replace(name,'a','A') from customers;



