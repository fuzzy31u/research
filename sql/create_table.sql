-- drop table
DROP TABLE IF EXISTS image;
DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS result_like;
DROP TABLE IF EXISTS result_ratio;
DROP TABLE IF EXISTS hit_study_ratio;
DROP TABLE IF EXISTS hit_analized_ratio;

-- create table
CREATE TABLE image(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       genre_id INT NOT NULL,
       file_name VARCHAR(64) NOT NULL
) CHARSET=utf8;

CREATE TABLE history(
       image_id INT NOT NULL,
       user_id INT NOT NULL,
       genre_id INT NOT NULL,
       shown_flg TINYINT(1) NOT NULL DEFAULT 0
) CHARSET=utf8;

CREATE TABLE user(
       id INT NOT NULL PRIMARY KEY,
       name VARCHAR(64) NOT NULL
) CHARSET=utf8;

CREATE TABLE genre(
       id INT NOT NULL PRIMARY KEY,
       name VARCHAR(32) NOT NULL
) CHARSET=utf8;

CREATE TABLE result_like(
       image_id INT NOT NULL PRIMARY KEY,
       user_id INT NOT NULL,
       genre_id INT NOT NULL
) CHARSET=utf8;

CREATE TABLE result_ratio(
       genre_id INT NOT NULL PRIMARY KEY,
       user_id INT NOT NULL,
       ratio FLOAT NOT NULL,
       normalisation_ratio FLOAT NOT NULL
) CHARSET=utf8;

CREATE TABLE hit_study_ratio(
       user_id INT NOT NULL PRIMARY KEY,
       like_cnt INT NOT NULL DEFAULT 0,
       ratio FLOAT NOT NULL
) CHARSET=utf8;

CREATE TABLE hit_analized_ratio(
       user_id INT NOT NULL PRIMARY KEY,
       like_cnt INT NOT NULL DEFAULT 0,
       ratio FLOAT NOT NULL
) CHARSET=utf8;
