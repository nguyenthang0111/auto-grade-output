import time
import json
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def autograde(opt):
    # Dang nhap website ctt-sis
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://ctt-sis.hust.edu.vn/Account/Login.aspx")
    #driver.maximize_window()

    # Nhap email
    user = driver.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_tbUserName_I")
    user.clear()
    user.send_keys(opt['user'])
    user.send_keys(Keys.RETURN)

    # Nhap mat khau
    password = driver.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_tbPassword_I")
    password.clear()
    password.send_keys(opt['password'])
    password.send_keys(Keys.RETURN)

    # Dung vai giay de nguoi dung nhap captcha
    time.sleep(8)

    # Tu dong an nut dang nhap
    button = driver.find_element_by_id("ctl00_ctl00_contentPane_MainPanel_MainContent_btLogin")
    ActionChains(driver).move_to_element(button).click(button).perform()
    driver.implicitly_wait(5)


    #Chuyen sang trang bang diem
    driver.get("https://ctt-sis.hust.edu.vn/Students/StudentCourseMarks.aspx")

    #Cho doi chuyen trang
    driver.implicitly_wait(5)

    listMonHoc = []

    MonHoc = driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr")
    for i in range(4, len(MonHoc)+1):
        maHP = driver.find_element_by_xpath(
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr[" + str(
                i) + "]/td[2]").text
        tenMonHoc = driver.find_element_by_xpath(
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr[" + str(
                i) + "]/td[3]").text
        soTinChi = driver.find_element_by_xpath(
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr[" + str(
                i) + "]/td[4]").text
        diemQT = driver.find_element_by_xpath(
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr[" + str(
                i) + "]/td[6]").text
        diemThi = driver.find_element_by_xpath(
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr[" + str(
                i) + "]/td[7]").text
        diemChu = driver.find_element_by_xpath(
            "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td/table[2]/tbody/tr[" + str(
                i) + "]/td[8]").text
        thongTinMH = {
            'M?? HP': maHP,
            'T??n HP': tenMonHoc,
            'S??? t??n ch???': soTinChi,
            '??i???m QT': diemQT,
            '??i???m thi': diemThi,
            '??i???m ch???': diemChu
        }
        listMonHoc.append(thongTinMH)

    print(listMonHoc)
    soMonHoc = len(MonHoc) - 3

    print(soMonHoc)

    with open('result.csv', mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['M?? HP', 'T??n HP', 'S??? t??n ch???', '??i???m QT', '??i???m thi', '??i???m ch???'])
        for j in range(0, soMonHoc):
            writer.writerow(
                [listMonHoc[j]['M?? HP'], listMonHoc[j]['T??n HP'], listMonHoc[j]['S??? t??n ch???'], listMonHoc[j]['??i???m QT'],
                 listMonHoc[j]['??i???m thi'], listMonHoc[j]['??i???m ch???']])

    time.sleep(5)
    driver.close()

def main():
    file = open('account.txt', 'r')
    data = file.read()
    file.close()
    opt = json.loads(data)
    autograde(opt)

if __name__ == "__main__":
    main()
