# -*- coding:UTF-8 -*-

import sys

from ProductGraber.EabyGraber import EbayGraber
from ProductGraber.GraEbuyerPhone import GrabEbuyerPhone
from ProductGraber.GrabCdiscountPhone import GrabCdiscountPhone
from ProductGraber.GrabOverStockPhone import GrabOverStockPhone
from ProductGraber.SearGraber import GrabSearsPhone

reload(sys)
sys.setdefaultencoding('utf-8')


def grab_ebay_datas():
    # 将以下信息存入到数据库中的一张表中，表名：CrawSubject，构建结构体 CrawSubject：root_URL,product_type, storage_table_name
    # for 循环遍历，生成多个对象并启动对应的start

    # spider = GrabEabyTV("http://www.ebay.com", "tv", "online_retail_products_data_ebay_tv")
    # spider.start()

    # phone_spider = GrabEabyPhone("http://www.ebay.com", "phone", "online_retail_products_data_ebay_phone")
    # phone_spider.start()
    #
    # camera_spider = GrabEabyCamera("http://www.ebay.com", "camera", "online_retail_products_data_ebay_Camera")
    # camera_spider.start()
    #
    # bike_spider = GrabEabyBike("http://www.ebay.com", "bike", "online_retail_products_data_ebay_bike")
    # bike_spider.start()
    #
    # labtop_spider = EbayGraber("http://www.ebay.com", "labtop", "online_retail_products_data_ebay_labtop")
    # labtop_spider.start()

    camera_spider = EbayGraber("http://www.ebay.com", "digital camera", "online_retail_products_data_ebay_camera")
    camera_spider.start()

    camera_spider1 = EbayGraber("http://www.ebay.com", "DSLR camera", "online_retail_products_data_ebay_camera")
    camera_spider1.start()

    # phone_spider = GrabEabyPhone("http://www.ebay.com", "phone", "online_retail_products_data_ebay_phone")
    # phone_spider.start()
    pass


def grab_ebuer_datas():

    tv_spider = GrabEbuyerPhone("http://www.ebuyer.com", "tv", "online_retail_products_data_ebuyer_tv")
    tv_spider.start()

    phone_spider = GrabEbuyerPhone("http://www.ebuyer.com", "phone", "online_retail_products_data_ebuyer_phone")
    phone_spider.start()

    camera_spider = GrabEbuyerPhone("http://www.ebuyer.com", "camera", "online_retail_products_data_ebuyer_camera")
    camera_spider.start()

    labtop_spider = GrabEbuyerPhone("http://www.ebuyer.com", "labtop", "online_retail_products_data_ebuyer_labtop")
    labtop_spider.start()

    bike_spider = GrabEbuyerPhone("http://www.ebuyer.com", "bike", "online_retail_products_data_ebuyer_bike")
    bike_spider.start()

    pass

def grab_cdiscount_datas():
    phone_spider = GrabCdiscountPhone("http://www.cdiscount.com", "phone", "online_retail_products_data_cdiscount_phone")
    phone_spider.start()

    camera_spider = GrabCdiscountPhone("http://www.cdiscount.com", "camera", "online_retail_products_data_cdiscount_camera")
    camera_spider.start()

    bike_spider = GrabCdiscountPhone("http://www.cdiscount.com", "bike", "online_retail_products_data_cdiscount_bike")
    bike_spider.start()

    labtop_spider = GrabCdiscountPhone("http://www.cdiscount.com", "labtop", "online_retail_products_data_cdiscount_labtop")
    labtop_spider.start()

    tv_spider = GrabCdiscountPhone("http://www.cdiscount.com", "tv", "online_retail_products_data_cdiscount_tv")
    tv_spider.start()

    pass

def grab_sears_datas():
    phone_spider = GrabSearsPhone("http://www.sears.com", "cellphone",  "online_retail_products_data_sears_phone")
    phone_spider.start()

    tv_spider = GrabSearsPhone("http://www.sears.com", "tv", "online_retail_products_data_sears_tv")
    tv_spider.start()

    camera_spider = GrabSearsPhone("http://www.sears.com", "digit camera", "online_retail_products_data_sears_camera")
    camera_spider.start()

    labtop_spider = GrabSearsPhone("http://www.sears.com", "Labtop", "online_retail_products_data_sears_labtop")
    labtop_spider.start()

    bike_spider = GrabSearsPhone("http://www.sears.com", "bike", "online_retail_products_data_sears_bike")
    bike_spider.start()
    pass

def grab_overstcok_datas():
    phone_spider = GrabOverStockPhone("http://www.overstock.com", "cellphone",  "online_retail_products_data_overstcok_phone")
    phone_spider.start()

    tv_spider = GrabOverStockPhone("http://www.overstock.com", "tv", "online_retail_products_data_overstcok_tv")
    tv_spider.start()

    tv_spider = GrabOverStockPhone("http://www.overstock.com", "bike", "online_retail_products_data_overstcok_bike")
    tv_spider.start()

    labtop_spider = GrabOverStockPhone("http://www.overstock.com", "labtop", "online_retail_products_data_overstcok_labtop")
    labtop_spider.start()

    camera_spider = GrabOverStockPhone("http://www.overstock.com", "camera", "online_retail_products_data_overstcok_camera")
    camera_spider.start()
    pass

def grab_jet_datas():
    phone_spider = GrabCdiscountPhone("http://www.sears.com", "cellphone",  "online_retail_products_data_sears_phone")
    phone_spider.start()

    tv_spider = GrabCdiscountPhone("http://www.sears.com", "tv", "online_retail_products_data_sears_tv")
    tv_spider.start()
    pass

if __name__ == '__main__':

    grab_ebay_datas()
    #grab_ebuer_datas()
    # grab_cdiscount_datas()
    # grab_sears_datas()     ################3  单击按钮   单击下一页错误
    #grab_overstcok_datas()
    # grab_jet_datas()


    #pool = IPProxyPool()
    #pool.start()

def GetNewKeyWord():
    productArray = []
    file = open("Bikes.txt")
    while 1:
        line = file.readline()
        if not line:
            break
        productArray.append(line)
    return  productArray