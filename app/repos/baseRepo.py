from sqlalchemy import create_engine


class BaseRepo:
    engine: object

    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:0000@localhost/ContactDB")
