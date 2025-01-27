import csv
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch

class Command(BaseCommand):
    help = 'Load bank and branch data from a CSV file'

    def handle(self, *args, **kwargs):
        file_path = 'data/bank_branches.csv'  
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: 
                bank, _ = Bank.objects.get_or_create(
                    id=row['bank_id'],
                    name=row['bank_name']
                ) 
                Branch.objects.get_or_create(
                    bank=bank,
                    ifsc=row['ifsc'],
                    branch_name=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
