from django.db import models

class ContactMessage(models.Model):
    subjectChoises = [
        ('DUVIDAS', 'Dúvidas'),
        ('ORCAMENTOS', 'Orçamentos'),
        ('PROJETOS', 'Projetos'),
        ('FEEDBACK', 'Feedback'),
        ('SUGESTAO', 'Sugestão'),
        ('BUG', 'Bug'),
        ('OUTROS', 'Outros'),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    subject = models.CharField(max_length=20, choices=subjectChoises, default='')
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"