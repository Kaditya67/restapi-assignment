# banks/views.py
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

# List all banks
class BankListView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


# Get branch details by IFSC
class BranchDetailView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'  # Filter branches by the `ifsc` field
