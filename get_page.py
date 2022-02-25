import os
from dotenv import load_dotenv
load_dotenv()

from Notion.wrapper import Notion
from pprint import pprint


NOTION_API_KEY = os.getenv('NOTION_API_KEY')
n = Notion(NOTION_API_KEY)

# Use lazy mode. Page will be prepared to append new blocks but you'll save time on data request
page = n.get_page('8fe825aab0cf45868d75900042efd3d7', lazy = True)
page.append_block(
    n.create_paragraph([
        n.create_rich_text('Hey, everyone! I am using '), 
        n.create_rich_text('the lazy mode ').toggle_bold(),
        n.create_rich_text('to add new block on the page.')
    ])
)

# or normal mode to get all page data
page = n.get_page('8fe825aab0cf45868d75900042efd3d7')
pprint(page.get_data())