# frontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # الصفحات الرئيسية
    path('', views.index_view, name='home'),
    path('services/', views.our_services_view, name='our_services'),
    path('about/', views.about_us_view, name='about_us'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('faq/', views.faq_view, name='faq'),
    path('order/', views.make_order_view, name='make_order'),

    # روابط لوحة التحكم (Executor Dashboard)
    path('executor-dashboard/', views.dashboard_view, name='executor_dashboard'),
    path('executor-dashboard/market/', views.job_market_view, name='job_market'),
    path('executor-dashboard/active/', views.active_assignments_view, name='active_assignments'),
    path('executor-dashboard/history/', views.delivery_history_view, name='delivery_history'),
    path('executor-dashboard/financials/', views.financials_view, name='financials_payouts'),
]