import requests
from Notion.page import Page

class Notion():
    key = None
    api_version = '2021-08-16'

    def __init__(self, key):
        Notion.key = key
        Notion.auth_h = Notion.key;

    def get_basic_headers(self):
        return {
            'Notion-Version': Notion.api_version,
            'Authorization': 'Bearer ' + Notion.key
        }

    def req_get(self, url, params = {}, headers = {}):
        headers.update(self.get_basic_headers())
        response = requests.get(url, json = params, headers = headers)
        return response.json()

    def req_post(self, url, params = {}, headers = {}):
        headers.update(self.get_basic_headers())
        response = requests.post(url, json = params, headers = headers)
        return response.json()

    def req_put(self, url, params = {}, headers = {}):
        headers.update(self.get_basic_headers())
        response = requests.put(url, json = params, headers = headers)
        return response.json()

    def req_delete(self, url, params = {}, headers = {}):
        headers.update(self.get_basic_headers())
        response = requests.delete(url, json = params, headers = headers)
        return response.json()

    def req_patch(self, url, params = {}, headers = {}):
        headers.update(self.get_basic_headers())
        response = requests.patch(url, json = params, headers = headers)
        return response.json()



    def get_page(self, page_id):
        page = Page(self.req_get('https://api.notion.com/v1/pages/' + page_id))
        page.set_block_info(self.req_get('https://api.notion.com/v1/blocks/' + page_id))
        page.data['has_content'] = page.data['block_info']['has_children']
        if page.data['has_content']:
            page.set_content(self.req_get('https://api.notion.com/v1/blocks/' + page_id + '/children'))
        return page

    def append_block_to(self, block, parent_id):
        pass


    
    def db_query(self, db_id, filter = {}, sorts = []):
        data = {}
        if len(filter) != 0:
            data['filter'] = filter
        if len(sorts) != 0:
            data['sorts']
        return self.req_post('https://api.notion.com/v1/databases/' + db_id + '/query', data)