import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()


import random
from quitutes.models import Doce

def criando_doces(qtd_doces):
    for c in range(qtd_doces):
        nome = f'teste {c}'
        peso = f'{random.randrange(0,60)}.{random.randrange(0,60)}{random.randrange(0,60)}'
        peso = float(peso)
        descricao = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy'
        valor = f'{random.randrange(0,60)}.{random.randrange(0,60)}{random.randrange(0,60)}'
        valor = float(valor) 
        ativo = True
        categorias = ['brigadeiro','bolacha','brownie','torta']
        categoria = categorias[random.randrange(0,4)]
        a = Doce(nome=nome,peso=peso,descricao=descricao,valor=valor,ativo = ativo,categoria=categoria)
        a.save()



criando_doces(40)
