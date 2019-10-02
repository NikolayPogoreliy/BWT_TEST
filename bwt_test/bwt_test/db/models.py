from sqlalchemy import Column, Integer, Text, String, ForeignKey, UniqueConstraint

from bwt_test.db.utils import Base


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, autoincrement=True, primary_key=True)
    location = Column(String(150))

    def __repr__(self):
        return f'Location: {self.location}'


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, autoincrement=True, primary_key=True)
    category = Column(String(50))

    def __repr__(self):
        return f'Category: {self.category}'


class Organization(Base):
    __tablename__ = 'organization'

    id = Column(Integer, autoincrement=True, primary_key=True)
    category = Column(ForeignKey('category.id'))
    location = Column(ForeignKey('location.id'))
    title = Column(String(255))
    address = Column(String(255))
    phone = Column(String(20), nullable=True)
    link = Column(String(200), nullable=True)
    working_hours = Column(Text, nullable=True)
    about = Column(Text, nullable=True)
    reviews = Column(Integer, nullable=True)
    photo_url = Column(String(255), nullable=True)

    __table_args__ = (UniqueConstraint('title', 'address', name='_title_address_uc'), )

    def __repr__(self):
        return f'{self.title}: {self.location}: {self.category}'
