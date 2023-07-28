from core.models import TimeStampedModel
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser
import uuid as uuid_lib

class Race(models.Model):
    name = models.TextField(max_length=15, blank=False, default="")
    race_id = models.PositiveSmallIntegerField(unique=True, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.name


class Profile(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4,editable=False)
    name = models.TextField(max_length=20, blank=False, default='')
    profile_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='profiles')

    xp0 = models.PositiveBigIntegerField(default=0)
    xp1 = models.PositiveBigIntegerField(default=100)
    lvl = models.PositiveSmallIntegerField(default=1)

    trips = models.PositiveSmallIntegerField(default=32, validators=[MinValueValidator(0), MaxValueValidator(32)])

    
    #Each stat in this section need to have exact the same in item prefix, item base and item sufix models in ./items/models.py
    stat1 = models.PositiveIntegerField(default=0)
    stat2 = models.PositiveIntegerField(default=0)
    stat3 = models.PositiveIntegerField(default=0)
    stat4 = models.PositiveIntegerField(default=0)
    stat5 = models.PositiveIntegerField(default=0)


    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=1)
    dmg2 = models.PositiveIntegerField(default=1)
    initiative = models.PositiveIntegerField(default=0)

    hit_mod = models.PositiveIntegerField(default=0)
    #////

    equip_stat1 = models.PositiveIntegerField(default=0)
    equip_stat2 = models.PositiveIntegerField(default=0)
    equip_stat3 = models.PositiveIntegerField(default=0)
    equip_stat4 = models.PositiveIntegerField(default=0)
    equip_stat5 = models.PositiveIntegerField(default=0)


    def __str__(self):
        return "profile of a user: {}".format(self.name, self.profile_user.username)

    def update_lvl(self, xp):
        lvl = self.lvl
        xp1 = self.xp1
        print(xp1, type(xp1), xp, type(xp))
        while xp > xp1:
            self.lvl_up()
        return lvl, xp1

    def lvl_up(self):
        lvl += 1
        xp1 = xp1 + xp1*19/18 


class TextMessage(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4,editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_sender')
    reciever = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg_reciever')

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='msg')

    text = models.TextField(blank=False, max_length=400)
    title = models.TextField(blank=False, max_length=40)

    new = models.BooleanField(default=True)



    class Meta:
        ordering = ['-created_at']