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

    stat1 = models.PositiveIntegerField(default=0)
    stat2 = models.PositiveIntegerField(default=0)
    stat3 = models.PositiveIntegerField(default=0)
    stat4 = models.PositiveIntegerField(default=0)
    stat5 = models.PositiveIntegerField(default=0)

    equip_stat1 = models.PositiveIntegerField(default=0)
    equip_stat2 = models.PositiveIntegerField(default=0)
    equip_stat3 = models.PositiveIntegerField(default=0)
    equip_stat4 = models.PositiveIntegerField(default=0)
    equip_stat5 = models.PositiveIntegerField(default=0)


    def __str__(self):
        return "profile of a user: {}".format(self.name, self.profile_user.username)

    def update_lvl(self):
        if self.xp0 >= self.xp1:
            self.lvl_up()
        if self.xp0 >= self.xp1:
            self.update_lvl()

    def lvl_up(self):
        self.lvl += 1
        self.xp1 = self.xp1 + self.xp1*19/18 