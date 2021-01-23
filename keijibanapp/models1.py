from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User


GENDER_CHOICE=[["male","男性"],["female","女性"]]



class Profile(models.Model):
    name = models.CharField('ユーザー名',max_length=10)
    age = models.IntegerField('年齢',validators=[MinValueValidator(0),MaxValueValidator(150)])
    sex = models.CharField('性別',
        max_length=10,
        choices = GENDER_CHOICE,
    )
    image = models.ImageField(upload_to="",null=True,blank=True)
    def __str__(self) :
        return self.name




class Keijiban(models.Model) :
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    toukou = models.TextField('投稿内容')
    created_at = models.DateTimeField(default=timezone.now)
    good = models.IntegerField(null=True,blank=True)
