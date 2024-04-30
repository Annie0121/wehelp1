## task2

[task2](task2.png)
```
create table member(  
 `id`  bigint primary key AUTO_INCREMENT  comment'Unique ID',  
 `name`  varchar(255) not null comment'Name',  
 `username` varchar(255) not null  comment'Username',  
  `password` varchar(255) not null comment'Password',  
  `follower_count` int unsigned not null default 0 comment'Follower Count',  
  `time` datetime not null default now() comment'Signup Time'  
  
)
 ``` 
  
  

## task3

task3-1
```
insert into member(name,username,password) values   
('test','test','test'),  
('test-2','qwe','123'),  
('test-3','qwe','456'),  
('test-4','qwe','789'),  
('test-5','asd','123') ;
 ```

[task3-2](task3r2.png)  
```
SELECT * FROM member;
```

[task3-3](task3r3.png)  
```
SELECT * FROM member order by time;
```  

[task3-4](task3r4.png)  
```
SELECT * FROM member order by time limit 1,3;
```  

[task3-5](task3r5.png)  
```
SELECT * FROM member where username='test';
```  

[task3-6](task3r6.png)  
```
SELECT * FROM member where name like '%es%';
```  

[task3-7](task3r7.png)  
```
SELECT * FROM member where username='test' and password='test';
```

[task3-8](task3r8.png)  
```
UPDATE member SET name = 'test2' WHERE username='test';
SELECT * FROM member;
```
    
    
## task4
[task4-1](task4r1.png)  
```
SELECT COUNT(*) FROM member;
```  
  
[task4-2](task4r2.png)  
```
SELECT SUM(follower_count) FROM member;  
```
  
[task4-3](task4r3.png)  
```
SELECT AVG(follower_count) FROM member; 
``` 

[task4-4](task4r4.png)  
```
SELECT AVG(follower_count) FROM  (SELECT follower_count FROM member  order by follower_count desc limit 2) AS follower_count_AVG;  
```  
  
  
## task5
[task5-1](task5r1.png)  
```
create table message(  
	id bigint primary key auto_increment  comment'Unique ID',  
    member_id bigint not null comment'Member ID for Message Sender',  
    content varchar(255) not null comment'ContentD',  
    like_count int unsigned not null default  0 comment'Like Count',  
    time datetime not null default  now() comment'Publish Time'  
);  

alter table message add foreign key(member_id) references `member`(id);  

desc message;  
```
[task5-2](task5r2.png) 
```
insert into message(member_id,content,like_count) values(1,'hello',1),(2,'hello2',2),(3,'hello3',3),(4,'hello4',4),(5,'hello5',5) ;

select * from message,member where member.id = message.member_id ;
```
[task5-3](task5r3.png) 
```
select message.* ,member.* from message left outer join member on member.id = message.member_id where username='test';
```
[task5-4](task5r4.png) 
```
select avg(like_count) from message  join member on member.id = message.member_id where username='test';
```
[task5-5](task5r5.png)  
```
select username,avg(like_count) from message join member on member.id = message.member_id group by username;
```