--create table products
--(
--	catogary varchar not null,
--	prod_id int not null,
--	price int not null,
--	pro_type varchar not null,
--	pro_location varchar not null,
--	address varchar not null,
--	p_size int not null,
--  primary key(prod_id)
--);

--create table description 
--(
--	prod_id int,
--	constraint fk_prod_id foreign key(prod_id) references products(prod_id),
--	descrip varchar
--)


-- create table customers
-- (
-- 	username varchar not null,
-- 	f_name varchar not null,
-- 	l_name varchar not null,
-- 	contact numeric(14) not null,
-- 	email varchar not null,
-- 	primary key(username)
-- )

-- create table credential
-- (
-- 	usernames varchar,
-- 	constraint fk_username foreign key(username) references customers(username),
-- 	pass varchar not null
-- )

select * from products