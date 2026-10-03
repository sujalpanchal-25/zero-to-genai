select *
from customers c
join sales s
on c.customer_id = s.customer_id
order by c.customer_id , s.sale_date
;


select c.customer_id, concat_ws(' ',c.first_name,c.last_name) as Full_Name,
s.sale_id,s.sale_date,s.total_amount
from customers c
join sales s
on c.customer_id = s.customer_id
order by c.customer_id , s.sale_date


select concat_ws(' ' ,c.first_name,c.last_name),s.sale_id,s.sale_date,s.total_amount
from sales s 
join customers c
on c.customer_id = s.customer_id
;

select concat_ws(' ' , c.first_name , c.last_name) as Full_name,
p.product_name,
sum(s.quantity) as total_qty
from sales s 
join customers c
on s.customer_id = c.customer_id
join products p
on s.product_id = p.product_id
group by full_name,p.product_name


