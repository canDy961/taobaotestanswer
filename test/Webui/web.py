from selenium import webdriver
import tool
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time
driver=webdriver.Chrome()
driver.get("https://www.taobao.com/")
def login():
    # 获取登录入口并点击
    get_loginelem=driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]');
    get_loginelem.click();

    # 获取用户名和密码输入框
    get_usernameelem=driver.find_element_by_xpath('//*[@id="fm-login-id"]');
    get_passwordelem=driver.find_element_by_xpath('//*[@id="fm-login-password"]');

    # 输入用户名和密码
    data=tool.readConfig()
    print(data['user']['usermane'])
    get_usernameelem.send_keys(data['user']['usermane']);
    print(data['user']['password'])
    get_passwordelem.send_keys(data['user']['password']);

    # 滑动模块
    driver.implicitly_wait(10)
    slider=driver.find_element_by_xpath('//*[@id="nc_2_n1z"]')  # 定位滑动模块
    action=ActionChains(driver)
    action.click_and_hold(slider).perform()  # 单击并按下鼠标左键
    for index in range(200):
        try:
            action.move_by_offset(2,0).perform()  # 移动鼠标
        except UnexpectedAlertPresentException:
           break
        action.reset_actions()   # 重置action
        time.sleep(0.1)

# 搜索商品
def search_goods():
    # 获取搜索输入框
    get_searchelem=driver.find_element_by_xpath('//*[@id="q"]');
    # 读取搜索商品内容
    data=tool.readConfig()
    print(data['search']['goods'])
    get_searchelem.send_keys(data['search']['goods']);
    get_searchbtn=driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button');
    get_searchbtn.click();
    driver.implicitly_wait(10) #等待页面加载成功

# 商品下单
def order():
    # 获取第1个商品并点击
    current_window=driver.current_window_handle
    get_goods=driver.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]');
    get_goods.click();
    # 切换窗口
    all_handles=driver.window_handles()  # 获取当前所有打开的窗口句柄
    for handle in all_handles:
        if handle !=current_window:
            driver.switch_to_window(handle)
            break;

    # 选中商品属性
    get_goodssize=driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[1]/a/span')
    get_goodsclor=driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/ul/li[1]/a/span')
    get_orderbtn=driver.find_element_by_xpath('//*[@id="J_LinkBuy"]')
    get_orderbtn.click();
    driver.implicitly_wait(10); # 等待页面加载
def paygood():
    # 选择收获地址
    get_address=driver.find_element_by_xpath('//*[@id="addressPC_1"]/div[3]/div[1]/div[1]')
    # 提交订单
    get_paybtn=driver.find_element_by_xpath('//*[@id="submitOrderPC_1"]/div/a')
    get_paybtn.click();
    # 输入支付密码
    get_payN01= driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[1]')
    get_payN02= driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[2]')
    get_payN03= driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[3]')
    get_payN04= driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[4]')
    get_payN05= driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[5]')
    get_payN06= driver.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[6]')
    get_payN01.send_keys(1)
    get_payN02.send_keys(2)
    get_payN03.send_keys(3)
    get_payN04.send_keys(4)
    get_payN05.send_keys(5)
    get_payN06.send_keys(6)
    get_submit=driver.find_element_by_xpath('//*[@id="J_authSubmit"]')
    get_submit.click()
# 退出 webdriver
driver.close()






















