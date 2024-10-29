import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from flask import Flask, render_template

app = Flask(__name__)

class EpicGamesSpider:
    def __init__(self):
        options = Options()
        options.headless = True

        # Adicione o caminho para o executável do Firefox
        if os.name == 'nt':  # Verifica se é Windows
            options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        elif os.name == 'posix':  # Verifica se é Linux ou Mac
            options.binary_location = "/usr/bin/firefox"  # Ajuste conforme a instalação

        # Usando caminho relativo para o geckodriver
        gecko_path = os.path.join(os.getcwd(), 'static', 'geckodriver.exe')  # Mude conforme necessário
        service = Service(executable_path=gecko_path)
        
        self.driver = webdriver.Firefox(service=service, options=options)

    def parse(self):
        self.driver.get('https://store.epicgames.com/pt-BR/free-games')
        games = self.driver.find_elements(By.CSS_SELECTOR, 'div.css-1myhtyb')

        free_games = []
        for game in games:
            title = game.find_element(By.XPATH, './/h6').text
            link = game.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            image = game.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')

            free_games.append({
                'title': title,
                'link': link,
                'image': image,
            })

        self.driver.quit()
        return free_games

@app.route('/')
def home():
    spider = EpicGamesSpider()
    games = spider.parse()
    return render_template('index.html', games=games)

if __name__ == "__main__":
    app.run(debug=True)
