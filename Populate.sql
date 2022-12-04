INSERT INTO PERSON
VALUES 	(123456788,"tina", "w", "24 School Drive", "password", 4034034033, "t.w@ucalgary.ca"), 
        (133456789,"ramneet", "h", "23 School Drive", "password", 4034034034, "r.h@ucalgary.ca"), 
        (123456798,"isaac", "d", "22 School Drive", "password", 4034034043, "i.d@ucalgary.ca"), 
        (466709091, "member1", "stark", "87 Member street", "password", 4039925656, "member1@ucalgary.ca"),
        (466707071, "member2", "mcdonald", "91 Member street", "password", 4038855858, "member2@ucalgary.ca"),
        (466606061, "member3", "smith",  "3 Member street", "password", 4039919911, "member3@ucalgary.ca"), 
        (123333335,"manager", "f", "24 Manager Lane", "password", 4035445454, "manager@ucalgary.ca");

INSERT INTO RESTRICTED_USER
VALUES  (123456788, 1, "t.w@ucalgary.ca", "tina", "w", "24 School Drive", "password", 4034034033), 
        (133456789, 2, "r.h@ucalgary.ca", "ramneet", "h", "23 School Drive", "password", 4034034034), 
        (123456798, 3, "i.d@ucalgary.ca", "isaac", "d", "22 School Drive", "password", 4034034043);

INSERT INTO EMPLOYEE
VALUES  (123456788, 1, "t.w@ucalgary.ca", "tina", "w", "24 School Drive", 4034034033, "password", 1), 
        (133456789, 2, "r.h@ucalgary.ca", "ramneet", "h", "23 School Drive", 4034034034, "password", 1), 
        (123456798, 3, "i.d@ucalgary.ca", "isaac", "d", "22 School Drive", 4034034043, "password", 1);

INSERT INTO ASSOCIATE
VALUES  (123456788, 1, "t.w@ucalgary.ca", "tina", "w", "24 School Drive", 4034034033, "password", 1), 
        (133456789, 2, "r.h@ucalgary.ca", "ramneet", "h", "23 School Drive", 4034034034, "password", 1);

INSERT INTO TRAINER
VALUES (123456798, 3, "i.d@ucalgary.ca", "isaac", "d", "22 School Drive", 4034034043, "password", 1);

INSERT INTO ADMIN
VALUES (123333335, 1, "manager@ucalgary.ca", "manager", "f", "24 Manager Lane", "password", 4035445454);

INSERT INTO MANAGER
VALUES (123333335, 1, "manager@ucalgary.ca", 1, "manager", "f", "24 Manager Lane", "password", 4035445454);


INSERT INTO CLIENT
VALUES (466709091, 1, "member1@ucalgary.ca", "member1", "stark", "password", "87 Member street", 4039925656),
        (466707071, 2, "member2@ucalgary.ca", "member2", "mcdonald", "password", "91 Member street", 4038855858),
        (466606061, 3, "member3@ucalgary.ca", "member3", "smith", "password", "3 Member street", 4039919911);

INSERT INTO MEMBER
VALUES (466709091, 1, 1, "member1@ucalgary.ca", True, "member1", "stark", "87 Member street", "password", 4039925656), 
        (466707071, 2, 2, "member2@ucalgary.ca", FALSE, "member2", "mcdonald", "91 Member street", "password", 4038855858), 
        (466606061, 3, 3, "member3@ucalgary.ca", True, "member3", "smith", "3 Member street", "password", 4039919911);
        
INSERT INTO CLASS
VALUES (1, "Monday", "1:00", 1, 3, "i.d@ucalgary.ca", 123456798), 
        (2, "Tuesday", "10:00", 1, 3, "i.d@ucalgary.ca", 123456798), 
        (3, "Friday", "8:00", 1, 3, "i.d@ucalgary.ca", 123456798);
        
INSERT INTO ROOMS
VALUES (1, "Monday" , "1:00"),
        (1, "Tuesday", "1:00"), 
        (2, "Monday", "1:00");
        
SELECT * FROM ROOMS