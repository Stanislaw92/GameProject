from inspect import GEN_RUNNING
from itertools import chain
import time
import random 

from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser


from django.http import JsonResponse

from api.permissions import haveNoProfileYet, IsAuthorOrReadyOnly, IsOwner, isProfileOwnerOrReadyOnly
from api.serializers import ProfileSerializer, ItemSerializer, TripResultSerializer, TextMessageSerializer, Combat1v1ResultSerializer
from profiles.models import Profile, Race, TextMessage, Combat1v1_result
from items.models import Item, item_prefix, item_base, item_sufix, Trip_result

import random

def addXP(profile, xp_to_add):
    profile.xp0 += xp_to_add

    errorCounter = 0
    while profile.xp0 > profile.xp1:
        profile.lvl += 1
        profile.xp0 = profile.xp0 - profile.xp1
        profile.xp1 = round((profile.xp1*19/18), 0)
        errorCounter += 1

        if errorCounter >= 10:
            break

    profile.save()

def itemRollFunction(pref_chance, suf_chance):
    bases = list(item_base.objects.all())
    prefixes = list(item_prefix.objects.all())
    sufixes = list(item_sufix.objects.all())
    prefixes.pop(0)
    sufixes.pop(0)
    list_for_base_roll = []
    list_for_pref_roll = []
    list_for_suf_roll = []

    for idx, item in enumerate(bases):
        for i in range(idx*3):
            list_for_base_roll.append(item)
    random.shuffle(list_for_base_roll)
    base_result = random.choice(list_for_base_roll)

    if random.randint(0, 10000) > pref_chance:
        for idx, item in enumerate(prefixes):
            for i in range(idx*3):
                list_for_pref_roll.append(item)
        random.shuffle(list_for_pref_roll)
        pref_result = random.choice(list_for_pref_roll)
    else:
        pref_result = item_prefix.objects.get(prefix_number=0)

    if random.randint(0, 10000) > suf_chance:
        for idx, item in enumerate(sufixes):
            for i in range(idx*3):
                list_for_suf_roll.append(item)
        random.shuffle(list_for_suf_roll)
        suf_result = random.choice(list_for_suf_roll)
    else:
        suf_result = item_sufix.objects.get(sufix_number=0)

    pref = pref_result
    base = base_result
    suf = suf_result

    return [pref, base, suf]


def Trip_results(user):
    profile = user.profile
    if random.randint(1, 101) < 50:
        result_list = []
        chance_for_drop = 150
        percentage = chance_for_drop % 100
        items_to_drop = (chance_for_drop - percentage) // 100

        if random.randint(1, 101) < percentage:
            items_to_drop += 1

        result_list = DropItem(profile, items_to_drop)

        trip_xp = random.choice(range(25,35))
        addXP(profile, trip_xp)

        return [True, result_list]
    else:
        return [False]



def DropItem(profile, drops_number):
    drop_list = []
    for i in range(drops_number):
        [x, y, z] = itemRollFunction(4000, 4000)

        #if add another item types ( for now its only 1 ), uncomment this method 
        # itemyTypeList = [1,2,3,4,5,6,7,8] #number of item types
        # random.shuffle(itemyTypeList)
        # item_type = random.choice(itemyTypeList)
        
        item_type = 1

        prefix = item_prefix.objects.get(
            item_type=item_type, prefix_number=x.prefix_number)
        base = item_base.objects.get(
            item_type=item_type, item_base_number=y.item_base_number)
        sufix = item_sufix.objects.get(
            item_type=item_type, sufix_number=z.sufix_number)

        new_item = Item(owner=profile, itemType=item_type, prefix=prefix, base=base, sufix=sufix)
        new_item.save()

        drop_list.append(new_item)
    
    return drop_list


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return Profile.objects.all().filter(profile_user=request_user).order_by("id")

class AllProfilesListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.all().order_by("-xp0")

class ProfileRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, isProfileOwnerOrReadyOnly]
    lookup_field = 'uuid'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, haveNoProfileYet]

    def perform_create(self, serializer):
        kwarg_race = self.kwargs.get('race')
        request_user = self.request.user
        race = Race.objects.get(race_id=kwarg_race)
        serializer.save(profile_user=request_user,
                        xp0=0, xp1=100, lvl=1, race=race)


class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return Item.objects.all().filter(owner__profile_user=request_user).order_by('created_at')


class EquippedItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user

        updateEquippedStats(request_user)

        return Item.objects.all().filter(owner__profile_user=request_user).filter(equipped=True).order_by('created_at')

class UnEquippedItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return Item.objects.all().filter(owner__profile_user=request_user).filter(equipped=False).order_by('created_at')



class ItemRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'uuid'


class ItemCreateAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        [x, y, z] = itemRollFunction(5000, 5000)
        prefix = item_prefix.objects.get(
            item_type=1, prefix_number=x.prefix_number)
        base = item_base.objects.get(
            item_type=1, item_base_number=y.item_base_number)
        sufix = item_sufix.objects.get(
            item_type=1, sufix_number=z.sufix_number)
        request_user = self.request.user
        serializer.save(owner=request_user.profile, itemType=1,
                        prefix=prefix, base=base, sufix=sufix)


class TripResultAPIView(generics.CreateAPIView):
    queryset = Trip_result.objects.all()
    serializer_class = TripResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        result = Trip_results(request_user)
        
        if result[0]:
            serializer.save(owner=request_user.profile, result=True, loot=result[1])
        else:
            serializer.save(owner=request_user.profile, result=False)


class TripResultsListAPIView(generics.ListAPIView):
    serializer_class = TripResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return Trip_result.objects.all().filter(owner__profile_user=request_user).order_by('created_at')


class TripResultRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip_result.objects.all()
    serializer_class = TripResultSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'uuid'


class AllTextMessagesListAPIView(generics.ListAPIView):
    serializer_class=TextMessageSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return TextMessage.objects.all().order_by('-created_at')

class InboxTextMessagesListAPIView(generics.ListAPIView):
    serializer_class = TextMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return TextMessage.objects.all().filter(reciever__profile_user=request_user).filter(deleted_reciever=False).filter(saved=False).order_by('created_at')


class OutTextMessagesListAPIView(generics.ListAPIView):
    serializer_class = TextMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return TextMessage.objects.all().filter(sender__profile_user=request_user).filter(deleted_sender=False).order_by('created_at')


class SavedTextMesageListAPIView(generics.ListAPIView):
    serializer_class = TextMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return TextMessage.objects.all().filter(reciever__profile_user=request_user).filter(saved=True).filter(deleted_reciever=False).order_by('created_at')


class TextMessageCreateAPIView(generics.CreateAPIView):
    queryset = TextMessage.objects.all()
    serializer_class = TextMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        kwarg_reciever_uuid = self.kwargs.get('uuid')
        reciever_profile = Profile.objects.get(uuid=kwarg_reciever_uuid)
        request_user = self.request.user
        serializer.save(sender=request_user.profile, saved=False, reciever=reciever_profile, deleted_sender=False, deleted_reciever=False, raport=False)


class TextMessageRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TextMessage.objects.all()
    serializer_class = TextMessageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'




def Combat1v1(attacker, opponent):

    print(attacker.dmg1)
    print(attacker.dmg2)
    attack_order = 0

    players = [attacker, opponent]

    fight_text = []

    player1_hp = attacker.hp
    player2_hp = opponent.hp
    rounds = 1

    winner = None 

    break_first_loop = False
    while rounds < 11 and break_first_loop == False:

        player1_attacks = attacker.attacks
        player2_attacks = opponent.attacks

        if attacker.initiative > opponent.initiative:
            attack_order = 0
        else:
            attack_order = 1

        #round loop
        while player1_attacks > 0 or player2_attacks > 0:

            if attack_order == 0:
                victim_reductions = 0
                dmg = random.randrange( players[0].dmg1, players[0].dmg2 + 1, 1 ) - victim_reductions

                print('dmg', dmg)

                fight_text.append('player {} attacks player {} with a weapon XXX for <b>{}</b>'.format(players[0], players[1], dmg))
                
                player1_attacks -= 1
                print('attacker atttacks = ', player1_attacks)
                player2_hp -= dmg

                attack_order = 1
                
            else:
                dmg = random.randrange( players[1].dmg1, players[1].dmg2+1, 1 )
                fight_text.append('player {} attacks player {} with a weapon XXX for <b>{}<b>'.format(players[1], players[0], dmg))

                player2_attacks -= 1
                player1_hp -= dmg
                print('opponent atttacks = ', player2_attacks)

                attack_order = 0

            if player1_hp <= 0:
                winner = opponent
                break_first_loop = True
                break
            elif player2_hp <= 0: 
                winner = attacker
                break_first_loop = True
                break
            elif player1_hp <= 0 and player2_hp <= 0:
                winner = 'draw'
                break_first_loop = True
                break
            
        rounds += 1
        fight_text.append('end of round')
        # fight_text.append('--------------------------------------------------------------------')

    
    # if player1_hp <= 0 and player2_hp > 0:
    #     fight_text.append('winner is player {}'.format(players[1].name))
    # elif player2_hp <= 0 and player1_hp > 0:
    #     fight_text.append('winner is player {}'.format(players[0].name))
    # else:
    #     fight_text.append('its a draw')

    

    return [winner, fight_text]
    




class Combat1v1ResultAPIView(generics.CreateAPIView):
    queryset = Combat1v1_result.objects.all()
    serializer_class = Combat1v1ResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        kwarg_victim_uuid = self.kwargs.get('uuid')

        opponent_profile = get_object_or_404(Profile, uuid=kwarg_victim_uuid)
        print('opponent_profile', opponent_profile)

        request_user = self.request.user

        [winner, result_text]  = Combat1v1(request_user.profile, opponent_profile)



        serializer.save(result=result_text, attacker=request_user.profile, victim=opponent_profile, winner=winner)


class Combat1v1ResultRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combat1v1_result.objects.all()
    serializer_class = Combat1v1ResultSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

class Combat1v1ResultListAPIView(generics.ListAPIView):
    serializer_class = Combat1v1ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user

        offensive_array = Combat1v1_result.objects.all().filter(attacker=request_user.profile).order_by('created_at')

        defensive_array = Combat1v1_result.objects.all().filter(victim=request_user.profile).order_by('created_at')

        model_combination = list(chain(offensive_array, defensive_array))

        return model_combination



def updateEquippedStats(user_object):
    items = Item.objects.all().filter(owner__profile_user=user_object).filter(equipped=True).order_by('created_at')

    user_profile = user_object.profile   

    user_profile.equip_stat1 = 0
    user_profile.equip_stat2 = 0
    user_profile.equip_stat3 = 0
    user_profile.equip_stat4 = 0
    user_profile.equip_stat5 = 0
    user_profile.equip_critical_strike = 0
    user_profile.equip_critical_strike_dmg_mod = 0
    user_profile.equip_armor = 0
    user_profile.equip_hp = 0
    user_profile.equip_dmg1 = 0
    user_profile.equip_dmg2 = 0
    user_profile.equip_initiative = 0
    user_profile.equip_attacks = 0
    user_profile.equip_hit_mod = 0

    equip_stat1 = 0
    equip_stat2 = 0
    equip_stat3 = 0
    equip_stat4 = 0
    equip_stat5 = 0
    equip_critical_strike = 0
    equip_critical_strike_dmg_mod = 0
    equip_armor = 0
    equip_hp = 0
    equip_dmg1 = 0
    equip_dmg2 = 0
    equip_initiative = 0
    equip_attacks = 0
    equip_hit_mod = 0


    for item in items:
            equip_stat1 += (item.prefix.stat1 + item.base.stat1 + item.sufix.stat1)
            equip_stat2 += (item.prefix.stat2 + item.base.stat2 + item.sufix.stat2)
            equip_stat3 += (item.prefix.stat3 + item.base.stat3 + item.sufix.stat3)
            equip_stat4 += (item.prefix.stat4 + item.base.stat4 + item.sufix.stat4)
            equip_stat5 += (item.prefix.stat5 + item.base.stat5 + item.sufix.stat5)
            equip_critical_strike += (item.prefix.equip_critical_strike + item.base.equip_critical_strike + item.sufix.equip_critical_strike)
            equip_critical_strike_dmg_mod += (item.prefix.equip_critical_strike_dmg_mod + item.base.equip_critical_strike_dmg_mod + item.sufix.equip_critical_strike_dmg_mod)
            equip_armor+= (item.prefix.equip_armor + item.base.equip_armor + item.sufix.equip_armor)
            equip_hp += (item.prefix.hp + item.base.hp + item.sufix.hp)
            equip_dmg1 += (item.prefix.dmg1 + item.base.dmg1 + item.sufix.dmg1)
            equip_dmg2 += (item.prefix.equip_dmg2 + item.base.equip_dmg2 + item.sufix.dmg2)
            equip_initiative += (item.prefix.initiative + item.base.initiative + item.sufix.initiative)
            equip_attacks += ( item.prefix.attacks + item.base.attacks + item.sufix.attacks)
            equip_hit_mod += (item.prefix.equip_hit_mod + item.base.hit_mod + item.sufix.hit_mod)


    user_profile.equip_stat1 = equip_stat1
    user_profile.equip_stat2 = equip_stat2
    user_profile.equip_stat3 = equip_stat3
    user_profile.equip_stat4 = equip_stat4
    user_profile.equip_stat5 = equip_stat5
    user_profile.equip_critical_strike = equip_critical_strike
    user_profile.equip_critical_strike_dmg_mod = equip_critical_strike_dmg_mod
    user_profile.equip_armor = equip_armor
    user_profile.equip_hp = equip_hp
    user_profile.equip_dmg1 = equip_dmg1
    user_profile.equip_dmg2 = equip_dmg2
    user_profile.equip_initiative = equip_initiative
    user_profile.equip_attacks = equip_attacks
    user_profile.equip_hit_mod = equip_hit_mod

    user_profile.save()