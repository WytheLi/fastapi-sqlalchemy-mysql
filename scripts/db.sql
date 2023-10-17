CREATE TABLE fastapi_demo.users (
	id INT auto_increment NOT NULL,
	username varchar(8) NOT NULL,
	password varchar(255) NULL,
	is_active BOOL DEFAULT true NOT NULL,
	last_login DATETIME NULL,
	create_time DATETIME NULL,
	update_time DATETIME NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

--root $2b$12$ikylDV/B0rfwFAO1Bp0PZOfO1Ov41f2av1jR6PQYF.LffFB2T3OM6
