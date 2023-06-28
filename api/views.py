from inspect import GEN_RUNNING
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import  IsAdminUser


from api.permissions import haveNoProfileYet, IsAuthorOrReadyOnly, IsOwner, isProfileOwnerOrReadyOnly
from api.serializers import ProfileSerializer, ItemSerializer
from profiles.models import Profile, Race
from items.models import Item, item_prefix, item_base, item_sufix

import random

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

    if random.randint(0,10000) > suf_chance:
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


class ProfileListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return Profile.objects.all().filter(profile_user=request_user).order_by("id")

class ProfileRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, isProfileOwnerOrReadyOnly]
    lookup_field = 'uuid'

class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, haveNoProfileYet]

    def perform_create(self, serializer):
        kwarg_race = self.kwargs.get('race')
        request_user = self.request.user
        race = Race.objects.get(race_id=kwarg_race)
        serializer.save(profile_user=request_user, xp0=0, xp1=100, lvl=1, race=race)

class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = self.request.user
        return Item.objects.all().filter(owner__profile_user = request_user).order_by('created_at')

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
        [x,y,z] = itemRollFunction(5000,5000)
        prefix = item_prefix.objects.get(item_type=1, prefix_number=x.prefix_number)
        base = item_base.objects.get(item_type=1, item_base_number=y.item_base_number)
        sufix = item_sufix.objects.get(item_type=1, sufix_number=z.sufix_number)
        request_user = self.request.user
        serializer.save(owner=request_user.profile, itemType=1, prefix=prefix, base=base, sufix=sufix)