from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankListView(ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchDetailView(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'   

class BankBranchesListView(ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        bank_id = self.kwargs['pk']
        return Branch.objects.filter(bank_id=bank_id)