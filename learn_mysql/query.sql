use awesome;
-- drop table  users;
-- select * from Users;
-- DELETE FROM users where name like'GpYnu
-- show tables;
-- DESC test;

-- 增删改语句都很容易理解和掌握
-- INSERT into test (id) VALUES 
-- ('001'),
-- ('002');

-- UPDATE test 
-- set id='111'
-- where id='001';

-- DELETE FROM  test 
-- where `id`='002';

-- % 匹配长度>=0的任意字符串
-- SELECT id,email,name,created_at
-- insert into blogs (id,user_id='000',user_name) VALUES
-- ('111'),
-- ('123'),
-- ('456');


select 
u.name uname,
u.email,
b.name bname,
b.content bcontent

-- users.id uid ,
-- blogs.id bid
from users u,blogs b,users_blogs ub
where u.id=ub.uid and b.id=ub.bid



-- where  id like '%2'
-- order by id
-- group by id
-- limit 3 OFFSET 6







;


-- select *
-- from users;

-- drop table users,blogs;
-- select * from users;