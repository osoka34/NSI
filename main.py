from parser.parser import InfoParser
from parser.s_constant import EOP_FIELDS, RE_PATTERN_EOP, D_TYPE_EOP
from repository.model import NSIData


from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import registry
from sqlalchemy.orm import mapper, sessionmaker, Session
import psycopg2

# Ваша база данных
engine = create_engine('postgresql://postgres:postgres@localhost:12000/postgres')
session = Session(engine)
# connection = engine.connect()
# print("Подключение к базе данных успешно.")
# connection.close()


#
parser = InfoParser("./parser/EOP_14_C04_IAU2000A_one_file_1962-now.txt", EOP_FIELDS, RE_PATTERN_EOP, D_TYPE_EOP)
data = parser.parse()
#
instance = NSIData(**data[0])

session.add(instance)
session.commit()
