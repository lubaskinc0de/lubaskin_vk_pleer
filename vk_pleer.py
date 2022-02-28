from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import auth

options = webdriver.ChromeOptions()
#options.add_argument(f'user-agent=your_user_agent - optional')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless') # в фоне

driver = webdriver.Chrome(r'your_chromedriver_path',options=options) # if you dont install chromedriver install it = https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.102/ , next , unzip and write path, example - C:\Users\User\Desktop\chromedriver.exe

try:
    print('''Добро пожаловать мой гениальный создатель!\nПослушаем вашу музыку?\nСледующий трек: >\nПредыдущий: <\nПауза: =\nНачать прослушивание: /start''')
    operation = str(input('Окунуться в мир музыки?\n'))
    if operation == '/start':
        driver.get('https://vk.com/')
        print('Passing auth...')
        email_input = driver.find_element_by_id('index_email') # атрибут id (нашел на сайте вк) ввод почты
        email_input.clear() # очищает поле ввода
        email_input.send_keys(auth.PHONE) # your login_file_phone
        pass_input = driver.find_element_by_id('index_pass')
        pass_input.clear()
        pass_input.send_keys(auth.PASS) # your pass
        button_login = driver.find_element_by_css_selector('#index_login_button')
        button_login.click()
        print('Auth complete!')
        time.sleep(10)
        driver.find_element_by_id('l_aud').click()
        print('click to audio')
        time.sleep(5)
        music = driver.find_element_by_css_selector('#content > div > div._audio_page_content_block_wrap.audio_page_content_block_wrap > div.audio_page_sections._audio_page_sections.clear_fix > div.audio_section.audio_w_covers._audio_section._audio_section__general.audio_section__general > div > div:nth-child(1) > div.CatalogBlock__content.CatalogBlock__my_audios_block.CatalogBlock__layout--triple_stacked_slider > div > div.ui_gallery__inner_cont > div > div:nth-child(1) > ul > li:nth-child(1) > div > div > div.audio_row__cover_back._audio_row__cover_back').click()
except Exception:
    print('Неккоректный ввод!')

pleer = str(input('Введите действия для плеера (по желанию)\n'))

def listen_music(operand):
    try:
        if operand == '>':
            time.sleep(1)
            music_next = driver.find_element_by_css_selector('#content > div > div._audio_page_player_wrap.audio_page_player_wrap.page_block > div > button.audio_page_player_ctrl.audio_page_player_next').click()
            listen_music(str(input('Введите команду для плеера:\n')))
        elif operand == '<':
            time.sleep(1)
            music_back = driver.find_element_by_css_selector('#content > div > div._audio_page_player_wrap.audio_page_player_wrap.page_block > div > button.audio_page_player_ctrl.audio_page_player_prev').click()
            listen_music(str(input('Введите команду для плеера:\n')))
        elif operand == '=':
            time.sleep(1)
            driver.find_element_by_css_selector('#content > div > div._audio_page_player_wrap.audio_page_player_wrap.page_block > div > button.audio_page_player_ctrl.audio_page_player_play._audio_page_player_play').click()
            listen_music(str(input('Введите команду для плеера:\n')))
        else:
            print('Неккоректный ввод')
            listen_music(str(input('Введите команду для плеера:\n')))
    except Exception:
        print('Неккоректный ввод!')

listen_music(pleer)

