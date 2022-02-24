import stat
from Notion.richtext import RichText
from Notion.wrapper import Notion

class Block:
    def __init__(self, data = None):
        if data is not None:
            self.data = data
            self.type = data["type"]
            self.has_children = data["has_children"]
            self.id = data["id"]

            self.parse_richtext_list()

    def parse_richtext_list(self):
        text_list = self.data[self.type]["text"]
        self.rich_text_objects = []
        for rt_obj in text_list:
            richtextobj = RichText(rt_obj)
            self.rich_text_objects.append(richtextobj)

    def get_plaintext(self):
        result = ""
        for rto in self.rich_text_objects:
            result += rto.get_plaintext()
        return result

    def get_json(self):
        rt_list = []
        for rt in self.rich_text_objects:
            rt_list.append(rt.get_json())
        return {
            "object": "block",
            "type": self.type,
            "archived": False,
            "has_children": False,
            "text": rt_list
        }