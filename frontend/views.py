from django.shortcuts import render

# Create your views here.


# frontend/views.py
from django.shortcuts import render

# 1. الدالة الخاصة بالصفحة الرئيسية (التي ستفتح index.html)
def index_view(request):
    """
    تفتح ملف index.html
    """
    return render(request, 'index.html')

# 2. الدالة الخاصة بلوحة تحكم المنفذ (التي ستفتح performer_dashboard.html)
def dashboard_view(request):
    """
    تفتح ملف performer_dashboard.html
    """
    return render(request, 'performer_dashboard.html')

# 3. مثال لدالة تفتح صفحة داخل الداشبورد
def financials_view(request):
    """
    تفتح ملف financials_payouts.html
    """
    return render(request, 'financials_payouts.html')

# يمكنك إضافة دوال أخرى بنفس الطريقة للصفحات المتبقية



def our_services_view(request):
    return render(request, 'Our_services.html')

def about_us_view(request):
    return render(request, 'About_us.html')

def pricing_view(request):
    return render(request, 'pricing.html')
    
def faq_view(request):
    return render(request, 'faq.html')
    
def make_order_view(request):
    return render(request, 'make an order.html') # انتبه لاسم الملف

# دوال الداشبورد الفرعية
def delivery_history_view(request):
    return render(request, 'delivery_history.html')

def active_assignments_view(request):
    return render(request, 'active_assignments.html')

def job_market_view(request):
    return render(request, 'job_market_full.html')