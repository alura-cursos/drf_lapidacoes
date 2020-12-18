import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random, datetime
from escola.models import  Aluno, Curso, Matricula

def criando_alunos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        cpf = cpf.generate()
        data_nascimento = fake.date_between(start_date='-18y', end_date='today')
        a = Aluno(nome=nome,rg=rg, cpf=cpf,data_nascimento=data_nascimento)
        a.save()

def criando_cursos(quantidade_de_cursos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_cursos):
        codigo_curso = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']
        descricao = random.choice(descs)
        descs.remove(descricao)
        nivel = random.choice("BIA")
        c = Curso(codigo_curso=codigo_curso,descricao=descricao, nivel=nivel)
        c.save()


criando_alunos(200)
criando_cursos(5)