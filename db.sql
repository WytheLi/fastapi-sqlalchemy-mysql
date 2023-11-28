CREATE TABLE users (
	id INT auto_increment NOT NULL,
	username varchar(255) NOT NULL COMMENT '用户名',
	password varchar(100) NOT NULL COMMENT '非明文密码',
	mobile varchar(11) NOT NULL,
	email varchar(32) NOT NULL,
	avatar_url varchar(256) NULL COMMENT '用户头像',
	gender INT DEFAULT 0 NULL COMMENT '性别',
	is_active BOOL DEFAULT true NULL COMMENT '有效用户',
	is_admin BOOL DEFAULT true NULL COMMENT '管理员用户',
	last_login DATETIME NULL COMMENT '最近登录时间',
	create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
	update_time DATETIME NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


CREATE TABLE category (
	id INT auto_increment NOT NULL,
	name varchar(8) NULL COMMENT '分类名称',
	CONSTRAINT category_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


CREATE TABLE news (
	id INT auto_increment NOT NULL,
	title varchar(64) NOT NULL COMMENT '新闻标题',
	source varchar(16) NOT NULL COMMENT '新闻来源',
	digest varchar(32) NOT NULL COMMENT '新闻摘要',
	content TEXT NOT NULL COMMENT '新闻内容',
	pageviews INT DEFAULT 0 NULL COMMENT '浏览量',
	image_url TEXT NULL COMMENT '新闻列表图片路径',
	category_id INT NULL,
	user_id INT NULL,
	status INT DEFAULT 0 NULL COMMENT '当前新闻状态。如果为1代表审核通过，0代表审核中，-1代表审核不通过',
	reason varchar(256) NULL COMMENT '未通过原因，status = -1 的时候使用',
	CONSTRAINT news_PK PRIMARY KEY (id),
	CONSTRAINT news_FK FOREIGN KEY (category_id) REFERENCES category(id),
	CONSTRAINT news_FK_1 FOREIGN KEY (user_id) REFERENCES users(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


CREATE TABLE comment (
	id INT auto_increment NOT NULL,
	user_id INT NOT NULL,
	news_id INT NOT NULL,
	content TEXT NOT NULL COMMENT '评论内容',
	parent_id INT NULL COMMENT '自关联，父id',
	up_count INT DEFAULT 0 NULL COMMENT '点赞条数',
	CONSTRAINT comment_PK PRIMARY KEY (id),
	CONSTRAINT comment_FK FOREIGN KEY (user_id) REFERENCES users(id),
	CONSTRAINT comment_FK_1 FOREIGN KEY (news_id) REFERENCES news(id),
	CONSTRAINT comment_FK_2 FOREIGN KEY (parent_id) REFERENCES comment(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci
COMMENT='评论';


CREATE TABLE comment_user_up_rel (
	comment_id INT NULL,
	user_id INT NULL,
	id INT auto_increment NOT NULL,
	CONSTRAINT comment_user_up_rel_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci
COMMENT='评论点赞';


CREATE TABLE user_collection_rel (
	id INT auto_increment NOT NULL,
	user_id INT NOT NULL,
	news_id INT NOT NULL,
	create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
	CONSTRAINT user_collection_rel_PK PRIMARY KEY (id, user_id, news_id),
	CONSTRAINT user_collection_rel_FK FOREIGN KEY (user_id) REFERENCES users(id),
	CONSTRAINT user_collection_rel_FK_1 FOREIGN KEY (news_id) REFERENCES news(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;


CREATE TABLE user_follower_rel (
	id INT auto_increment NOT NULL,
	follower_id INT NOT NULL,
	followed_id INT NOT NULL,
	create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
	CONSTRAINT user_follower_rel_PK PRIMARY KEY (id, follower_id, followed_id),
	CONSTRAINT user_follower_rel_FK FOREIGN KEY (follower_id) REFERENCES users(id),
	CONSTRAINT user_follower_rel_FK_1 FOREIGN KEY (followed_id) REFERENCES users(id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
