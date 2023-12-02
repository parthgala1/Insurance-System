drop database insurance_company;
 
set sql_safe_updates = 0;
 
create database insurance_company;
use insurance_company;
create table company(
	c_id int primary key,
    c_name varchar(250),
    c_gstno varchar(250),
    c_loc varchar(250)
);
desc company;
 
create table customer(
	cust_id varchar(250) primary key,
    cust_name varchar(250),
    cust_license varchar(250),
    cust_pass varchar(250),
    c_id int,
    foreign key(c_id) references company(c_id)
);
desc customer;
 
drop table customer;
 
select * from customer;
 
select * from custmob;
 
create table custmob(
	cust_id varchar(250) , 
    foreign key(cust_id) references customer(cust_id),
    cust_mob varchar(10) 
);
desc custmob;
 
alter table custmob 
	add primary key(cust_id, cust_mob);
desc custmob;
 
create table car(
	car_no varchar(250) primary key,
    car_owner varchar(250),
    car_model varchar(250),
    car_type varchar(250),
    cust_id varchar(250),
    foreign key(cust_id) references customer(cust_id)
);
desc car;
select * from car;	
 
drop table car;
 
create table accident(
	a_report varchar(250) primary key default "a_place:\'\', a_time: \'\', a_date:\'\'",
    a_place varchar(250),
    a_time varchar(250),
    a_date varchar(250),
    car_no varchar(250),
    foreign key(car_no) references car(car_no)
);
desc accident;
 
drop table accident;

select * from accident;
 
create table services(
	s_id int primary key default 1000,
    s_addOn varchar(250),
    s_cust varchar(250),
    c_id int,
    foreign key(c_id) references company(c_id)
);
desc services;
 
drop table services;
 
create table payment(
	p_id int primary key auto_increment ,
    p_amt float NOT NULL,
    p_time varchar(250),
    p_dur varchar(250),
    cust_id varchar(250),
    foreign key(cust_id) references customer(cust_id)
)auto_increment = 100000;
desc payment;
select * from payment;
drop table payment;
 
insert into payment(p_amt, p_time, p_dur, cust_id) values(10000, "4:00", "1 year", 123);
 
create table Online(
	p_id int,
    foreign key(p_id) references payment(p_id),
    on_UPI varchar(250) default NULL,
    on_card varchar(250) default NULL,
    on_netb varchar(250) default NULL
);
desc Online;
 
select * from Online;
 
drop table Online;
 
create table Offline(
	p_id int,
    foreign key(p_id) references payment(p_id),
    of_cheque varchar(250),
    of_cash varchar(250)
);
 
 
insert into payment values (100, 10000, 2, 3); 
insert into Offline(p_id, of_cheque, of_cash) values(100, "Cheque", "Cash");
 
select * from Offline;
 
drop table Offline;
desc Offline;
create table employee(
	e_id varchar(250) primary key,
    e_role varchar(250),
    e_name varchar(250),
    c_id int,
    cust_id varchar(250),
    foreign key(c_id) references company(c_id),
    foreign key(cust_id) references customer(cust_id)
);
desc employee;
create table emob(
	e_id varchar(250),
    foreign key(e_id) references employee(e_id),
    e_mob varchar(10)
);
alter table emob
	add primary key(e_id, e_mob);
desc emob;
create table insurance(
	ip_id int auto_increment primary key,
    ip_amt int,
    ip_plan varchar(250),
    ip_date varchar(250),
    cust_id varchar(250),
    foreign key(cust_id) references customer(cust_id)
)AUTO_INCREMENT = 1000;
 
-- QUERY
create view p1 as select ip_amt from insurance i,customer c, payment p where i.cust_id = p.cust_id;  
UPDATE payment set p_amt = (select ip_amt from insurance i,customer c where i.cust_id = c.cust_id and i.cust_id = 123);
 
select * from insurance;
select * from payment;
 
desc insurance;
 
select * from insurance;
 
drop table insurance;
 
create table bill(
	b_id varchar(250) primary key,
    b_tax double,
    b_amt double,
    ip_id varchar(250),
    foreign key(ip_id) references insurance(ip_id)
);
desc bill;
create table inspection(
	i_rep varchar(250) primary key,
    i_cond varchar(250),
    i_damage varchar(250),
    e_id varchar(250),
    foreign key(e_id) references employee(e_id),
    a_report varchar(250),
    foreign key(a_report) references accident(a_report)
);
desc inspection;
 
drop table inspection;
 
# Changes done after
 
insert into company
values (1,'cardekho','3455612345','mumbai');
 
select * from company;
 
insert into customer
values ('101','swayam','34556','swayam09',1);

insert into customer
values ('11','swayam','34556','swayam20',1);
 
 
select * from customer;
 
insert into insurance(ip_amt, ip_plan, ip_date) values (12, "Parth", "2023-10-12");
 
insert into customer values(102, "Parth", "324563", "pass@123", 1);
 
select * from customer where cust_id = 101;
 
select * from insurance;