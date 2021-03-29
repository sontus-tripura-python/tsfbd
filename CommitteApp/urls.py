from django.urls import path
from CommitteApp import views
 
urlpatterns = [
     path('brancch-category/', views.branch_categories, name='branch_categories'),
     path('branch-category-form/', views.branch_categories_form, name='branch_categories_form'),
     path('branch-category-update/<slug:slug>/<int:pk>/', views.branch_categories_updated, name='branch_categories_updated'),
     path('branch-category-delete/<slug:slug>/<int:pk>/', views.branch_categories_delete, name='branch_categories_delete'),
     path('branch-name/<slug:slug>/<int:pk>/', views.branch_name, name='branch_name'),
     path('branch-name-form/<slug:slug>/<int:pk>/', views.branch_name_form, name='branch_name_form'),
    path('branch-name-update/<slug:slug>/<int:pk>/', views.branch_name_update, name='branch_name_update'),
    path('branch-name-delete/<slug:slug>/<int:pk>/', views.branch_name_delete, name='branch_name_delete'),
    path('branch-year/<slug:slug>/<int:pk>/', views.branch_year_list, name='branch_year_list'),
     path('branch-year-form/<slug:slug>/<int:pk>/', views.branch_year_create_form, name='branch_year_create_form' ),
     path('branch-year-update/<slug:slug>/<int:pk>/', views.branch_year_update, name='branch_year_update'),
   path('branch-year-delete/<slug:slug>/<int:pk>', views.branch_year_delete, name='branch_year_delete'),
   path('branch-year/member/<slug:slug>/<int:pk>/', views.branch_member, name='branch_member'),
   path('branch-member-detail/<slug:slug><int:pk>/', views.branch_leader_details, name='branch_leader_details'),
   path('add-member/<slug:slug>/<int:pk>/', views.add_member_form, name='add_member_form'),
    path('branch/<slug:slug>/<int:pk>/leader', views.branch_leader_details, name='branch_leader_details'),
    path('branch-member/delete/<slug:slug>/<int:pk>/', views.branch_member_delete, name='branch_member_delete'),
    path('branch-member-update/<slug:slug>/<int:pk>/', views.member_details_update, name='member_details_update'),
    #central leaders
     path('central-year/', views.central_years, name='central_years'),
    path('central-year-create/', views.central_year_form, name='central_year_form'),
    path('central-year-update/<slug:slug>/<int:pk>/', views.central_year_update, name='central_year_update'),
    path('central-year-delete/<slug:slug>/<int:pk>/', views.central_year_delete, name='central_year_delete'),
    path('central-member-create/<slug:slug>/<int:pk>/', views.central_member_form, name='central_member_form'),
    path('central-member-update/<slug:slug>/<int:pk>/', views.central_leader_update, name='central_leader_update'),
    path('central-member-delete/<slug:slug>/<int:pk>/', views.central_leader_delete, name='central_leader_delete'),
    path('central-leader/<slug:slug>/<int:pk>/', views.central_leader, name='central_leader'),
    path('central-leader-detail/<slug:slug>/<int:pk>/', views.central_leader_details, name='central_leader_details'),

    #co-ordinators
    path('co-ordinator/', views.co_ordinator_list, name='co_ordinator_list'),
    path('co-ordinator/<slug:slug>/<int:pk>/', views.co_ordinator_details, name='co_ordinator_details'),
    path('co-ordinator/create/', views.coordinator_create, name='coordinator_create'),
    path('co-ordinator-update/<slug:slug>/<int:pk>', views.coordinator_update, name='coordinator_update'),
    path('co-ordinator-delete/<slug:slug>/<int:pk>/', views.co_ordinator_delete, name='co_ordinator_delete'),
 ]