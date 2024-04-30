create database website;
use website;
create table member(
 `id`  bigint primary key AUTO_INCREMENT  comment'Unique ID',
 `name`  varchar(255) not null comment'Name',
 `username` varchar(255) not null  comment'Username',
  `password` varchar(255) not null comment'Password',
  `follower_count` int unsigned not null default 0 comment'Follower Count',
  `time` datetime not null default now() comment'Signup Time'

);

desc member;

-- task3 r1
insert into member(name,username,password) values 
('test','test','test'),
('test-2','qwe','123'),
('test-3','qwe','456'),
('test-4','qwe','789'),
('test-5','asd','123') ;


-- task3 r2
SELECT * FROM member;

-- task3 r3
SELECT * FROM member order by time;

-- task3 r4
SELECT * FROM member order by time limit 1,3;

-- task3 r5
SELECT * FROM member where username='test';

-- task3 r6
SELECT * FROM member where name like '%es%';

-- task3 r7
SELECT * FROM member where username='test' and password='test';

-- task3 r8
UPDATE member SET name = 'test2' WHERE username='test';
SELECT * FROM member;

-- task4 r1
SELECT COUNT(*) FROM member;

-- task4 r2
SELECT SUM(follower_count) FROM member;
-- task4 r3
SELECT AVG(follower_count) FROM member;

-- task4 r4

SELECT AVG(follower_count) FROM  (SELECT follower_count FROM member  order by follower_count desc limit 2) AS follower_count_AVG;


-- task 5 r1
create table message(
	id bigint primary key auto_increment  comment'Unique ID',
    member_id bigint not null comment'Member ID for Message Sender',
    content varchar(255) not null comment'ContentD',
    like_count int unsigned not null default  0 comment'Like Count',
    time datetime not null default  now() comment'Publish Time'
);
alter table message add foreign key(member_id) references `member`(id);
desc message;

-- task 5 r2
insert into message(member_id,content,like_count) values(1,'hello',1),(2,'hello2',2),(3,'hello3',3),(4,'hello4',4),(5,'hello5',5) ;
select * from message,member where member.id = message.member_id ;

-- task5 task 3

select message.* ,member.* from message left outer join member on member.id = message.member_id where username='test';

-- task 5 r4
select avg(like_count) from message  join member on member.id = message.member_id where username='test';

-- task5 r5
select username,avg(like_count) from message join member on member.id = message.member_id group by username;