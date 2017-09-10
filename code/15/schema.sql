drop table if exists entries;
create table todos (
  id integer primary key autoincrement,
  task text not null
);