
select current_date , now();

select Extract(YEAR From now());	
select Extract(MOnth From now());	
select Extract(Week From now());	
select Extract(Day From now());	
select Extract(Hour From now());	
select Extract(Minute From now());	
select Extract( quarter From now());	


select AGE(current_date , '2025-07-25');

select now() , Date_Trunc('year',now());
select now() , Date_Trunc('month',now());
select now() , Date_Trunc('week',now());
select now() , Date_Trunc('day',now());
select now() , Date_Trunc('Hour',now());
select now() , Date_Trunc('Minute',now());
select now() , Date_Trunc('Quarter',now());

