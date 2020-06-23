DROP TABLE IF EXISTS 用户权限;/*SQL@Run*//*SkipError*/
CREATE TABLE 用户权限(
    User_Id VARCHAR(32) NOT NULL   COMMENT '用户名' ,
    Authorization_level INT    COMMENT '用户权限' ,
    PRIMARY KEY (User_id)
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 用户权限 COMMENT 'undefined';/*SQL@Run*/
DROP TABLE IF EXISTS 用户信息;/*SQL@Run*//*SkipError*/
CREATE TABLE 用户信息(
    User_Id VARCHAR(32) NOT NULL   COMMENT '用户名' ,
    Password VARCHAR(32) NOT NULL   COMMENT '密码' ,
    Authorization_level INT    COMMENT '用户权限' ,
    PRIMARY KEY (User_id)
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 用户信息 COMMENT 'undefined';/*SQL@Run*/
DROP TABLE IF EXISTS 学生;/*SQL@Run*//*SkipError*/
CREATE TABLE 学生(
    Student_Id VARCHAR(32) NOT NULL   COMMENT '学号' ,
    Student_Name VARCHAR(32)    COMMENT '姓名' ,
    Student_Sex VARCHAR(32)    COMMENT '性别' ,
    Student_Class VARCHAR(32)    COMMENT '班级' ,
    PRIMARY KEY (Student_Id)
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 学生 COMMENT 'undefined';/*SQL@Run*/
DROP TABLE IF EXISTS  教师;/*SQL@Run*//*SkipError*/
CREATE TABLE 教师(
    Teacher_Id VARCHAR(32) NOT NULL   COMMENT '工号' ,
    Teacher_Name VARCHAR(32)    COMMENT '姓名' ,
    Teacher_Sex VARCHAR(32)    COMMENT '性别' ,
    Teacher_Age INT    COMMENT '年龄' ,
    Teacher_Subject VARCHAR(32)    COMMENT '科目' ,
    PRIMARY KEY (Teacher_Id)
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 教师 COMMENT 'undefined';/*SQL@Run*/
DROP TABLE IF EXISTS  课程;/*SQL@Run*//*SkipError*/
CREATE TABLE 课程(
    Course_Id VARCHAR(32) NOT NULL   COMMENT '课程号' ,
    Course_Name VARCHAR(32)    COMMENT '课程名' ,
    Course_Credit INT    COMMENT '学分' ,
    Teacher_Name VARCHAR(32)    COMMENT '教师' ,
    PRIMARY KEY (Course_Id)
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 课程 COMMENT 'undefined';/*SQL@Run*/
DROP TABLE IF EXISTS  选课;/*SQL@Run*//*SkipError*/
CREATE TABLE 选课(
    Student_Id VARCHAR(32)    COMMENT '学号' ,
    Student_Name VARCHAR(32)    COMMENT '姓名' ,
    Course_Id VARCHAR(32)    COMMENT '课程号' ,
    Course_Name VARCHAR(32)    COMMENT '课程名' ,
    Teacher_Name VARCHAR(32)    COMMENT '教师' 
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 选课 COMMENT 'undefined';/*SQL@Run*/
DROP TABLE IF EXISTS  成绩;/*SQL@Run*//*SkipError*/
CREATE TABLE 成绩(
    Student_Id VARCHAR(32)    COMMENT '学号' ,
    Student_Name VARCHAR(32)    COMMENT '姓名' ,
    Class_Id VARCHAR(32)    COMMENT '课程号' ,
    Class_Name VARCHAR(32)    COMMENT '课程名' ,
    Score INT    COMMENT '成绩' 
) COMMENT = ' ';/*SQL@Run*/

ALTER TABLE 成绩 COMMENT 'undefined';/*SQL@Run*/
