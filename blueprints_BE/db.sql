DROP DATABASE IF EXISTS mydb;
CREATE DATABASE mydb;


CREATE TABLE users (
	role_id BIGSERIAL PRIMARY KEY,
	role_name TEXT UNIQUE NOT NULL
);

INSERT INTO users (role_name) VALUES ('translator'),('project_admin'),('super_admin');

CREATE TABLE users (
	user_id BIGSERIAL PRIMARY KEY, 
	public_id TEXT UNIQUE NOT NULL,
	email TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	role_id BIGINT REFERENCES roles(role_id) NOT NULL,
	created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP(2), 
	updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP(2) 
);