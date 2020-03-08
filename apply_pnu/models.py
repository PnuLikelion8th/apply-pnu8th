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

    def __str__(self):
        return self.name

from django.utils import timezone
# Create your models here.
class ApplyForm(models.Model):
    author = models.OneToOneField(Profile, on_delete=models.CASCADE)
    introduce = models.TextField('자기소개 및 지원동기(최대 1000자)', max_length=1000)
    position = models.TextField('기획자/개발자/디자이너 중 가장 본인에게 가깝다고 생각하는 것을 고르고, 관련 근거를 서술하시오(최대 500자)', max_length=500)
    goal = models.TextField('코딩을 배워서 무엇을 하고 싶은지 구체적으로 서술하시오(최대 500자)', max_length=500)
    plan = models.TextField('향후 1년계획 (학생회,동아리,아르바이트 등 최대 500자)', max_length=500)
    team = models.TextField('참여했던 팀 활동 중 가장 기억에 남는 경험과 느낌점을 서술하시오(최대500자)', max_length=500)
    concept = models.TextField('본인은 멋쟁이사자처럼 동아리내 어떤 캐릭터일지 서술하시오(최대 500자)', max_length=500)

    portfolio = models.FileField('본인을 나타낼 수 있는 포트폴리오를 첨부해주세요(URL의 경우 캡쳐후 첨부)', blank= True, upload_to='portfolio/')
    interview = models.TextField('면접가능시간( 3월 28일(토), 3월 29일(일) )을 작성해주세요', max_length=255)
    experience = models.TextField('프로그래밍 경험이 있다면 기술스택과 수준을, 프로그래밍 경험이 없다면 기대감과 각오를 적어주세요', max_length=1000)
    schedule = models.TextField('1학기 고정스케줄(요일&시간)', max_length=1000)

    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.introduce
