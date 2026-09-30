select * from customers where age >30;
select * from customers order by create_at DESC;
select * from customers order by Name asc , Age aSC;
select * from customers order by create_at DESC limit 5;

select count(*) from customers where age > 30;
select * from customers where age > 30 limit 5 offset 5;
select * from customers where age > 30 limit 5 ;

select distinct age from customers order by age;

select * from customers where age between 18 and 25;
select * from customers where age between 18 and 25 order by age;
select * From customers where age in (18,25,30) ;

select * from customers where name ilike 'a%';

select * from customers where age::text  ilike '1%'

select age , count(*) from customers group by age order by age;

select age , count(*) From customers where age between 18 and 20  group by age;

select age , count(*) as Per  from customers group by age Having age between 18 and 30 order by age;

select * from customers where age <31 and name ilike 'a%' order by age;

select * from customers where Not age <31 And not name ilike 'a%' order by age;


