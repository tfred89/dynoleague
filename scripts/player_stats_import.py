from django.conf import settings
import pandas as pd
'''
MAKE SURE THE MODEL/TABLE HAS SAME NAMED COLUMNS AS CSV
'''
file = 'ff2019stats.csv'

df = pd.read_csv(file, header=0, index_col=0)

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name,
)

engine = create_engine(database_url, echo=False)
df.to_sql(HistoricalPrices, con=engine)