from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Profile(models.Model):
    M_or_F = (
    ('남', '남'),
    ('여', '여'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('이름', max_length=5)
    major = models.CharField('학과', max_length=30)
    phone_number = models.CharField('전화번호', max_length=20)
    m_or_f = models.CharField('성별', choices=M_or_F, max_length=2)
    email = models.EmailField('이메일', max_length=254)
from django.utils import timezone
# Create your models here.
class ApllyForm(models.Model):
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    introduce = models.TextField('자기소개', max_length=1000)
    position = models.TextField('역할상상', max_length=500)
    goal = models.TextField('목표', max_length=500)
    plan = models.TextField('계획', max_length=500)
    team = models.TextField('팀활동', max_length=500)
    concept = models.TextField('컨셉', max_length=500)

    portfolio = models.FileField('포폴', blank= True, upload_to='portfolio/')
    interview = models.CharField('면접', max_length=255)
    experience = models.TextField('경험', max_length=1000)
    schedule = models.TextField('고정스케줄', max_length=1000)

    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
