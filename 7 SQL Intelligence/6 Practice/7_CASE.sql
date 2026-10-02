select * from customers;

Alter table customers
add column Age_Group varchar(20);

update customers set Age_Group = case 
when age < 20 then 'Teen'
when age between 20 and 29 then 'Young'
when age between 30 and 39 then 'Adult'
Else 'Senior'
End;

select * from customers;

select name,age,age_group from customers;

select * ,case
when age < 25 then 'Junior'
when age between 25 and 34 then 'Middle'
Else 'senior'
end as classiification
from customers;

select age_Group , count(age_group) as count_ageGroup from customers group by age_group;

select * from customers order by age;           