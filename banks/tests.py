from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Bank, Branch

class BankAPITestCase(APITestCase):
    def setUp(self):
        # Create test data
        self.bank1 = Bank.objects.create(id=1, name="Test Bank 1")
        self.bank2 = Bank.objects.create(id=2, name="Test Bank 2")
        
        self.branch1 = Branch.objects.create(
            bank=self.bank1,
            ifsc="TEST0001",
            branch_name="Branch 1",
            address="123 Test Street",
            city="Test City",
            district="Test District",
            state="Test State"
        )
        
        self.branch2 = Branch.objects.create(
            bank=self.bank2,
            ifsc="TEST0002",
            branch_name="Branch 2",
            address="456 Test Avenue",
            city="Another City",
            district="Another District",
            state="Another State"
        )

    def test_get_banks_list(self): 
        # Test the /api/banks/ endpoint
        url = reverse('bank-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two banks created
        self.assertEqual(response.data[0]['name'], "Test Bank 1")
        print("/api/banks/ Passed")

    def test_get_branch_detail(self): 
        # Test the /api/branches/<ifsc>/ endpoint
        url = reverse('branch-detail', args=[self.branch1.ifsc])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['branch_name'], "Branch 1")
        self.assertEqual(response.data['bank_name'], "Test Bank 1")
        print("/api/branches/<ifsc>/ Passed")

    def test_nonexistent_branch(self): 
        url = reverse('branch-detail', args=["INVALID_IFSC"])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
        if response.status_code == status.HTTP_404_NOT_FOUND:
            print("/api/branches/<ifsc>/ Test Passed: Invalid IFSC returned 404")
        else:
            print("/api/branches/<ifsc>/ Test Failed: Expected 404 but got", response.status_code)


    def test_get_bank_branches(self):
        # Test the /api/banks/<id>/branches/ endpoint
        url = reverse('bank-branches', args=[self.bank1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one branch linked to bank1
        self.assertEqual(response.data[0]['branch_name'], "Branch 1")
        self.assertEqual(response.data[0]['bank_name'], "Test Bank 1")
        print("/api/banks/<id>/branches/ Passed")
