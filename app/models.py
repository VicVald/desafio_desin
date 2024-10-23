from django.db import models

class Nave(models.Model):
    tamanho = models.IntegerField() # Gigantesca, Grande, Média, Pequena
    cor = models.CharField(max_length=255) # Branco, Preto, Azul, Verde, Vermelho, Amarelo, Laranja, Roxo, Rosa, Marrom, Cinza, Prata, Dourado
    local_queda = models.CharField(max_length=255) # Rua, Parque, Floresta, Lago, Mar, Comércio, Escola, Hospital, Aeroporto, Base Militar
    armamento = models.CharField(max_length=255) # Nenhum, Leve, Médio, Pesado, Nuclear
    combustivel= models.CharField(max_length=255) # Biocombustível, Antimatéria, Plasma, Energia Solar, Hidrogênio, Elétrico, Óleo, Gás
    tripulantes = models.CharField(max_length=255) #Decidir se é um campo de texto ou um dicionario de tripulantes e estado
    avaria = models.CharField(max_length=255) # Perda total, Muito destruída, Parcialmente destruída, Praticamente intacta e Sem avarias
    potencial_prospecção_tecnologico = models.IntegerField() # 0 a 10
    periculosidade = models.IntegerField() # 0 a 10
    etiquetas = models.CharField(max_length=255) # Adicionar as etiquetas de acordo com as condições
       

class Pato:
    
    pele_esverdeada = models.BooleanField()
    bico_pequeno = models.BooleanField()
    sotaque_esquisito = models.BooleanField()
    local = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255) # Sozinho, em dupla, em bando pequeno ou em bando grande
    xenofago = models.BooleanField()
    plano_captura = models.CharField(max_length=255)