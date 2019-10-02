from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker

from bwt_test.db.models import Category, Location, Organization
from bwt_test.db.utils import get_or_create, connect_db, create_db_table, update_or_create


class BwtTestItemToDbPipeline:
    def __init__(self):
        engine = connect_db()
        create_db_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if not item.get('title') or not item.get('address'):
            raise DropItem()
        session = self.Session()
        location = get_or_create(session, Location, {'location': spider.location})
        category = get_or_create(session, Category, {'category': spider.category})
        filter_query = {'title': item.pop('title'), 'address': item.pop('address')}
        attrs = {'location': location.id, 'category': category.id}
        attrs.update(item)
        update_or_create(session, Organization, filter_query, attrs)
        return item
