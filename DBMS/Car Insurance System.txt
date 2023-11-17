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
    cust_lisence varchar(250),
    c_id int,
    foreign key(c_id) references company(c_id)
);
desc customer;
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
create table accident(
	a_report varchar(250) primary key,
    a_place varchar(250),
    a_type varchar(250),
    a_date varchar(250),
    car_no varchar(250),
    foreign key(car_no) references car(car_no)
);
desc accident;
create table services(
	s_id varchar(250) primary key,
    s_addOn varchar(250),
    s_cust varchar(250),
    c_id int,
    foreign key(c_id) references company(c_id)
);
desc services;
create table payment(
	p_id varchar(25) primary key,
    p_amt int NOT NULL,
    p_time int default 1,
    p_dur int,
    check(p_dur>=1)
);
desc payment;
create table Online(
	p_id varchar(250),
    foreign key(p_id) references payment(p_id),
    on_UPI varchar(250),
    on_card varchar(250),
    on_netb varchar(250)
);
desc Online;
create table Offline(
	p_id varchar(250),
    foreign key(p_id) references payment(p_id),
    of_cheque varchar(250),
    of_cash varchar(250)
);
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
	ip_id varchar(250) primary key,
    ip_amt int,
    ip_plan varchar(250),
    ip_date date,
    cust_id varchar(250),
    foreign key(cust_id) references customer(cust_id)
);
desc insurance;
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
