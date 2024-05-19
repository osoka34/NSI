# 'postgresql://postgres:postgres@my_postgres_container:5432/postgres'
CONFIG = {
    'db': {
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
        # 'host': 'my_postgres_container',
        'host': '0.0.0.0',
        # 'port': '5432'
        'port': '12000'
    }
}

# TODO это урл для подключения к контейнеру, при запуске в докере
# чтобы запустить на хосте нужно заменить на 'postgresql://postgres:postgres@localhost:12000/postgres'
# engine = create_engine('postgresql://postgres:postgres@localhost:12000/postgres')
