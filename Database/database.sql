drop table if exists country;
create table country(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    Aname text not null
);

drop table if exists author;
create table author(
    id integer primary key AUTOINCREMENT,
    country_id integer,
    Aname text not null
);


drop table if exists book;
create table book(
    id integer primary key AUTOINCREMENT,
    author_id integer,
    title text not null,
    isbn text
);