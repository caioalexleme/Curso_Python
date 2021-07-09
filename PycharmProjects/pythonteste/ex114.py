import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento!')
else:
    print('Consegui acessar o site Pudim com secesso!')
    print(site.read()) #read consegue acessar o conteúdo html do site
