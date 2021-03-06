## -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime
import os

CURSOS_CHOICE = (
    (u"Estatística", u"Estatística"),
    (u"Matemática", u"Matemática"),
    (u"Engenharia Cartográfica", u"Engenharia Cartográfica"),
    (u"Fisioterapia", u"Fisioterapia"),
    (u"Geografia", u"Geografia"),
    (u"Química", u"Química"),
    (u"Ciência da Computação", u"Ciência da Computação"),
    (u"Educação Física", u"Educação Física"),
    (u"Arquitetura e Urbanismo", u"Arquitetura e Urbanismo"),
    (u"Engenharia Ambiental", u"Engenharia Ambiental"),
    (u"Pedagogia", u"Pedagogia"),
    (u"Física", u"Física"),
)


class Disciplina(models.Model):
    data = models.DateField(
        u"Ano",
        default=datetime.datetime.now,
        help_text="Ano que a Disciplina será Oferecida",
    )
    nome = models.CharField(
        u"Nome do Disciplina", max_length=200, null=False, blank=False
    )
    curso = models.CharField(u"Curso", choices=CURSOS_CHOICE, max_length=100)

    class Meta:
        verbose_name = u"Disciplinas"
        verbose_name_plural = u"Disciplinas"

    def __unicode__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(
        u"Nome do Professor", max_length=200, null=False, blank=False
    )
    universidade = models.CharField(
        u"Universidade", max_length=200, null=False, blank=False
    )
    depto = models.CharField(u"Departamento", max_length=200, null=False, blank=False)
    cidade = models.CharField(u"Cidade", max_length=200, null=False, blank=False)
    email = models.EmailField(u"Email", null=False, blank=False)
    c_lattes = models.URLField(
        u"URL do Curriculum Lattes",
        help_text="ex:http://buscatextual.cnpq.br/buscatextual/visualizacv.jsp?id=XXXXXX",
    )
    disciplinas = models.ManyToManyField(
        Disciplina,
        related_name="professor_disciplinas",
        help_text="Disciplinas que o professor irá ministrar",
    )

    avatar = models.ImageField(
        u"Imagem do Professor", upload_to="uploads/professor/avatar/"
    )

    class Meta:
        verbose_name = u"Professor"
        verbose_name_plural = u"Professores"


class MaterialApoio(models.Model):
    data = models.DateField(default=datetime.datetime.now, editable=False)
    descricao = models.TextField(u"Descrição", blank=False, null=False)
    codigo = models.TextField(u"Código Fonte", blank=True, null=True)
    tags = models.ManyToManyField(
        Disciplina,
        related_name="disciplina_material",
        help_text="Disciplinas Relacionadas",
    )
    arquivo = models.FileField(u"Arquivo", upload_to="uploads/arquivos/")

    class Meta:
        verbose_name = u"Material de Apoio"
        verbose_name_plural = u"Materiais de Apoio"

    def filename(self):
        return os.path.basename(self.arquivo.name)


class Aluno(models.Model):
    user = models.ForeignKey(User, blank=False, null=True, editable=False)
    curso = models.CharField(u"Curso", choices=CURSOS_CHOICE, max_length=100)
    disciplinas = models.ManyToManyField(
        Disciplina,
        related_name="aluno_disciplinas",
        help_text="Disciplinas que o aluno irá estudar",
    )

    avatar = models.ImageField(
        u"Imagem do Aluno", upload_to="uploads/alunos/avatar/", blank=True, null=True
    )

    class Meta:
        verbose_name = u"Aluno"
        verbose_name_plural = u"Alunos"

    def __unicode__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(u"Nome do Projeto", max_length=200, null=False, blank=False)
    bolsista = models.ManyToManyField(
        Aluno, related_name="alunos_projeto", help_text="Alunos pertecentes ao Projeto"
    )


class Aviso(models.Model):
    data = models.DateField(default=datetime.datetime.now, editable=False)
    descricao = models.TextField(u"Descrição")
    slug = models.SlugField(unique=True, max_length=100, editable=False, default="")
    anexo = models.FileField(u"Anexo", upload_to="uploads/anexo/")

    def save(self):
        self.slug = slugify(self.descricao)
        super(Aviso, self).save()
