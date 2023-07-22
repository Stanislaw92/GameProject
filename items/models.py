from core.models import TimeStampedModel
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid as uuid_lib

from profiles.models import Profile

class item_prefix(models.Model):
    prefix_number = models.PositiveSmallIntegerField(
        default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(15)])
    item_type = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    prefix_pic = models.ImageField(
        default='0.png', upload_to='prefix_pics', blank=True)
    name = models.TextField(max_length=20, blank=False, default="")

    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=1)
    dmg2 = models.PositiveIntegerField(default=1)
    initiative = models.PositiveIntegerField(default=0)
    hit_mod = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['item_type', 'prefix_number']
        unique_together = ['prefix_number', 'item_type']
        verbose_name_plural = "prefixes"


class item_base(models.Model):
    item_base_number = models.PositiveSmallIntegerField(
        default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(15)])
    item_type = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    item_base_pic = models.ImageField(
        default='0.png', upload_to='base_pics', blank=True)
    name = models.TextField(max_length=20, blank=False, default="")


    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=1)
    dmg2 = models.PositiveIntegerField(default=1)
    initiative = models.PositiveIntegerField(default=0)
    hit_mod = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['item_type', 'item_base_number']
        unique_together = ['item_base_number', 'item_type']
        verbose_name_plural = "Item bases"


class item_sufix(models.Model):
    sufix_number = models.PositiveSmallIntegerField(
        default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(15)])
    item_type = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    sufix_pic = models.ImageField(
        default='0.png', upload_to='sufix_pics', blank=True)
    name = models.TextField(max_length=20, blank=False, default="")


    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=1)
    dmg2 = models.PositiveIntegerField(default=1)
    initiative = models.PositiveIntegerField(default=0)
    hit_mod = models.PositiveIntegerField(default=0)

    
    def __str__(self):
        return self.name

class Meta:
        ordering = ['item_type', 'sufix_number']
        unique_together = ['sufix_number', 'item_type']
        verbose_name_plural = "sufixes"


class Item(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4,editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='items_list', null=True)
    itemType = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])

    base = models.ForeignKey(item_base, on_delete=models.CASCADE, related_name="items_with_that_base")
    prefix = models.ForeignKey(item_prefix, on_delete=models.CASCADE, related_name="items_with_that_prefix")
    sufix = models.ForeignKey(item_sufix, on_delete=models.CASCADE, related_name="items_with_that_sufix")

    equipped = models.BooleanField(default=False)

    def __str__(self):
        if self.prefix.prefix_number == 0:
            x = ''
        else:
            x = self.prefix
        if self.sufix.sufix_number == 0:
            y = ''
        else:
            y = self.sufix
        text = 'item: {} {} {}'.format(x, self.base, y)
        text = text.strip()
        return text
