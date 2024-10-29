# 🕹️ Free Games

## Descrição

O **Free Games Scraper** é um projeto em Flask que coleta e exibe jogos gratuitos disponíveis na Epic Games Store. Utilizando Selenium e o Geckodriver, ele automatiza a extração de dados da página de jogos gratuitos e apresenta essas informações em uma interface web simples e elegante.

## Tecnologias Utilizadas

- **Flask**: Um microframework para construção de aplicações web em Python.
- **Selenium**: Uma biblioteca para automação de navegadores, usada para interagir com a Epic Games Store.
- **Geckodriver**: Um driver para o navegador Firefox, necessário para executar o Selenium.
- **HTML/CSS**: Para a estrutura e estilo da interface.

## Instalação

Para configurar o projeto em sua máquina local, siga as etapas abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
2. **Crie um ambiente virtual:**

   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
3. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
4. **Baixe o Geckodriver:**
    Acesse Geckodriver Releases e baixe a versão apropriada para o seu sistema operacional.
    Extraia o arquivo e coloque geckodriver.exe na pasta static do projeto.
**Como executar**
    ```bash
    python app.py
Acesse a aplicação em seu navegador em: http://127.0.0.1:5000

**Contribuição**

Contribuições são bem-vindas! Se você tem sugestões ou melhorias, sinta-se à vontade para abrir um pull request.
