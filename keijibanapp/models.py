from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import AbstractUser


GENDER_CHOICE=[["male","男性"],["female","女性"]]
ADDRESS_CHOICE=[[0,"北海道"]]



class User(AbstractUser):

    age = models.IntegerField('年齢',validators=[MinValueValidator(0),MaxValueValidator(150)])
    sex = models.CharField('性別',
        max_length=10,
        choices = GENDER_CHOICE,
    )
    address = models.CharField('都道府県',
        max_length=10,
        choices = ADDRESS_CHOICE,
        null=True,blank=True,
        )
    icon = models.ImageField(upload_to="",null=True,blank=True)





class Keijiban(models.Model) :
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    toukou = models.TextField('投稿内容')
    image = models.ImageField(upload_to="",null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    good = models.IntegerField(null=True,blank=True)
