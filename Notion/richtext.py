class RichText:
    def __init__(self, data=None):
        if data is not None:
            if isinstance(data, dict):
                self.data = data
                self.is_link = data["href"] is not None
                self.href = data["href"]
                self.is_bold = data["annotations"]["bold"]
                self.is_italic = data["annotations"]["italic"]
                self.is_underlined = data["annotations"]["underline"]
                self.is_strikethrough = data["annotations"]["strikethrough"]
                self.is_code = data["annotations"]["code"]
                self.color = data["annotations"]["color"]
                self.text = data["plain_text"]
            elif isinstance(data, str):
                self.text = str

    def get_plaintext(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_json(self):
        return {
            "type": "text",
            "href": self.href,
            "plain_text": self.text,
            "annotations": {
                "bold": self.is_bold,
                "code": self.is_code,
                "color": self.color,
                "italic": self.is_italic,
                "strikethrough": self.is_strikethrough,
                "underline": self.is_underline,
            },
            "text": {
                "content": self.text,
                "link": self.href if self.href is not None else {"url": self.href}
            }
        }
