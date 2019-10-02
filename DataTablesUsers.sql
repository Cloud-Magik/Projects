create table Users
(
    user_name text not null,  
	pass_word text not null,
    first_name text not null,
    last_name text not null,
    phone_number text not null,
	email text not null 
)

insert into Users(user_name, pass_word, first_name, last_name, phone_number, email)
values('Username', 'Pass_word', 'first_name', 'last_name', 'phone_number', 'email')

select * from Users 

delete from Users

update Users

