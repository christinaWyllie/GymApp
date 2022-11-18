
DROP DATABASE IF EXISTS GYM_DATABASE;
CREATE DATABASE GYM_DATABASE; 
USE GYM_DATABASE;

DROP TABLE IF EXISTS PERSON;
CREATE TABLE PERSON (
ssn CHAR(9) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
email VARCHAR(25) NOT NULL,
primary key (ssn), 
UNIQUE (email)
);

DROP TABLE IF EXISTS ADMIN;
CREATE TABLE ADMIN (
assn CHAR(9) NOT NULL,
admin_id CHAR(10) NOT NULL,
admin_email VARCHAR(25) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
PRIMARY KEY (admin_id),
FOREIGN KEY (assn) REFERENCES PERSON(ssn),
FOREIGN KEY (admin_email) REFERENCES PERSON(email) 
);

DROP TABLE IF EXISTS OWNER;
CREATE TABLE OWNER (
ossn CHAR(9) NOT NULL,
owner_id CHAR(10) NOT NULL,
owner_email VARCHAR(25) NOT NULL,
Branch_num INT NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
PRIMARY KEY (owner_id),
FOREIGN KEY (ossn) REFERENCES ADMIN(assn),
FOREIGN KEY (owner_email) REFERENCES ADMIN(admin_email) 
);

DROP TABLE IF EXISTS MANAGER;
CREATE TABLE MANAGER (
mssn CHAR(9) NOT NULL,
m_id CHAR(10) NOT NULL,
m_email VARCHAR(25) NOT NULL,
branch_no INT NOT NULL,
PRIMARY KEY (m_id),
FOREIGN KEY (mssn) REFERENCES ADMIN(assn),
FOREIGN KEY (m_email) REFERENCES ADMIN(admin_email) 
);

DROP TABLE IF EXISTS CLIENT;
CREATE TABLE CLIENT (
cssn CHAR(9) NOT NULL,
client_id CHAR(10) NOT NULL,
client_email VARCHAR(25) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
PRIMARY KEY (client_id),
FOREIGN KEY (cssn) REFERENCES PERSON(ssn),
FOREIGN KEY (client_email) REFERENCES PERSON(email) 
);

DROP TABLE IF EXISTS MEMBER;
CREATE TABLE MEMBER (
mssn CHAR(9) NOT NULL,
client_id CHAR(10) NOT NULL,
membership_id CHAR(10) NOT NULL,
member_email VARCHAR(25) NOT NULL,
type VARCHAR(10) NOT NULL,
status bit(1) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
PRIMARY KEY (membership_id),
FOREIGN KEY (mssn) REFERENCES CLIENT(cssn),
FOREIGN KEY (client_id) REFERENCES CLIENT(client_id),
FOREIGN KEY (member_email) REFERENCES CLIENT(client_email) 
);

DROP TABLE IF EXISTS RESTRICTED_USER;
CREATE TABLE RESTRICTED_USER(
rssn CHAR(9) NOT NULL,
r_user_id CHAR(10) NOT NULL,
r_email VARCHAR(25) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
PRIMARY KEY (r_user_id),
FOREIGN KEY (rssn) REFERENCES PERSON(ssn),
FOREIGN KEY (r_email) REFERENCES PERSON(email) 
);

DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE(
essn char(9) NOT NULL,
e_user_id char(10) NOT NULL,
e_email varchar (25) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
branch_no int NOT NULL,
PRIMARY KEY (e_user_id),
FOREIGN KEY (e_user_id) REFERENCES RESTRICTED_USER(r_user_id),
FOREIGN KEY (essn) REFERENCES RESTRICTED_USER(rssn),
FOREIGN KEY (e_email) REFERENCES RESTRICTED_USER(r_email) 
);

DROP TABLE IF EXISTS ASSOCIATE;
CREATE TABLE ASSOCIATE(
sssn char(9) NOT NULL,
s_user_id char(10) NOT NULL,
s_email varchar (25) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
branch_no int NOT NULL,
PRIMARY KEY (s_user_id),
FOREIGN KEY (s_user_id) REFERENCES EMPLOYEE(e_user_id),
FOREIGN KEY (sssn) REFERENCES EMPLOYEE(essn),
FOREIGN KEY (s_email) REFERENCES EMPLOYEE(e_email) );

DROP TABLE IF EXISTS TRAINER;
CREATE TABLE TRAINER(
tssn char(9) NOT NULL,
t_user_id char(10) NOT NULL,
t_email varchar (25) NOT NULL,
fname VARCHAR(15) NOT NULL,
lname VARCHAR(15) NOT NULL,
address VARCHAR(30),
phone_number INT NOT NULL,
branch_no int NOT NULL,
PRIMARY KEY (t_user_id),
FOREIGN KEY (t_user_id) REFERENCES EMPLOYEE(e_user_id),
FOREIGN KEY (tssn) REFERENCES EMPLOYEE(essn),
FOREIGN KEY (t_email) REFERENCES EMPLOYEE(e_email) );

DROP TABLE IF EXISTS CLASS;
CREATE TABLE CLASS (
class_no INT NOT NULL,
date DATE NOT NULL,
time VARCHAR(10) NOT NULL,
branch_no INT NOT NULL, 
t_id CHAR(9) NOT NULL,
t_email VARCHAR(25)NOT NULL,
tssn INT NOT NULL,
PRIMARY KEY(class_no),
FOREIGN KEY(t_id) REFERENCES TRAINER(t_user_id) );

DROP TABLE IF EXISTS TRAINER_CLASS;
CREATE TABLE TRAINER_CLASS(
t_user_id char(10) NOT NULL,
class_no int NOT NULL,
PRIMARY KEY (t_user_id),
FOREIGN KEY (t_user_id) REFERENCES TRAINER(t_user_id),
FOREIGN KEY (class_no) REFERENCES CLASS(class_no) );

DROP TABLE IF EXISTS WEEKLY_SCHEDULE;
CREATE TABLE WEEKLY_SCHEDULE(
m_id char(10) NOT NULL,
r_user_id char(10) NOT NULL,
branch_no int NOT NULL,
time_slots varchar(20) NOT NULL,
PRIMARY KEY (r_user_id),
FOREIGN KEY (m_id) REFERENCES MANAGER(m_id));



DROP TABLE IF EXISTS T_BOOKS_R;
CREATE TABLE T_BOOKS_R (
r_email varchar(25) NOT NULL,
r_id char(10) NOT NULL,
rssn char(9) NOT NULL,
room_id char(9) NOT NULL,
PRIMARY KEY (r_id),
FOREIGN KEY (r_email) REFERENCES TRAINER(r_email),
FOREIGN KEY (r_id) REFERENCES TRAINER(r_id),
FOREIGN KEY (rssn) REFERENCES TRAINER (rssn),
FOREIGN KEY (room_id) REFERENCES ROOMS(room_id) );


DROP TABLE IF EXISTS EQUIPMENT;
CREATE TABLE EQUIPMENT (
equipment_no INT NOT NULL,
cdn VARCHAR(15) NOT NULL,
duration INT,
branch_no INT NOT NULL,
PRIMARY KEY(equipment_no),
FOREIGN KEY(branch_no) REFERENCES GYM(branch_no) );

DROP TABLE IF EXISTS EQUIPMENT_AMOUNT;
CREATE TABLE EQUIPMENT_AMOUNT(
equipment_no INT NOT NULL, 
amount INT NOT NULL, 
PRIMARY KEY(equipment_no, amount), 
FOREIGN KEY(equipment_no) REFERENCES EQUIPMENT(equipment_no));

DROP TABLE IF EXISTS SUPPLIES;
CREATE TABLE SUPPLIES (
sname VARCHAR(15) NOT NULL,
supply_no INT NOT NULL,
stock INT NOT NULL,
branch_no INT NOT NULL,
PRIMARY KEY(supply_no),
FOREIGN KEY(branch_no) REFERENCES GYM(branch_no) );

DROP TABLE IF EXISTS GYM;
CREATE TABLE GYM(
branch_no INT NOT NULL,
location VARCHAR(30) NOT NULL,
ossn CHAR(9) NOT NULL,
owner_email varchar(25) NOT NULL,
owner_id char(10) NOT NULL,
PRIMARY KEY (branch_no),
FOREIGN KEY (ossn) REFERENCES OWNER(ossn),
FOREIGN KEY (owner_email) REFERENCES OWNER(owner_email),
FOREIGN_KEY (owner_id) REFERENCES OWNER(owner_id) );

DROP TABLE IF EXISTS SUBSCRIPTION;
CREATE TABLE SUBSCRIPTION(
login_id VARCHAR(30) NOT NULL,
name VARCHAR(25) NOT NULL,
status bit(1) NOT NULL,
PRIMARY KEY (login_id) );

DROP TABLE IF EXISTS SUB_BRANCHES;
CREATE TABLE SUB_BRANCHES(
login_id VARCHAR(30) NOT NULL, 
branch_no INT NOT NULL, 
PRIMARY KEY(login_id, branch_no), 
FOREIGN KEY(branch_no) REFERENCES GYM(branch_no),
FOREIGN KEY(login_id) REFERENCES SUBSCRIPTION(login_id));

SELECT *
FROM PERSON;
