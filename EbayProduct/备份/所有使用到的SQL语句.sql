38764
31714

SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'ebay' AND mark = 'tv';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'ebay' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'ebay' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'ebay' AND mark = 'camera';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'ebay' AND mark = 'bike';

SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'dealigg' AND mark = 'tv';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'dealigg' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'dealigg' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'dealigg' AND mark = 'camera';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'dealigg' AND mark = 'bike';

SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'bhphotovideo' AND mark = 'tv'; # 多了100
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'bhphotovideo' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'bhphotovideo' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'bhphotovideo' AND mark = 'camera';

SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'cdiscount' AND mark = 'tv'; # 多了100
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'cdiscount' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'cdiscount' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data_unique WHERE site = 'cdiscount' AND mark = 'camera';

SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'macmall' AND mark = 'tv'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'macmall' AND mark = 'phone'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'macmall' AND mark = 'laptop'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'macmall' AND mark = 'camera'; #

SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'ebuyer' AND mark = 'tv'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'ebuyer' AND mark = 'phone'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'ebuyer' AND mark = 'laptop'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'ebuyer' AND mark = 'camera'; #
SELECT COUNT(url) FROM ywx_product_data_unique WHERE site = 'ebuyer' AND mark = 'bike'; #


INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebay_bike;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebay_camera;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebay_labtop;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebay_phone;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebay_tv;# ok

INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_dealigg_bike;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_dealigg_camera;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_dealigg_labtop;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_dealigg_phone;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_dealigg_tv;# ok

INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_bhphotovides_labtop;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_bhphotovides_camera;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_bhphotovides_phone;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_bhphotovides_tv;# ok

INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebuyer_camera;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebuyer_phone;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebuyer_tv;# ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_ebuyer_bike;# ok

INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_cdiscount_labtop; # ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_cdiscount_camera; # ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_cdiscount_phone; # ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_cdiscount_tv; # ok

INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_marcmall_camera; # ok 1301
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, domain_name, keyword, url FROM online_retail_products_data_marmall_tv; # ok
INSERT INTO ywx_product_data(id, site, mark,url) SELECT id, site, mark, url  FROM online_retail_products_data_marcmall_labtop; # ok

SELECT COUNT(*) FROM ywx_single_url;
SELECT COUNT(*) FROM ywx_product_data;
SELECT DISTINCT(url) FROM ywx_product_data;
SELECT * FROM ywx_product_data WHERE url NOT IN (SELECT url FROM ywx_single_url);

SELECT DISTINCT(mark) FROM ywx_product_data WHERE site = ' http://www.ebay.com';
SELECT * FROM ywx_product_data WHERE site = ' http://www.ebay.com';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'LED tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'laptop core i';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'DSLR camera';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'bike';
UPDATE ywx_product_data SET mark = 'tv' WHERE site = ' http://www.ebay.com' AND mark = 'LED tv';
UPDATE ywx_product_data SET mark = 'phone'  WHERE site = ' http://www.ebay.com' AND mark = 'phone';
UPDATE ywx_product_data SET mark = 'laptop' WHERE site = ' http://www.ebay.com' AND mark = 'laptop core i';
UPDATE ywx_product_data SET mark = 'camera' WHERE site = ' http://www.ebay.com' AND mark = 'DSLR camera';
UPDATE ywx_product_data SET mark = 'bike'  WHERE site = ' http://www.ebay.com' AND mark = 'bike';
UPDATE ywx_product_data SET site = 'ebay' WHERE site = ' http://www.ebay.com';
SELECT * FROM ywx_product_data WHERE site = 'ebay';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'ebay' AND mark = 'tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'ebay' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'ebay' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'ebay' AND mark = 'camera';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'ebay' AND mark = 'bike';
#delete from  ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'LED tv';
#delete from  ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'phone';
#delete from  ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'laptop core i';
#delete from  ywx_product_data WHERE site = ' http://www.ebay.com' AND mark = 'DSLR camera';
#delete from  ywx_product_data  WHERE site = ' http://www.ebay.com' AND mark = 'bike';

SELECT DISTINCT(mark) FROM ywx_product_data WHERE site = ' http://www.dealigg.com';
SELECT * FROM ywx_product_data WHERE site = ' http://www.dealigg.com';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'LED tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'phone 4g';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'Laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'digital camera';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'bike';
UPDATE ywx_product_data SET mark = 'tv' WHERE site = ' http://www.dealigg.com' AND mark = 'LED tv';
UPDATE ywx_product_data SET mark = 'phone'  WHERE site = ' http://www.dealigg.com' AND mark = 'phone 4g';
UPDATE ywx_product_data SET mark = 'laptop' WHERE site = ' http://www.dealigg.com' AND mark = 'Laptop';
UPDATE ywx_product_data SET mark = 'camera' WHERE site = ' http://www.dealigg.com' AND mark = 'digital camera';
UPDATE ywx_product_data SET mark = 'bike'  WHERE site = ' http://www.dealigg.com' AND mark = 'bike';
UPDATE ywx_product_data SET site = 'dealigg' WHERE site = ' http://www.dealigg.com';
SELECT * FROM ywx_product_data WHERE site = 'dealigg';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'dealigg' AND mark = 'tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'dealigg' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'dealigg' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'dealigg' AND mark = 'camera';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'dealigg' AND mark = 'bike';
#delete from  ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'LED tv';
#delete from  ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'phone';
#delete from  ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'laptop core i';
#delete from  ywx_product_data WHERE site = ' http://www.dealigg.com' AND mark = 'DSLR camera';
#delete from  ywx_product_data  WHERE site = ' http://www.dealigg.com' AND mark = 'bike';

SELECT DISTINCT(mark) FROM ywx_product_data WHERE site = ' https://www.bhphotovideo.com';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'LED tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'Laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'camera';
UPDATE ywx_product_data SET mark = 'tv' WHERE site = ' https://www.bhphotovideo.com' AND mark = 'LED tv'; # ok
UPDATE ywx_product_data SET mark = 'phone'  WHERE site = ' https://www.bhphotovideo.com' AND mark = 'phone';
UPDATE ywx_product_data SET mark = 'laptop' WHERE site = ' https://www.bhphotovideo.com' AND mark = 'Laptop';
UPDATE ywx_product_data SET mark = 'camera' WHERE site = ' https://www.bhphotovideo.com' AND mark = 'camera ';
UPDATE ywx_product_data SET site = 'bhphotovideo' WHERE site = ' https://www.bhphotovideo.com';
SELECT * FROM ywx_product_data WHERE site = 'bhphotovideo';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'tv'; # 多了100
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'camera';

SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'tv'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'phone'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'laptop'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'bhphotovideo' AND mark = 'camera'; #
#delete from  ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'LED tv';
#delete from  ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'phone';
#delete from  ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'laptop core i';
#delete from  ywx_product_data WHERE site = ' https://www.bhphotovideo.com' AND mark = 'DSLR camera';

SELECT DISTINCT(mark) FROM ywx_product_data WHERE site = ' https://www.cdiscount.com';
SELECT * FROM ywx_product_data WHERE site = ' http://www.www.cdiscount.com';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.cdiscount.com' AND mark = 'tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.cdiscount.com' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.cdiscount.com' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.cdiscount.com' AND mark = 'camera';
UPDATE ywx_product_data SET mark = 'tv' WHERE site = ' http://www.www.cdiscount.com' AND mark = 'tv';
UPDATE ywx_product_data SET mark = 'phone'  WHERE site = ' http://www.www.cdiscount.com' AND mark = 'phone';
UPDATE ywx_product_data SET mark = 'laptop' WHERE site = ' http://www.www.cdiscount.com' AND mark = 'laptop';
UPDATE ywx_product_data SET mark = 'camera' WHERE site = ' http://www.www.cdiscount.com' AND mark = 'camera';
UPDATE ywx_product_data SET site = 'cdiscount' WHERE site = ' http://www.www.cdiscount.com';
SELECT * FROM ywx_product_data WHERE site = 'cdiscount';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'tv'; # 多了100
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'camera';

SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'tv'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'phone'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'laptop'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'cdiscount' AND mark = 'camera'; #
#delete from  ywx_product_data WHERE site = ' http://www.cdiscount.com' AND mark = 'LED tv';
#delete from  ywx_product_data WHERE site = ' http://www.cdiscount.com' AND mark = 'phone';
#delete from  ywx_product_data WHERE site = ' http://www.cdiscount.com' AND mark = 'laptop core i';
#delete from  ywx_product_data WHERE site = ' http://www.cdiscount.com' AND mark = 'DSLR camera';
#delete from  ywx_product_data  WHERE site = ' http://www.cdiscount.com' AND mark = 'bike';

SELECT DISTINCT(mark) FROM ywx_product_data WHERE site = ' http://www.macmall.com';
SELECT * FROM ywx_product_data WHERE site = ' http://www.macmall.com';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'LED TV';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'Laptop';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'camera';
UPDATE ywx_product_data SET mark = 'tv'  WHERE site = ' http://www.macmall.com' AND mark = 'LED TV';
UPDATE ywx_product_data SET mark = 'laptop' WHERE site = ' http://www.macmall.com' AND mark = 'Laptop';
UPDATE ywx_product_data SET mark = 'camera' WHERE site = ' http://www.macmall.com' AND mark = 'camera';
UPDATE ywx_product_data SET site = 'macmall' WHERE site = ' http://www.macmall.com';
SELECT * FROM ywx_product_data WHERE site = 'macmall';
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'macmall' AND mark = 'tv'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'macmall' AND mark = 'phone'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'macmall' AND mark = 'laptop'; #
SELECT DISTINCT(url) FROM ywx_product_data WHERE site = 'macmall' AND mark = 'camera'; #
#delete from  ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'LED tv';
#delete from  ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'phone';
#delete from  ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'laptop core i';
#delete from  ywx_product_data WHERE site = ' http://www.macmall.com' AND mark = 'DSLR camera';
#delete from  ywx_product_data  WHERE site = ' http://www.macmall.com' AND mark = 'bike';

SELECT DISTINCT(mark) FROM ywx_product_data WHERE site = ' https://www.bhphotovideo.com';
SELECT * FROM ywx_product_data WHERE site = ' http://www.www.ebuyer.com';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.ebuyer.com' AND mark = 'tv';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.ebuyer.com' AND mark = 'phone';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.ebuyer.com' AND mark = 'camera';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.ebuyer.com' AND mark = 'LED TV';
SELECT COUNT(*) FROM ywx_product_data WHERE site = ' http://www.www.ebuyer.com' AND mark = 'bike';
UPDATE ywx_product_data SET mark = 'tv' WHERE site = ' http://www.www.ebuyer.com' AND mark = 'tv';
UPDATE ywx_product_data SET mark = 'phone'  WHERE site = ' http://www.www.ebuyer.com' AND mark = 'phone';
UPDATE ywx_product_data SET mark = 'camera' WHERE site = ' http://www.www.ebuyer.com' AND mark = 'camera';
UPDATE ywx_product_data SET mark = 'bike'  WHERE site = ' http://www.www.ebuyer.com' AND mark = 'bike';
UPDATE ywx_product_data SET site = 'ebuyer' WHERE site = ' http://www.www.ebuyer.com';
SELECT * FROM ywx_product_data WHERE site = 'ebuyer';
#delete from  ywx_product_data WHERE site = ' http://www.bhphotovideo.com' AND mark = 'LED tv';
#delete from  ywx_product_data WHERE site = ' http://www.bhphotovideo.com' AND mark = 'phone';
#delete from  ywx_product_data WHERE site = ' http://www.bhphotovideo.com' AND mark = 'laptop core i';
#delete from  ywx_product_data WHERE site = ' http://www.bhphotovideo.com' AND mark = 'DSLR camera';
#delete from  ywx_product_data  WHERE site = ' http://www.bhphotovideo.com' AND mark = 'bike';



































##############################################################################################################
SELECT COUNT(*) FROM online_retail_products_data_ebay_bike;
SELECT COUNT(*) FROM online_retail_products_data_ebay_camera;
SELECT COUNT(*) FROM online_retail_products_data_ebay_labtop;
SELECT COUNT(*) FROM online_retail_products_data_ebay_phone;
SELECT COUNT(*) FROM online_retail_products_data_ebay_tv;   

SELECT COUNT(*) FROM online_retail_products_data_bhphotovides_labtop;
SELECT COUNT(*) FROM online_retail_products_data_bhphotovides_camera;
SELECT COUNT(*) FROM online_retail_products_data_bhphotovides_phone;
SELECT COUNT(*) FROM online_retail_products_data_bhphotodes_tv;

SELECT COUNT(*) FROM online_retail_products_data_sears_tv;
SELECT COUNT(*) FROM online_retail_products_data_marcmall_labtop;
SELECT COUNT(*) FROM online_retail_products_data_sears_camera;

SELECT COUNT(*) FROM online_retail_products_data_cdiscount_labtop;
SELECT COUNT(*) FROM online_retail_products_data_cdiscount_camera;
SELECT COUNT(*) FROM online_retail_products_data_cdiscount_phone;
SELECT COUNT(*) FROM online_retail_products_data_cdiscount_tv;

SELECT COUNT(*) FROM online_retail_products_data_cdiscount_labtop;
SELECT COUNT(*) FROM online_retail_products_data_cdiscount_camera;
SELECT COUNT(*) FROM online_retail_products_data_cdiscount_phone;
SELECT COUNT(*) FROM online_retail_products_data_cdiscount_tv;