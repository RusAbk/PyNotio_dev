from Notion.properties import Prop
from Notion.blocks import Block
import json

class Page:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.get_json()
    def __repr__(self):
        return self.get_json()

    def get_json(self):
        return json.dumps(self.data, indent=4)

    
    def set_block_info(self, block_info):
        self.data['block_info'] = block_info
    def set_content(self, content):
        self.data['raw_content'] = content
        self.content = []
        self.data['plaintext'] = []
        for block in content['results']:
            b = Block(block)
            self.content.append(b)
            self.data['plaintext'].append(b.get_plaintext())


    def get_data(self):
        return self.data
    
    def get_title(self):
        return self.data['properties']['title']['plain_text']

    def get_cover(self):
        return self.data['cover']['external']['url']

    def get_created_time(self):
        return self.data['created_time']

    def get_prop(self, prop):
        return Prop(self.data['properties'][prop])

    def get_prop_value(self, prop):
        return Prop(self.data['properties'][prop]).get_value()
        