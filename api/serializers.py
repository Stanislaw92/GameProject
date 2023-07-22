from rest_framework import serializers

from profiles.models import Profile
from items.models import Item

class ProfileSerializer(serializers.ModelSerializer):
    race = serializers.SerializerMethodField()

    class Meta: 
        model = Profile
        fields = ['name', 'race', 'id', 'xp0', 'xp1', 'lvl', 'uuid','stat1', 'stat2','stat3','stat4','stat5', 'equip_stat1', 'equip_stat2','equip_stat3','equip_stat4','equip_stat5']
        
    def get_race(self, instance):
        return instance.race.name


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    name = serializers.SerializerMethodField()
    item_type = serializers.StringRelatedField()
    base = serializers.SerializerMethodField()
    base_num = serializers.SerializerMethodField()
    prefix = serializers.SerializerMethodField()
    prefix_num = serializers.SerializerMethodField()
    sufix = serializers.SerializerMethodField()
    sufix_num = serializers.SerializerMethodField()
    itemType = serializers.StringRelatedField()
    # equipped = serializers.StringRelatedField()

    class Meta:
        model = Item
        fields = ['owner', 'name','item_type','base','base_num','prefix','prefix_num','sufix','sufix_num','itemType', 'equipped', 'id', 'uuid']


    def get_name(self, instance):
        return '{} {} {} {}'.format(instance.itemType, instance.prefix.name, instance.base.name, instance.sufix.name)

    def get_base(self, instance):
        return instance.base.name

    def get_base_num(self, instance):
        return instance.base.item_base_number

    def get_prefix(self, instance):
        return instance.prefix.name

    def get_prefix_num(self, instance):
        return instance.prefix.prefix_number

    def get_sufix(self, instance):
        return instance.sufix.name

    def get_sufix_num(self, instance):
        return instance.sufix.sufix_number