from django.test import TestCase
from .models import Usuario

class UsuarioModelTest(TestCase):
    def setUp(self):
        Usuario.objects.create(nome="David", idade=28)
        Usuario.objects.create(nome="Euller", idade=14)
        Usuario.objects.create(nome="Julia", idade=17)
        Usuario.objects.create(nome="Pedro", idade=19)
        Usuario.objects.create(nome="Vitor", idade=25)

    def test_existe_ou_nao_existe(self):
        teste1 = Usuario.objects.filter(nome="Carlos").exists()
        teste2 = Usuario.objects.filter(nome="Joana").exists()
        teste3 = Usuario.objects.filter(nome="Lucas").exists()
        print("Verificando se usuários existem:")
        print()     
        print(f" Carlos existe? {teste1}")
        print(f" Joana existe? {teste2}")
        print(f" Lucas existe? {teste3}")

        print("-------------------------------")

    def test_usuario_maior_de_18(self):
        usuarios_maior_18 = Usuario.objects.filter(idade__gt=18)
        print("Usuários com idade maior que 20 anos:")
        for usuario in usuarios_maior_18:
            print(f"Nome: {usuario.nome}, Idade: {usuario.idade}")
        print("-------------------------------")    
    
    def test_usuario_menor_de_18(self):
        usuarios_menor_18 = Usuario.objects.filter(idade__lt=18)
        print("Usuários com a idade menor que 20 anos:")
        for usuario in usuarios_menor_18:
            print(f"Nome: {usuario.nome}, Idade: {usuario.idade}")
        print("-------------------------------")

    def test_usuario_de_maior_ou_menor(self):
        usuario = Usuario.objects.get(nome="Pedro")
        if usuario.idade > 18:
            print(f"{usuario.nome} é maior de 18 anos, idade: {usuario.idade}")
        else:
            print(f"{usuario.nome} é menor de 18 anos, idade: {usuario.idade}")
        print("-------------------------------")

