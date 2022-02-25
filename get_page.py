import os
from dotenv import load_dotenv
load_dotenv()
import json

from Notion.wrapper import Notion


NOTION_API_KEY = os.getenv('NOTION_API_KEY')
n = Notion(NOTION_API_KEY)


page = n.get_page('8fe825aab0cf45868d75900042efd3d7')
txt = n.create_rich_text('hello world')
b = n.create_paragraph(txt)
data = {
    'children': [b.get_json()]
}

page.append_block(b)