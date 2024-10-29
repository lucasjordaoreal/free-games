from flask import Flask, render_template
from epic_games_spider import EpicGamesSpider

app = Flask(__name__)

@app.route('/')
def index():
    spider = EpicGamesSpider()
    games = spider.parse()  # Agora obtém a lista de jogos corretamente
    return render_template('index.html', games=games)  # Passa os jogos para o template

if __name__ == '__main__':
    app.run(debug=True)
