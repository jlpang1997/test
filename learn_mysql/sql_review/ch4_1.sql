drop database if EXISTS practice;
create database practice;
use practice;

-- -- grant select, insert, update, delete on practice.* to 'jlpang'@'localhost' identified by 'jlpang';



drop table if EXISTS student;
create table student(
    sno int PRIMARY key,
    sname varchar(10) unique not null,
    sex char(1),
    check(sex in ('M','F')) -- 并没有作用 靠
);
drop table if EXISTS course;
create table course(
    cno int PRIMARY KEY AUTO_INCREMENT,
    cname varchar(50)
);
drop table if EXISTS select_course;
create table select_course(
    sno int ,
    cno int,
    PRIMARY key(sno,cno),
    FOREIGN key(sno) REFERENCES student(sno)
    on update cascade
    on delete cascade,
    FOREIGN key(cno) REFERENCES course(cno)
    on update cascade
    on delete cascade
);
insert into student 
value(1,'ming','M');

insert into course 
value(5,'cs');

insert into select_course
value(1,5);
select * from student;
select * from course;
select * from select_course;
select 
s.sname,
c.cname
from student s,course c,select_course sc 
where s.sno=sc.sno and c.cno=sc.cno;
