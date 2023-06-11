DROP TABLE CONTACT;
DROP TABLE UTIL;

CREATE TABLE UTIL(
    id_util SERIAL UNIQUE primary key,
    login varchar(20),
    mdp varchar(20)
);
CREATE TABLE CONTACT(
    id_contact SERIAL UNIQUE primary key,
    nom varchar(100),
    email varchar(100),
    telephone varchar(10),
    adresse varchar(100),
    id_util smallint references UTIL(id_util),
    lat real,
    lon real

);
INSERT INTO UTIL(login, mdp) VALUES('root','root');
INSERT INTO UTIL(login, mdp) VALUES('user','user');