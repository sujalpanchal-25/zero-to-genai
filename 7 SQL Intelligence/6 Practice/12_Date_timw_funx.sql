select * from customers; 

select current_date;

select now();

select  extract('year' from now());
select  extract('Month' from now());
select  extract('Week' from now());
select  extract('Quarter' from now());
select  extract('day' from now());
select  extract('Hour' from now());

select Age(current_date,'2025-07-25');

select now() ,Date_trunc('year',now());
select now() ,Date_trunc('month',now());
select now() ,Date_trunc('week',now());
select now() ,Date_trunc('day',now());





















