-- DROP database desafioweb;
CREATE DATABASE desafioweb;

use desafioweb;

create table contato (id_conta int auto_increment primary key,
email varchar(255) not null,
assunto varchar(255) not null,
descricao varchar(255) not null);