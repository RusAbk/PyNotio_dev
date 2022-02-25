import os
from dotenv import load_dotenv
load_dotenv()
import json

from Notion.wrapper import Notion
from pprint import pprint


NOTION_API_KEY = os.getenv('NOTION_API_KEY')
n = Notion(NOTION_API_KEY)

# get page by id
page = n.get_page('8fe825aab0cf45868d75900042efd3d7')

# create rich_text element
text_elem = n.create_rich_text('hello')
# make text bold
text_elem.toggle_bold()


# create paragraph-block
b = n.create_paragraph(text_elem)
# send query to append paragraph-block to page
print(json.dumps(b.get_json(), indent = 2))


# be more smart & flexible
b = n.create_paragraph([
    n.create_rich_text('I am ').toggle_bold(), 
    n.create_rich_text('more ').toggle_italic(), 
    n.create_rich_text('smart ').toggle_striketrough(),
    n.create_rich_text('flexible way').toggle_underlined()
])
# send query to append paragraph-block to page
page.append_block(b)


# create links
lnk = n.create_rich_text('Go to Github repo').set_link('https://github.com/Ruslanabk/pyNotion')
b = n.create_paragraph(lnk)
# send query to append paragraph-block to page
page.append_block(b)