from django.db import models

# Create your models here.


class UserData(models.Model):


    age = models.IntegerField()
    workplace = models.CharField(max_length=100)
    fnlwgt = models.BigIntegerField()
    education = models.CharField(max_length=100)
    education_num = models.IntegerField()
    marital_status = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    capital_gain = models.IntegerField()
    capital_loss = models.IntegerField()
    hours_per_week = models.IntegerField()
    native_country = models.CharField(max_length=100)

    def to_json(self):
        return {
            'age': self.age,
            'workplace': self.workplace,
            'fnlwgt': self.fnlwgt,
            'education': self.education,
            'education_num': self.education_num,
            'marital_status': self.marital_status,
            'occupation': self.occupation,
            'relationship': self.relationship,
            'race': self.race,
            'sex': self.sex,
            'capital_gain': self.capital_gain,
            'capital_loss': self.capital_loss,
            'hours_per_week': self.hours_per_week,
            'native_country': self.native_country
        }
