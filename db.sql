CREATE TABLE users (
	id INT auto_increment NOT NULL,
	username varchar(255) NOT NULL COMMENT '用户名',
	password varchar(100) NOT NULL COMMENT '非明文密码',
	mobile varchar(11) NOT NULL,
	email varchar(32) NOT NULL,
	avatar_url varchar(256) NULL COMMENT '用户头像',
	gender INT DEFAULT 0 NULL COMMENT '性别',
	is_active BOOL DEFAULT true NULL COMMENT '有效用户',
	last_login DATETIME NULL COMMENT '最近登录时间',
	create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
	update_time DATETIME NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


--root $2b$12$ikylDV/B0rfwFAO1Bp0PZOfO1Ov41f2av1jR6PQYF.LffFB2T3OM6
