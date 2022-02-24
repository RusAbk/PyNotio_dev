# from Notion import NotionWrapper, Ftr, FtrGr
import os
from dotenv import load_dotenv
load_dotenv()

from pprint import pprint 
from Notion.wrapper import Notion
from Notion.filters import CompoundFilter, TextFilter


NOTION_API_KEY = os.getenv('NOTION_API_KEY')

n = Notion(NOTION_API_KEY)
pprint(n.get_page('8fe825aab0cf45868d75900042efd3d7').get_data())
# pprint(n.req_get('https://api.notion.com/v1/blocks/' + 'a53eef1606ad4f18bc743c23b2445f0b' + '/children'))


# f = CompoundFilter(TextFilter.contains('Название', '3'), TextFilter.contains('Название', 'V'), 'and')
# pprint(n.db_query('2a55093ae101451f98962060b32dbbbf', f.get()))