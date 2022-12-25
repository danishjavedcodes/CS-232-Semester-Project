-------------------BY Danish Javed-------------------
-- create table branch(branch_code integer primary key, city varchar);

-- create table adminusers(f_name varchar not null,
-- 						l_name varchar,
-- 						user_id integer primary key not null,
-- 						user_password varchar not null,
-- 						e_mail varchar not null,
-- 						phone_number numeric (14) not null,
-- 						branch_code integer not null references branch(branch_code),
-- 						user_type varchar not null);
-- CREATE FUNCTION CHECK_PASS(U_ID INT, PASS VARCHAR)
-- RETURNS BOOLEAN AS $$
-- DECLARE 
-- 	CHECK_PASS BOOLEAN;
-- BEGIN
-- 	SELECT (user_password = $2) into CHECK_PASS
-- 	FROM adminusers
-- 	where user_id = $1;
-- 	return CHECK_PASS;
-- END;
-- $$  LANGUAGE plpgsql

-- select * from adminusers

-- CREATE FUNCTION create_Adminuser(f_name,l_name,user_id,user_password,e_mail,phone_number,branch_code,user_type)
-- BEGIN
-- 	insert into adminusers values ($1,$2,$3,$4,$5,$6,$7,$8)
-- END;
-- select * from adminusers

-- CREATE FUNCTION GET_PASS(U_ID INT)
-- RETURNS VARCHAR AS $$
-- DECLARE 
-- 	CHECK_PASS VARCHAR;
-- BEGIN
-- 	SELECT user_password into CHECK_PASS
-- 	FROM adminusers
-- 	where user_id = $1;
-- 	return CHECK_PASS;
-- END;
-- $$  LANGUAGE plpgsql

-- CREATE FUNCTION GET_type(U_ID INT)
-- RETURNS VARCHAR AS $$
-- DECLARE 
-- 	user_t VARCHAR;
-- BEGIN
-- 	SELECT user_type into user_t
-- 	FROM adminusers
-- 	where user_id = $1;
-- 	return user_t;
-- END;
-- $$  LANGUAGE plpgsql



------------------by Ali -------------------
-- create table products
-- (
-- 	catogary varchar not null,
-- 	prod_id int not null,
-- 	price int not null,
-- 	pro_type varchar not null,
-- 	pro_location varchar not null,
-- 	address varchar not null,
-- 	p_size int not null,
--  primary key(prod_id)
-- );


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


------------------BY DANISH----------------

-- drop table customers

--create table customers
-- (
-- 	user_id varchar not null primary key,
-- 	f_name varchar not null,
-- 	l_name varchar,
-- 	contact numeric(14) not null,
-- 	email varchar not null,
-- 	pass varchar not null
-- )


-- CREATE FUNCTION GET_customers_PASS(U_ID varchar)
-- RETURNS VARCHAR AS $$
-- DECLARE 
-- 	CHECK_PASS VARCHAR;
-- BEGIN
-- 	SELECT pass into CHECK_PASS
-- 	FROM customers
-- 	where user_id = $1;
-- 	return CHECK_PASS;
-- END;
-- $$  LANGUAGE plpgsql


-- create table products
-- (
-- 	prod_id int not null primary key,
-- 	catogary varchar not null,
-- 	price int not null,
-- 	pro_type varchar not null,
-- 	pro_location varchar not null,
-- 	address varchar not null,
-- 	p_size int not null,
--  	description varchar
-- );


-- CREATE PROCEDURE add_products(p_id integer,cat varchar, price integer, p_type varchar, p_loc varchar, address varchar, p_size integer, p_decription varchar)
-- LANGUAGE SQL
-- as $$
--   insert into products values (p_id+1, cat, price, p_type, p_loc, address, p_size, p_decription);
-- $$;