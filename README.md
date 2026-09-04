
<div>
<img width="250" height="140.5" alt="Stripe-logo-500x281" src="https://github.com/user-attachments/assets/95e5d8aa-83fd-4fdb-bdd7-e1424c4ae01c" />
</div>

# Aplicativo para programação de interfaces em meios de pagamentos como Stripe e Kiwify feito em Django

Este aplicativo se baseia em uma aplicação na linguagem de programação Python com o framework Django.

---

### Objetivo do Aplicativo

A aplicação tem como principal meta suprir a demanda de métodos de pagamentos para aplicações web, oferecendo como os alguns dos principais meios em sua API (Application Web Interface) e suas URLs, como Stripe e Kiwify para os meios de pagamentos, podendo expandir para outras, como: mercado pago, pagar.me, hotmart, etc. Sendo o principal objetivo de garantir que tenhamos como pagar nosso produto através dessa API.

---

### Padrão de Projetos

O padrão de projeto adotado nessa aplicação vem da convenção do site do Django, onde com base em sua documentação e suas orientações, criei um backend modelado nos padrões django, usando comandos do framework e entre outros aspectos dessa ferramenta, sendo uma ótima ferramenta para criação de aplicações rapidamente escaláveis. 

---

## Comandos para instalação e inicialização do programa

### Configuração inicial do projeto

Tenha certeza de ter o Python instalado em sua máquina, sendo de uma versão atualizada, de meu computador sendo do versionamento 3.14.5

*Criação do pacote /venv na pasta do projeto*
```bash
# para maioria dos projetos Python, crie um pacote /venv para usablidade facilitada da linguagem 
python -m venv venv
```

*Instalação do Django no Arquivo Local*
```bash
# baixar Django no arquivo local 
python -m pip install Django
```
*Verificando se o Django foi instalado corretamente*
```shell
# use o shell ou rode em um arquivo .py para verificar se está instalado corretamente
>>> import django
>>> print(django.get_version())
output: 6.1
```

---

### Rodando o projeto

*Comando para rodar a aplicação na pasta do manage.py*
```bash
# após a instalação e configuração rode esse programa
python manage.py runserver
```
## Realizando testes automatizados em nossas aplicações 

Testes são uma parte fundamental em nossa aplicação

*Comando para rodar os testes na aplicação*
```bash
# esse comando irá rodar os testes
python manage.py test
```
---

<img width="340" height="180" alt="Captura de tela 2026-09-04 010518" src="https://github.com/user-attachments/assets/9fc71d3b-9ce6-4cc6-9e37-8191b3385d38" />

# Django Rest Framework
