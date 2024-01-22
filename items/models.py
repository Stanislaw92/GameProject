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

    type_of_wep = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    prefix_pic = models.ImageField(
        default='0.png', upload_to='prefix_pics', blank=True)
    name = models.TextField(max_length=20, blank=False, default="")

    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=0)
    dmg2 = models.PositiveIntegerField(default=0)
    initiative = models.PositiveIntegerField(default=0)
    hit_mod = models.PositiveIntegerField(default=0)
    attacks = models.PositiveIntegerField(default=0)
    
    stat1 = models.PositiveIntegerField(default=0)
    stat2 = models.PositiveIntegerField(default=0)
    stat3 = models.PositiveIntegerField(default=0)
    stat4 = models.PositiveIntegerField(default=0)
    stat5 = models.PositiveIntegerField(default=0)


    def __str__(self):
        if self.item_type == 1 or self.item_type == 2:
            return itemTypes[self.item_type] + '({})'.format(self.item_type) + ' ' + typeOfWeps[self.type_of_wep]+'({})'.format(self.type_of_wep) + ' prefix: ' + self.name
        else:
            return itemTypes[self.item_type]+'({})'.format(self.item_type) + ' prefix: ' + self.name

    class Meta:
        ordering = ['item_type', 'prefix_number']
        unique_together = ['prefix_number', 'item_type', 'type_of_wep']
        verbose_name_plural = "item prefixes"

itemTypes = {
    0: 'None',
    1: 'mainhand',
    2: 'offhand',
    3: 'chest',
    4: 'legs',
    5: 'rings',
    6: 'necklacle',
    7: 'head',
    8: 'shoes',
}


typeOfWeps = {
    0: 'not weapon',
    1: '1h meele',
    2: '2h meele',
    3: 'shield',
    4: '1h firearm',
    5: '2h firearm',
    6: 'ranged weapon',
}



class item_base(models.Model):
    item_base_number = models.PositiveSmallIntegerField(
        default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(15)])


    #Type of item depending of the slot in armory
    item_type = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])


    #type of weapon for example gun, 2h gun, meele wep, 2h meele wep etc, if= itemy_type != 1: type_of_wep=0
    type_of_wep = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    
    item_base_pic = models.ImageField(
        default='0.png', upload_to='base_pics', blank=True)
    name = models.TextField(max_length=20, blank=False, default="")


    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=0)
    dmg2 = models.PositiveIntegerField(default=0)
    initiative = models.PositiveIntegerField(default=0)
    hit_mod = models.PositiveIntegerField(default=0)
    attacks = models.PositiveIntegerField(default=0)

    stat1 = models.PositiveIntegerField(default=0)
    stat2 = models.PositiveIntegerField(default=0)
    stat3 = models.PositiveIntegerField(default=0)
    stat4 = models.PositiveIntegerField(default=0)
    stat5 = models.PositiveIntegerField(default=0)

    def __str__(self):
        if self.item_type == 1 or self.item_type == 2:
            return itemTypes[self.item_type]+'({})'.format(self.item_type) + ' ' + typeOfWeps[self.type_of_wep]+'({})'.format(self.type_of_wep) + ' base: ' + self.name
        else:
            return itemTypes[self.item_type]+'({})'.format(self.item_type) + ' base: ' + self.name

    class Meta:
        ordering = ['item_type', 'item_base_number']
        unique_together = ['item_base_number', 'item_type', 'type_of_wep']
        verbose_name_plural = "Item bases"


class item_sufix(models.Model):
    sufix_number = models.PositiveSmallIntegerField(
        default=0, null=False, validators=[MinValueValidator(0), MaxValueValidator(15)])
    item_type = models.PositiveSmallIntegerField(null=True, default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    sufix_pic = models.ImageField(
        default='0.png', upload_to='sufix_pics', blank=True)
    type_of_wep = models.PositiveSmallIntegerField(default=0, blank=False, validators=[
                                                 MinValueValidator(0), MaxValueValidator(15)])
    name = models.TextField(max_length=20, blank=False, default="")


    stat1 = models.PositiveIntegerField(default=0)
    stat2 = models.PositiveIntegerField(default=0)
    stat3 = models.PositiveIntegerField(default=0)
    stat4 = models.PositiveIntegerField(default=0)
    stat5 = models.PositiveIntegerField(default=0)

    critical_strike  = models.PositiveIntegerField(default=0)
    critical_strike_dmg_mod = models.PositiveIntegerField(default=0)
    armor = models.PositiveIntegerField(default=0)
    hp = models.PositiveIntegerField(default=0)
    dmg1 = models.PositiveIntegerField(default=0)
    dmg2 = models.PositiveIntegerField(default=0)
    initiative = models.PositiveIntegerField(default=0)
    hit_mod = models.PositiveIntegerField(default=0)
    attacks = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        if self.item_type == 1 or self.item_type == 2:
            return itemTypes[self.item_type]+'({})'.format(self.item_type) + ' ' + typeOfWeps[self.type_of_wep]+'({})'.format(self.type_of_wep) + ' sufix: ' + self.name
        else:
            return itemTypes[self.item_type]+'({})'.format(self.item_type) + ' sufix: ' + self.name

    class Meta:
            ordering = ['item_type', 'sufix_number']
            unique_together = ['sufix_number', 'item_type', 'type_of_wep']
            verbose_name_plural = "item sufixes"





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
        text = ' : {} {} {}'.format(x, self.base, y)
        text = text.strip()
        return itemTypes[self.itemType] + text


class Trip_result(TimeStampedModel):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='trip_result')
    loot = models.ManyToManyField(Item, blank=True)
    result = models.BooleanField(default=False)
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4,editable=False)
    new = models.BooleanField(default=True)
    saved = models.BooleanField(default=False)

    def __str__(self):
        return 'trip no {}'.format(self.uuid)
