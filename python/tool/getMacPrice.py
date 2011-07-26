import urllib2
import time

def fetchPrice(url, filename):
    # print 'geting price page, please wait..'
    page = urllib2.urlopen(url).read();

    priceIndex = page.find('priceLarge') + 16
    oPriceIndex = page.find('listprice">') + 15

    price = page[priceIndex: priceIndex + 8]
    oPrice = page[oPriceIndex: oPriceIndex + 8]

    priceString = '[%s]orgin price: %s  => now: %s\n'%(time.strftime('%m-%d %H:%M:%S'), oPrice, price)
    # print priceString

    f = open('/root/liao/' + filename, 'a')
    f.write(priceString)
    f.close()

macUrl = 'http://www.amazon.cn/gp/product/B004PYEGE8/ref=s9_simh_gw_p147_d0_i1?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=center-1&pf_rd_r=0JW1WWYZ20YWJ1A7A29B&pf_rd_t=101&pf_rd_p=58840952&pf_rd_i=899254051'
fetchPrice(macUrl, 'mac.prc')
iphoneUrl = 'http://www.amazon.cn/%E8%8B%B9%E6%9E%9Ciphone-4%E6%89%8B%E6%9C%BA/dp/B004185D5O/ref=sr_1_1?ie=UTF8&qid=1311663437&sr=8-1'
fetchPrice(iphoneUrl, 'iphone.prc')
