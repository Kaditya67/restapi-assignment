# banks/urls.py
from django.urls import path
from .views import BankListView, BranchDetailView

urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank-list'),  # List all banks
    path('branches/<str:ifsc>/', BranchDetailView.as_view(), name='branch-detail'),  # Get branch by IFSC
]
