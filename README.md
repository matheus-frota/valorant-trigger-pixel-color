# TriggerBot pixel color

Essa é um bot trigger em Python que automatiza o disparo das armas com base na identificação do inimico a partir da coloração do contorno do próprio.

## Requisitos
* Python 3.x
* Bibliotecas: keyboard, pyautogui, pygetwindow, win32api, matplotlib
## Como usar
1. Clone o repositório em sua máquina local.
```bash
git clone https://github.com/seu-usuario/valorant-bot.git
```
2. Instale as dependências usando o pip.
```bash
pip install -r requirements.txt
```
3. Execute o script trigger_bot.py.
```bash
python trigger_pixel_color/trigger_bot.py
```
4. Use as teclas "Ctrl" para ativar/desativar o disparo e "Ctrl+Alt" para fechar o programa.

## Observações
* Este script é simples, porém funcional. Ele atira quando detecta um inimigo, mas é importante lembrar que é uma solução muito básica e não se compara às alternativas disponíveis no mercado que usam métodos mais avançados. Embora eu tenha testado esse script em vários modos de jogo sem nunca ter sido banido, é importante ressaltar que a utilização do mesmo é de total responsabilidade do usuário.
* O programa funciona somente em resolução de tela 1920x1080 (Full HD). Caso sua resolução seja diferente, será necessário ajustar as constantes WIDTH e HEIGHT no arquivo config.py.
* O programa pode violar os Termos de Serviço do jogo. O uso é de responsabilidade do usuário.