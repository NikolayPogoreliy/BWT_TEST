from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def connect_db():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_db_table(engine):
    Base.metadata.create_all(engine)


def get_or_create(session, table, filter_query, do_commit=True):
    instance = session.query(table).filter_by(**filter_query).first()
    if not instance:
        instance = table(**filter_query)

        if do_commit:
            try:
                session.add(instance)
                session.commit()
            except:
                session.rollback()
    return instance


def update_or_create(session, table, filter_query, attrs, do_commit=True):
    instance = session.query(table).filter_by(**filter_query).first()
    if not instance:
        instance = table()
    attrs.update(filter_query)
    for key, value in attrs.items():
        instance.__setattr__(key, value)
    if do_commit:
        try:
            if not instance.id:
                session.add(instance)
            session.commit()
        except:
            session.rollback()
    return instance

