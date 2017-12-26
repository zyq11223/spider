/*Table structure for table `online_retail_products_data_sears_bike` */


CREATE TABLE `online_retail_products_data_bhphotovides_bike` (
  `id` varchar(255) NOT NULL,
  `domain_name` varchar(72) DEFAULT NULL COMMENT '根网址',
  `keyword` varchar(72) DEFAULT NULL COMMENT '四种类型：手机、电视机、自行车、相机，每种类型800条以上，至少爬5个网站',
  `url` text COMMENT '具体网页',
  `title` text COMMENT '网页标题',
  `doc` longtext COMMENT '网页内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `online_retail_products_data_sears_camera` */

CREATE TABLE `online_retail_products_data_bhphotovides_camera` (
  `id` varchar(255) NOT NULL,
  `domain_name` varchar(72) DEFAULT NULL COMMENT '根网址',
  `keyword` varchar(72) DEFAULT NULL COMMENT '四种类型：手机、电视机、自行车、相机，每种类型800条以上，至少爬5个网站',
  `url` text COMMENT '具体网页',
  `title` text COMMENT '网页标题',
  `doc` longtext COMMENT '网页内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `online_retail_products_data_sears_labtop` */


CREATE TABLE `online_retail_products_data_bhphotovides_labtop` (
  `id` varchar(255) NOT NULL,
  `domain_name` varchar(72) DEFAULT NULL COMMENT '根网址',
  `keyword` varchar(72) DEFAULT NULL COMMENT '四种类型：手机、电视机、自行车、相机，每种类型800条以上，至少爬5个网站',
  `url` text COMMENT '具体网页',
  `title` text COMMENT '网页标题',
  `doc` longtext COMMENT '网页内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `online_retail_products_data_sears_phone` */


CREATE TABLE `online_retail_products_data_bhphotovides_phone` (
  `id` varchar(255) NOT NULL,
  `domain_name` varchar(72) DEFAULT NULL COMMENT '根网址',
  `keyword` varchar(72) DEFAULT NULL COMMENT '四种类型：手机、电视机、自行车、相机，每种类型800条以上，至少爬5个网站',
  `url` text COMMENT '具体网页',
  `title` text COMMENT '网页标题',
  `doc` longtext COMMENT '网页内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `online_retail_products_data_sears_tv` */

CREATE TABLE `online_retail_products_data_bhphotovides_tv` (
  `id` varchar(255) NOT NULL,
  `domain_name` varchar(72) DEFAULT NULL COMMENT '根网址',
  `keyword` varchar(72) DEFAULT NULL COMMENT '四种类型：手机、电视机、自行车、相机，每种类型800条以上，至少爬5个网站',
  `url` text COMMENT '具体网页',
  `title` text COMMENT '网页标题',
  `doc` longtext COMMENT '网页内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;