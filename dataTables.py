#Datatables for (?):*Username anculator at end fod password; create a loop for returning customer or need to register.
#**reservation date & time; create array for month weeks and days? *another one *dj khaled voice* for services and how much were gonna
#charge for (maybe a promo code for discount?)*checkout calr su, wemmary including reservation times and confirmation number of order
create table cohort2 
(
user_id serial primary key, #username and password?
first_name text not null,
last_name text not null,
phone_number text not null #maybe also email address?
)

insert into cohort2 (first_name, last_name, phone_number, email) #same as before but this would be input
values(''),
(''),
('')

select * from cohort2 order by user_id asc #pull up table

delete from cohort2 where user_id=14

update cohort2 set first_name='Dunieski' where user_id=8 #forgot password?

select user_id,first_name from cohort2 where user_id=8 #not sure how we can implement come back to see if necessary


CREATE SEQUENCE serial START 1;
DaT
