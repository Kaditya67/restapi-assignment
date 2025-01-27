from django.urls import path
from .views import BankListView, BranchDetailView, BankBranchesListView

urlpatterns = [
    path('banks/', BankListView.as_view(), name='bank-list'),  # List all banks
    path('banks/<int:pk>/branches/', BankBranchesListView.as_view(), name='bank-branches'),  
    path('branches/<str:ifsc>/', BranchDetailView.as_view(), name='branch-detail'),  
]
