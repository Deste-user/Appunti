DROP TABLE IF EXISTS Workers;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS flags;

-- non ho tutta sta voglia di inserire altre tabelle
CREATE TABLE Workers (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       firstname TEXT NOT NULL,
       lastname TEXT NOT NULL
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE flags(
    flag TEXT NOT NULL
);

INSERT INTO flags(flag)
VALUES('SEI UN CONTRABBANDIEROS/2 ;-) ,ADESSO TI MANCA DA ASCOLTARE 4000 VOLTE SQUALO73');

INSERT INTO users (username, password, role)
VALUES ('admin', 'admin_password', 'admin');
