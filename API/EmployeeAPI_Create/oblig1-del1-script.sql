--
-- Table structure for table `dept`
--
START TRANSACTION;

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `deptno` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(100) DEFAULT NULL,
  `loc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`deptno`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dept`
--
LOCK TABLES `dept` WRITE;
INSERT INTO `dept` VALUES 
(1,'Accounting','New York'),
(2,'Research','Dallas'),
(3,'Sales','Chicago'),
(4,'Operations','Boston');
UNLOCK TABLES;

--
-- Table structure for table `emp`
--
DROP TABLE IF EXISTS `emp`;
CREATE TABLE `emp` (
  `empno` int NOT NULL AUTO_INCREMENT,
  `ename` varchar(100) DEFAULT NULL,
  `job` varchar(100) DEFAULT NULL,
  `mgr` int DEFAULT NULL,
  `hiredate` DATETIME NULL DEFAULT NULL ,
  `sal` float DEFAULT NULL,
  `comm` float DEFAULT NULL,
  `deptno` int DEFAULT NULL,
  PRIMARY KEY (`empno`)
) ENGINE=InnoDB AUTO_INCREMENT=7935 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp`
--
LOCK TABLES `emp` WRITE;
INSERT INTO `emp` VALUES 
(7369,'Smith','Clerk',7902,'1980-12-17 00:00:00',800,NULL,2),
(7499,'Allen','Salesman',7698,'1981-02-20 00:00:00',1600,300,3),
(7521,'Ward','Salesman',7698,NULL ,1250,500,3),
(7566,'Jones','Manager',7839,NULL ,2975,NULL,2),
(7654,'Martin','Salesman',7698,NULL ,1250,1400,3),
(7698,'Blake','Manager',7839,NULL ,2850,NULL,3),
(7782,'Clark','Manager',7839,NULL ,2450,NULL,1),
(7788,'Scott','Analyst',7566,NULL ,3000,NULL,2),
(7839,'King','President',NULL,NULL ,5000,NULL,1),
(7844,'Turner','Salesman',7698,NULL ,1500,0,3),
(7876,'Adams','Clerk',7788,NULL ,1100,NULL,2),
(7900,'James','Clerk',7698,NULL ,950,NULL,3),
(7902,'Ford','Analyst',7566,NULL ,3000,NULL,2),
(7934,'Miller','Clerk',7782,NULL ,1300,NULL,1);
UNLOCK TABLES;
COMMIT;

