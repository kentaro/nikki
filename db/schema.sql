create table if not exists login_user (
    login_id int unsigned auto_increment,
    login_name varchar(255) not null,
    password varchar(255) not null,
    email varchar(255) not null,

    primary key (login_id),
    key (login_name, password)
);

create table if not exists entry (
    entry_id int unsigned auto_increment,
    login_id int unsigned not null,
    entry_text varchar(255) not null,

    primary key (entry_id)
);
