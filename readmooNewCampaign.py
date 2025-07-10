from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import re
import datetime

def search_eisbn(eisbn):
    # 初始化 Firefox WebDriver
    options = Options()
    options.headless = True  # 無頭模式
    driver = webdriver.Firefox(options=options)
    
    try:
        # 開啟目標網站
        driver.get("https://readmoo.com/campaign/activities")  # 替換為您的目標網址
        
        # 獲取所有指定元素
        elements = driver.find_elements(By.CSS_SELECTOR, '.col-sm-8.mt-2.mt-sm-0')

        # 創建一個數組來存儲活動信息
        activities = []

        # 遍歷每個匹配的元素
        for element in elements:
            # 獲取標題元素
            title_element = element.find_element(By.CSS_SELECTOR, 'h2.font-weight-bold a')
            title = title_element.text.strip() if title_element else ''
            link = title_element.get_attribute('href') if title_element else ''

            # 獲取活動期間的文本內容
            period_text = element.find_element(By.TAG_NAME, 'p').text.strip()

            # 提取日期部分
            period_match = re.search(r'活動期間：(\d{4}\/\d{2}\/\d{2}) - (\d{4}\/\d{2}\/\d{2})', period_text)
            start_date = period_match.group(1) if period_match else ''
            end_date = period_match.group(2) if period_match else ''

            # 將活動信息添加到數組中
            activities.append({
                'startDate': start_date,
                'endDate': end_date,
                'title': title,
                'link': link
            })

        # 對活動數組按照 startDate 由舊到新排序
        activities.sort(key=lambda x: datetime.datetime.strptime(x['startDate'], '%Y/%m/%d'))

        # 打印排序後的活動信息
        for activity in activities:
            print(activity['startDate'], ";", activity['endDate'], ";", activity['title'], ";", activity['link'])
    
    finally:
        # 關閉瀏覽器
        driver.quit()

# 調用函數示例（根據需要傳入 eISBN）
search_eisbn("your_eisbn_here")
