DROP TABLE IF EXISTS `film`;
CREATE TABLE `film` (
`fnr` int NOT NULL AUTO_INCREMENT,
`tittel` varchar(50) DEFAULT NULL,
`år` int DEFAULT NULL,
`land` varchar(50) default null,
`sjanger` varchar(50) default null,
`alder` int default null,
`tid` int default null,
`pris` decimal(6,2) default null,
PRIMARY KEY (`fnr`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

INSERT INTO `film` VALUES 
(1, 'Casablanca', '1942', 'USA', 'Drama', 15, 102, 149), 
(2, 'Fort Apache', '1948', 'USA', 'Western', 15, 127, null), 
(3, 'Apocalypse Now', '1979', 'USA', 'Action', 18, 155, 123), 
(4, 'Streets of Fire', '1984', 'USA', 'Action', 15, 93, null), 
(5, 'High Noon', '1952', 'USA', 'Western', 15, 85, 123), 
(6, 'Cinema Paradiso', '1988', 'Italia', 'Komedie', 11, 123, null), 
(7, 'Asterix hos Britene', '1988', 'Frankrike', 'Tegnefilm', 7, 78, 149), 
(8, 'Veiviseren', '1987', 'Norge', 'Action', 15, 96, 87), 
(9, 'Salmer fra kjøkkenet', '2002', 'Norge', 'Komedie', 7, 80, 149), 
(10, 'Anastasia', '1997', 'USA', 'Tegnefilm', 7, 94, 123), 
(11, 'La Grande bouffe', '1973', 'Frankrike', 'Drama', 15, 129, 87), 
(12, 'Blues Brothers 2000', '1998', 'USA', 'Komedie', 11, 124, 135), 
(13, 'Beatles: Help', '1965', 'Storbritannia', 'Musikk', 11, 144, null);