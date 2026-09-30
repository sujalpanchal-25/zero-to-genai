select name , age , 
case
	when age < 20 then 'Teen'
	when age < 30 then 'Young'
	when age < 40 then 'Adolescent'
	Else 'Old'
	End as Age_Group
	From customers;