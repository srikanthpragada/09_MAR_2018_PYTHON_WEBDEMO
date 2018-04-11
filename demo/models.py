from django.db import models


# Create your models here.

class Course:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def __str__(self):
        return "Course : %s, Fee = %d" % (self.name, self.fee)
