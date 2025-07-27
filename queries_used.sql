-- Select * from sampledata;

/** select country, max(amount)
from sampledata 
group by country; **/

/** select country, min(amount)
from sampledata
group by country; **/

/** select * from sampledata
order by amount desc;  **/

/** select product,country from sampledata 
where product like "Peanut butter%" ; **/

/** Select Product,country from sampledata
where product != "peanut Butter cubes"; **/

-- Select distinct product from sampledata;

/** Select product from sampledata
where product like "%choco"; **/

/** Select product from sampledata
where product like "%bars"; **/

/** Select * from sampledata
LIMIT 50; **/

/** select N.Sales_Person, S.product, N.Amount,S.Date
From Sampledata as S
Join newdata as N 
ON S.Country = N.Country; **/

/** Select S.Sales_person, N.date, S.Boxes_Shipped
From sampledata as S
Left Join newdata as N
ON S.Amount=N.Amount; **/

/** Select S.Sales_Person,S.Product,N.Date
From sampledata as S
Right Join newdata as N
ON S.Amount=N.Amount; **/

/** select N.Sales_Person, S.product, N.Amount,S.Date
From Sampledata as S
 Cross Join newdata as N 
ON S.Country = N.Country; **/

/** Select * From Sampledata
where amount is Null; **/

/** Update sampledata
Set amount = amount*1.1
where product = "Milk bar"; **/

/** Delete from sampledata
where amount 
not in(select min(amount) from sampledata group by country); **/

/** create table revenue AS
select country,sum(amount) as totalamt
from sampledata
group by country; **/

