from django.db import models


class LocalEvento(models.Model):
    descricao = models.TextField()
    def __str__(self):
        return self.descricao


class ItemAgenda(models.Model):
    data = models.DateField('data do evento')
    hora = models.TimeField()
    titulo = models.CharField('título',max_length=100)
    descricao = models.TextField('descrição')
    criado_em = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(LocalEvento, on_delete=models.CASCADE)
    participantes = models.ManyToManyField('auth.User')

    class Meta:
        verbose_name_plural = 'tarefas agendadas'
        verbose_name = 'tafera agendada'

    def __str__(self):
        return '{} {} - {}'.format(
            self.data.strftime('%d/%m/%Y'),
            self.hora.strftime('%H:%M'),
            self.titulo
        )

