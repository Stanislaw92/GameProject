from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views as qv

urlpatterns = [

    path("profiles/", qv.ProfileListAPIView.as_view(), name="profiles-list"),
    path("all_profiles/", qv.AllProfilesListAPIView.as_view(),
         name="all-profiles-list"),
    path("profiles/<uuid:uuid>/",
         qv.ProfileRUDAPIView.as_view(), name="profiles-detail"),
    path("profiles/create/<int:race>/",
         qv.ProfileCreateAPIView.as_view(), name="profile-create"),

    path('items/', qv.ItemListAPIView.as_view(), name="items_list"),
    path('eqippedItems/', qv.EquippedItemListAPIView.as_view(),
         name="equipped_items_list"),
    path('unEqippedItems/', qv.UnEquippedItemListAPIView.as_view(),
         name="un_equipped_items_list"),
    path("items/<uuid:uuid>/", qv.ItemRUDAPIView.as_view(), name='item-detail'),
    path("items/create/", qv.ItemCreateAPIView.as_view(), name='item-create'),


    path('trip_results/', qv.TripResultsListAPIView.as_view(), name="trip_results"),
    path('trip_results/create/', qv.TripResultAPIView.as_view(), name="trip_result"),
    path('trip_results/<uuid:uuid>/', qv.TripResultRUDAPIView.as_view(), name="trip_results_details/"),

    

    path('txtmsg/all_of_them/', qv.AllTextMessagesListAPIView.as_view(), name="text_messages__list"),
    path('txtmsg/inbox/', qv.InboxTextMessagesListAPIView.as_view(), name="text_messages_inbox_list"),
    path('txtmsg/outbox/', qv.OutTextMessagesListAPIView.as_view(), name="text_messages_outbox_list"),
    path('txtmsg/saved/', qv.SavedTextMesageListAPIView.as_view(), name="text_messages_saved_list"),
    path('txtmsg/create/<uuid:uuid>/', qv.TextMessageCreateAPIView.as_view(), name="create_text_message"),
    path('txtmsg/<uuid:uuid>/', qv.TextMessageRUDAPIView.as_view(), name="ruda_text_message"),


    path('combat_result/', qv.Combat1v1ResultListAPIView.as_view(), name="combat1v1_results"),
    path('combat_result/<uuid:uuid>/', qv.Combat1v1ResultRUDAPIView.as_view(), name="ruda_combat1v1_result"),
    path('combat_result/attack/<uuid:uuid>/', qv.Combat1v1ResultAPIView.as_view(), name="combat1v1_create_result"),


    path('items_update/', qv.MultipleItemsUpdateAPIView.as_view(), name="multiple_items_update"),


    path('updatedPrefixes/', qv.addprefixes),

]
