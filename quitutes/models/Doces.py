from quitutes.models import *

class Doce(models.Model):

    CATEGORIAS = (
        ('brigadeiro','Brigadeiro'),
        ('bolacha','Bolacha'),
        ('brownie','Brownie'),
        ('torta','Torta'),
    )
    nome = models.CharField(max_length=100, null=False,blank=False)
    peso = models.FloatField()
    descricao = models.TextField()
    valor = models.FloatField(null=False,blank=False)
    image = models.ImageField(null=True)
    categoria = models.CharField(choices=CATEGORIAS,default='brigadeiro',max_length=255)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome