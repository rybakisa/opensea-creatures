from django.urls import path

from . import views


app_name = 'creature'
urlpatterns = [
    path('contract/<str:contract_name>/', views.contract, name='contract'),

    path('api/creature/<int:token_id>/', views.creature, name='creature'),
    path('api/accessory/<int:token_id>/', views.accessory, name='accessory'),

    path('api/box/creature/<int:token_id>/', views.creature_box, name='creature_box'),
    path('api/box/accessory/<int:token_id>/', views.accessory_box, name='accessory_box'),

    path('api/factory/creature/<int:token_id>/', views.creature_factory, name='creature_factory'),
    path('api/factory/accessory/<int:token_id>/', views.accessory_factory, name='accessory_factory'),
]