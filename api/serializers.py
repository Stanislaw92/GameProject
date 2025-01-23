from rest_framework import serializers

from profiles.models import Profile, TextMessage, Combat1v1_result
from items.models import Item, Trip_result, item_base, item_prefix, item_sufix

class ProfileSerializer(serializers.ModelSerializer):
    race = serializers.SerializerMethodField()

    class Meta: 
        model = Profile
        fields = ['name', 'race', 'id', 'xp0', 'xp1', 'lvl', 'uuid','stat1', 'stat2','stat3','stat4','stat5', 'equip_stat1', 'equip_stat2','equip_stat3','equip_stat4','equip_stat5','trips', 'photo', 'training_points', 'trip_cooldown', 'ranking_place']
        
    def get_race(self, instance):
        return instance.race.name


class itemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = item_base
        fields = '__all__'

class itemPrefixSerializer(serializers.ModelSerializer):
    class Meta:
        model = item_prefix
        fields = '__all__'

class itemSufixSerializer(serializers.ModelSerializer):
    class Meta:
        model = item_sufix
        fields = '__all__'




class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    name = serializers.SerializerMethodField()
    item_type = serializers.StringRelatedField()
    # base = serializers.SerializerMethodField()
    base = itemBaseSerializer()
    base_num = serializers.SerializerMethodField()
    # prefix = serializers.SerializerMethodField()
    prefix = itemPrefixSerializer()
    prefix_num = serializers.SerializerMethodField()
    # sufix = serializers.SerializerMethodField()
    sufix = itemSufixSerializer()
    sufix_num = serializers.SerializerMethodField()
    itemType = serializers.StringRelatedField()
    # equipped = serializers.StringRelatedField()
    overall_stats = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = '__all__'

    def get_name(self, instance):
        if instance.itemType == 1:
            return '{} {} {} {} {}'.format(instance.itemType, instance.base.type_of_wep, instance.prefix.name, instance.base.name, instance.sufix.name)
        else:
            return '{} {} {} {}'.format(instance.itemType, instance.prefix.name, instance.base.name, instance.sufix.name)

    def get_base_num(self, instance):
        return instance.base.item_base_number

    def get_prefix_num(self, instance):
        return instance.prefix.prefix_number

    def get_sufix_num(self, instance):
        return instance.sufix.sufix_number
    
    def get_overall_stats(self, instance):
        list_of_stats = []


        dmg1_value = instance.prefix.dmg1 + instance.base.dmg1 + instance.sufix.dmg1
        dmg2_value = instance.prefix.dmg2 + instance.base.dmg2 + instance.sufix.dmg2

        if (instance.base.item_type == 1):
            list_of_stats.append(['dmg', dmg1_value, dmg2_value])
            # list_of_stats.append(['dmg2', dmg2_value])
        elif (dmg1_value != 0 & dmg2_value != 0):
            list_of_stats.append(['dmg', dmg1_value, dmg2_value])
        elif (dmg1_value != 0 & dmg2_value == 0):
            list_of_stats.append(['dmg', dmg1_value])
        elif (dmg1_value == 0 & dmg2_value != 0):
            list_of_stats.append(['dmg', 0, dmg2_value])
             
        

        
        
        
        stat1_value = instance.prefix.stat1 + instance.base.stat1 + instance.sufix.stat1
        if  stat1_value != 0:
            list_of_stats.append(['stat1', stat1_value])
        stat2_value = instance.prefix.stat2 + instance.base.stat2 + instance.sufix.stat2
        if  stat2_value != 0:
            list_of_stats.append(['stat2', stat2_value])
        stat3_value = instance.prefix.stat3 + instance.base.stat3 + instance.sufix.stat3
        if  stat3_value != 0:
            list_of_stats.append(['stat3', stat3_value])
        stat4_value = instance.prefix.stat4 + instance.base.stat4 + instance.sufix.stat4
        if  stat4_value != 0:
            list_of_stats.append(['stat4', stat4_value])
        stat5_value = instance.prefix.stat5 + instance.base.stat5 + instance.sufix.stat5
        if  stat5_value != 0:
            list_of_stats.append(['stat5', stat5_value])
        


        
        return list_of_stats




class TripResultSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    result = serializers.StringRelatedField()
    loot = ItemSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     loot_data = validated_data.pop('loot')
    #     print(loot_data)
    #     trip_result = Trip_result.objects.create(**validated_data)
    #     for item in loot_data:
    #         created_item = Item.objects.get_or_create(name=item)
    #         trip_result.loot.add(created_item)
        # return trip_result

    class Meta:
        model = Trip_result
        fields = ['owner', 'loot', 'result', 'uuid','created_at', 'new', 'saved']


class TextMessageSerializer(serializers.ModelSerializer):
    
    sender = serializers.SerializerMethodField()
    reciever = serializers.SerializerMethodField()

    # saved = serializers.StringRelatedField()
    sender_uuid = serializers.SerializerMethodField()
    reciever_uuid = serializers.StringRelatedField()
    # text = serializers.StringRelatedField()
    # title = serializers.StringRelatedField()

    # owner = serializers.SerializerMethodField()
    # new = serializers.StringRelatedField()


    def get_sender_uuid(self, instance):
        if instance.sender:
            return instance.sender.uuid
        else:
            return "Raport"

    def get_reciever_uuid(self, instance):
        return instance.reciever.uuid
 
    def get_sender(self, instance):
        if instance.sender:
            print(instance.sender)
            return instance.sender.name
        else:
            return '----'

    def get_reciever(self, instance):
        return instance.reciever.name


    class Meta:
        model = TextMessage
        fields = ['sender', 'reciever','text', 'title','new', 'deleted_sender', 'deleted_reciever', 'uuid', 'reciever_uuid', 'sender_uuid', 'saved', 'created_at']


class Combat1v1ResultSerializer(serializers.ModelSerializer):
    
    attacker = serializers.SerializerMethodField()
    victim = serializers.SerializerMethodField()

    # saved = serializers.StringRelatedField()
    attacker_uuid = serializers.SerializerMethodField()
    victim_uuid = serializers.SerializerMethodField()
    # text = serializers.StringRelatedField()
    # title = serializers.StringRelatedField()
    result = serializers.StringRelatedField()

    winner = serializers.SerializerMethodField()
    # new = serializers.StringRelatedField()


    def get_attacker_uuid(self, instance):
        return instance.attacker.uuid

    def get_victim_uuid(self, instance):
        return instance.victim.uuid

    def get_attacker(self, instance):
        return instance.attacker.name

    def get_victim(self, instance):
        return instance.victim.name


    def get_winner(self, instance):
        return instance.winner.name

    class Meta:
        model = Combat1v1_result
        fields = ['attacker', 'victim','result', 'uuid', 'attacker_uuid', 'victim_uuid', 'winner', 'created_at', 'new', 'saved','deleted_sender', 'deleted_reciever']