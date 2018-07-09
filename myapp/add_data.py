import csv
from collections import namedtuple

from main_project.settings import BASE_DIR
from myapp.models import UserData

csv_filename = BASE_DIR + '/data/adult_data.csv'

AdultDataObj = namedtuple('ADObj', 'age workplace fnlwgt education education_num marital_status occupation relationship race sex capital_gain capital_loss hours_per_week native_country')

def add_data():
    if not UserData.objects.all():
        file_csv = open(BASE_DIR + '/data/adult_data.csv')
        reader = csv.reader(file_csv)
        header = next(reader)
        
        result = [
            UserData(
                age=int(row[0].rstrip().strip()), # age (int)
                workplace=row[1].rstrip().strip(), # workplace (str)
                fnlwgt=int(row[2].rstrip().strip()), # fnlwgt (int)
                education=row[3].rstrip().strip(), # education (str)
                education_num=int(row[4].rstrip().strip()), # education_num (int)
                marital_status=row[5].rstrip().strip(), # marital_status (str)
                occupation=row[6].rstrip().strip(), # occupation (str)
                relationship=row[7].rstrip().strip(), # relationship (str)
                race=row[8].rstrip().strip(), # race (str)
                sex=row[9].rstrip().strip(), # sex (str)
                capital_gain=int(row[10].rstrip().strip()), # capital_gain (int)
                capital_loss=int(row[11].rstrip().strip()), # capital_loss (int)
                hours_per_week=int(row[12].rstrip().strip()), # hours_per_week (int)
                native_country=row[13].rstrip().strip(), # native_country (str)
            )
            for row in reader
        ]
        UserData.objects.bulk_create(result)
        file_csv.close()
    else:
        print("USER DATA ALREADY INSERTED.")