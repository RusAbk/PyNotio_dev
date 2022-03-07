import os
from dotenv import load_dotenv
load_dotenv()

from pynotio.wrapper import Notion
from pprint import pprint


NOTION_API_KEY = os.getenv('NOTION_API_KEY')
n = Notion(NOTION_API_KEY)

response = n.db_query('4016cf4e1b7f46789b1617369a5adfa3')
pprint(response)

# for page in response:
#     print(page.get_prop_value('Name'))