from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from repository.model import NSIData, RequestLogs


class Repository:
    def __init__(self):
        # TODO это урл для подключения к контейнеру, при запуске в докере
        # чтобы запустить на хосте нужно заменить на 'postgresql://postgres:postgres@localhost:12000/postgres'
        engine = create_engine('postgresql://postgres:postgres@my_postgres_container:5432/postgres')
        self.session = Session(engine)

    def __del__(self):
        self.close()

    def close(self):
        if self.session:
            self.session.close()
            self.session = None

    def add_nsi_data_list(self, data: list[dict]):
        try:
            instances = [NSIData(**d) for d in data]
            self.session.add_all(instances)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def add_nsi_data_one(self, data: dict):
        try:
            instance = NSIData(**data)
            self.session.add(instance)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def add_request_logs(self, data: RequestLogs):
        try:
            self.session.add(data)
            self.session.commit()
        except Exception as e:
            print(f"Error occurred while adding data to the database: {e}")

    def get_nsi_data(self):
        try:
            return self.session.query(NSIData).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return []

    def get_nsi_data_view(self, d_type: int):
        # TODO убрать лимит после тестов
        try:
            return self.session.query(NSIData).filter(NSIData.d_type == d_type).limit(10).all()
        except Exception as e:
            print(f"Error occurred while getting data from the database: {e}")
            return []

