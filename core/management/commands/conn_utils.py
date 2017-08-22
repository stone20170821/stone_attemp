#! encoding:utf-8

from django.conf import settings
from sqlalchemy import create_engine
from pandas import DataFrame

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']

database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
    user=user,
    password=password,
    database_name=database_name
)
engine = create_engine(database_url, echo=False)


def write_dataframe_to_sql(df, table_name, if_exists='append'):
    """
    :param if_exists:
    :param df:
    :type df: DataFrame
    :param table_name:
    :return:
    """
    df.to_sql(table_name, engine, if_exists=if_exists)
