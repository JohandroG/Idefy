CREATE DATABASE idefy;

USE idefy;

CREATE TABLE users(
user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
username VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
user_password varchar(250) NOT NULL,
created_at DATE NOT NULL,
updated_at DATETIME NOT NULL
);

INSERT INTO users(id,first_name,last_name,email,user_password,created_at,updated_at)
VALUES 
(1,'John', 'Ramirez','Johnsito55','johnr@gmail.com','john123',SYSDATE(),SYSDATE() );


CREATE TABLE ideas(
idea_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
idea_info VARCHAR(900) NOT NULL,
likes INT NOT NULL
category VARCHAR(100) NOT NULL,
created_at DATE NOT NULL,
updated_at DATETIME NOT NULL 
);

-- INSERT INTO ideas(idea_id,idea_info,likes,created_at,updated_at)
-- VALUES 
-- (1,'something',0, SYSDATE(),SYSDATE() );

CREATE TABLE categories(
    category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATETIME NOT NULL 
);

CREATE TABLE idefy_references(
thogether_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL, 
FOREIGN KEY (user_id) REFERENCES users(user_id) ,
idea_id INT NOT NULL,
FOREIGN KEY (idea_id) REFERENCES ideas(idea_id),
category_id INT NOT NULL,
FOREIGN KEY (category_id) REFERENCES categories(category_id),
liker_id INT,
);


