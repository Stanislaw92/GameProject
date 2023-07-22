from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views as qv

urlpatterns = [
    path("profiles/", qv.ProfileListAPIView.as_view(), name="profiles-list"),
    path("all_profiles/", qv.AllProfilesListAPIView.as_view(), name="all-profiles-list"),
    path("profiles/<uuid:uuid>/", qv.ProfileRUDAPIView.as_view(), name="profiles-detail"),
    path("profiles/create/<int:race>/", qv.ProfileCreateAPIView.as_view(), name="profile-create"),

    path('items/', qv.ItemListAPIView.as_view(), name="items_list"),
    path('eqippedItems/', qv.EquippedItemListAPIView.as_view(), name="equipped_items_list"),
    path('unEqippedItems/', qv.UnEquippedItemListAPIView.as_view(), name="un_equipped_items_list"),
    path("items/<uuid:uuid>/",qv.ItemRUDAPIView.as_view(), name='item-detail'),
    path("items/create/",qv.ItemCreateAPIView.as_view(), name='item-create'),

]