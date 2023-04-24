import datetime
from data.config import creator_id
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from loader import dp, connect, cursor
from selenium.webdriver.firefox.options import Options


def help_me(lst, lst1):
    res = {}
    last_date = ''
    rasp = []
    res_2 = []
    ind = 0
    for i in lst:
        text = str(i)[3:-4]
        if text.split()[0].isdigit():
            res[text] = []
            last_date = text
        else:
            res[last_date].append(text)
    for i in lst1[2:-1]:
        rasp.append(' '.join(str(i).split('<br/>')).replace('b', '').replace('r', '').replace('/', '').replace('>',
                                                                                                               '').replace(
            '<', '').replace('p', ''))
    for k, v in res.items():
        str_res = f"{k}\n\n"
        for _ in res[k]:
            str_res += f'{rasp[ind]}\n\n'
            ind += 1
        res_2.append(str_res)
    return res_2


async def my_shedule():
    url = 'https://www.rksi.ru/schedule'
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    try:
        driver.get(url=url)
        se = Select(driver.find_element(By.NAME, "group"))  # group - имя элемента
        for item in se.options:
            if item.text == 'ИС-12':
                item.click()
                break
        button = driver.find_element(By.NAME, "stt")
        button.click()
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")
        el = soup.find_all('b')
        el1 = soup.find_all('p')
        today, tommorow = help_me(el, el1)[:2]
        data = datetime.datetime.now()
        data = '.'.join([str(data.day), str(data.month), str(data.year)])
        cursor.execute(f"""INSERT INTO Shedule(data, today, tommorow) 
                        VALUES('{data}', '{today}', '{tommorow}') """)
        connect.commit()
        await dp.bot.send_message(creator_id, 'Новое расписание успешно добавлено в базу данных')
    except Exception as ex:
        await dp.bot.send_message(creator_id, f'Не удалось обновить расписание\n'
                                              f'Error: {ex}')
    finally:
        driver.close()
        driver.quit()
