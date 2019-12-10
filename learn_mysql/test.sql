use test;
-- 反引号是为了区分sql的关键字和保留字
drop table if EXISTS student;
CREATE TABLE `student` (
  `s_id` varchar(40) NOT NULL,
  `s_name` varchar(255) default NULL,
  `s_age` varchar(255) default NULL,
  `s_msg` varchar(255) default NULL,
  PRIMARY KEY  (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
-- -- ----------------------------
-- -- Records of student
-- -- ----------------------------
INSERT INTO `student` VALUES ('1', '早晨', '22', '电风扇');
INSERT INTO `student` VALUES ('2', '春节', '32', '发电设备');
INSERT INTO `student` VALUES ('3', '端午节', '33', '地方');
INSERT INTO `student` VALUES ('4', '清明节', '44', 'dfs ');
INSERT INTO `student` VALUES ('5', '圣诞节', '66', '的');

select * from student;

