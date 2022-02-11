class Logger:
    def __init__(self, file_obj):
        self.file_obj = file_obj
    def log(self, text, end="\n"):
        if type(text) != str:
            text = str(text)
        self.file_obj.write(text + end)
