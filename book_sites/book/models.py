from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Catalog(models.Model):
    #catalog_no = models.IntegerField()
    catalog = models.CharField(max_length=25)
    catalog_photo=models.CharField(max_length = 200, default='',blank=True)
    def __str__(self):
        return self.catalog

class Book(models.Model):
    #book_no=models.IntegerField()
    catalog=models.ForeignKey(Catalog)  #要改成ForeignKey
    #catalog=models.CharField(max_length=25)
    name=models.CharField(max_length=100)
    photo_url = models.CharField(max_length = 200, default='', blank=True)
    photo_zoom = models.CharField(max_length = 200, default='', blank=True)
    author=models.CharField(max_length=50)
    translator=models.CharField(max_length=50,null=True)
    publish_date=models.DateField(null=True)
    score=models.DecimalField(max_digits=2, decimal_places=1, default=0)
    synopsis=models.TextField(null=True)


    def __str__(self):
        return self.name

class Rating(models.Model):
    #https://github.com/twtrubiks/django-tutorial
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    # user_name = models.CharField('評分者姓名',max_length=100)
    # user = models.ForeignKey(MyUser, verbose_name='評分者', null=True)
    #user = models.ForeignKey(User, models.CASCADE, verbose_name='評分者', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='評分者', null=True)
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='書名')
    #book = models.ForeignKey(Book, models.CASCADE, verbose_name='書名')
    rating = models.FloatField('評分', choices=RATING_CHOICES)
    pub_date = models.DateTimeField('評分時間')
    comment = models.TextField('留言',max_length=200, blank =True )
    #likes = models.ManyToManyField(User)
    likes = models.IntegerField('讚', default=0)
    def get_rate(self):
        return self.rating
    def __str__(self):
        return self.user.username+","+self.book.name+":"+str(self.rating)


class Like(models.Model):
   comment = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name='留言')
   user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='按讚user')
   
   def __str__(self):
        return self.user.username+","+str(self.comment.id)

class UserProfile(models.Model):

    GENDER_CHOICES=(
        ('女','女'),
        ('男','男'),
        ('不想回答','不想回答'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='名稱', null=True, editable=False)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, default='女',verbose_name="性別")
    birth_day=models.DateField(null=True, blank=True, verbose_name="生日")
    location=models.CharField(max_length=30,blank=True, verbose_name="國家/城市")
    bio=models.TextField(max_length=500,blank=True, verbose_name="關於我")
    image=models.ImageField(upload_to='profile_img', blank=True, verbose_name="圖片")
    """docstring for UserProfile"""
    def __str__(self):
        return self.user.username
'''
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

'''
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''