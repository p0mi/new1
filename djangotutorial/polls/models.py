from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User



class Roles(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'


class Protocol(models.TextChoices):
    RDP = 'rdp', 'RDP'
    SSH = 'ssh', 'SSH'
    VNC = 'vnc', 'VNC'
    


# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    """ Краткое описание класса. Более подробное описание класса, если необходимо. Attributes: attr1 (str): Описание атрибута. attr2 (int): Описание атрибута. Methods: method1(param1, param2): Описание метода. Args: param1 (int): Описание параметра. param2 (str): Описание параметра. Returns: str: Описание возвращаемого значения. Raises: ValueError: Если параметр param1 меньше 0. """

    def __init__(self, attr1, attr2):
        """ Конструктор класса. Args: attr1 (str): Описание атрибута. attr2 (int): Описание атрибута. """
        self.attr1 = attr1
        self.attr2 = attr2

    def method1(self, param1, param2):
        """ Описание метода. Args: param1 (int): Описание параметра. param2 (str): Описание параметра. Returns: str: Описание возвращаемого значения. Raises: ValueError: Если параметр param1 меньше 0. """
        if param1 < 0:
            raise ValueError("param1 must be non-negative")
        return f"{param1} {param2}"



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     password_hash = models.CharField(max_length=64)
#     role = models.CharField(
#         max_length=50,
#         choices=Roles.choices,
#         default="User",
#     )

class Virtuals(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )
    hostname = models.CharField(max_length=32)
    protocol = models.CharField(
        max_length=5,
        choices=Protocol.choices
    )
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=128)
    port = models.IntegerField()
    user_vm = models.CharField(max_length=64)
    password_vm = models.CharField(max_length=128)
    ignore_cert = models.BooleanField()

class Audit_log(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )
    action = models.CharField(max_length=32)
    time = models.DateTimeField(auto_now_add=True)
    virtual_id = models.ForeignKey(
        Virtuals,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

