import csv
from users.models import User 

def save_data():
    with open('./utilities/data.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if row != ['first_name', 'last_name', 'password', 'username', 'email']:
                if not User.objects.get(email=row[4]):
                    User.objects.create_user(
                    first_name=row[0],
                    last_name=row[1],
                    password=row[2],
                    username=row[3],
                    email=row[4],
                    is_active = True,
                    )
                