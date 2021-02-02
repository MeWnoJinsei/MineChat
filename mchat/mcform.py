import json

class FormElement:
    def __repr__(self):
        return json.dumps(self.extract())
    def __str__(self):
        return self.__repr__()
    def extract(self):
        data = self.__dict__
        if hasattr(self, 'type'):
            data["type"] = self.type
        return data

class TextFormElement(FormElement):
    text = None
    def __init__(self, text):
        self.text = text

class Label(TextFormElement):
    type = 'label'
    
class Input(TextFormElement):
    type = 'input'
    placeholder = None
    default = None

    def __init__(self, text, placeholder, default):
        super(__class__, self).__init__(text)
        self.placeholder, self.default = placeholder, default


class Selection(TextFormElement):
    pass


class Toggle(TextFormElement):
    type = 'toggle'
    default = False
    def __init__(self, text, default):
        super(__class__, self).__init__(text)
        self.default = default

class SliderCommon(TextFormElement):
    type = None
    default = None
    def __init__(self, text, default):
        super(__class__, self).__init__(text)
        self.default = default
        

class Slider(SliderCommon):
    type = 'slider'
    step = None
    min, max = None, None
    def __init__(self, text, min, max, step, default):
        super(__class__, self).__init__(text, default)
        self.min, self.max = min, max
        self.step = step

class SliderStep(SliderCommon):
    type = 'step_slider'
    steps = []
    def __init__(self, text, steps, default):
        super(__class__, self).__init__(text, default)
        self.steps = steps

class Dropdown(TextFormElement):
    type = 'dropdown'
    options = []
    def __init__(self, text, defaultIndex, options):
        super(__class__, self).__init__(text)
        self.default = defaultIndex
        self.options = options

class FormCommon:
    type = None
    title = None
    content = None
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        return json.dumps(self.extract())
    def extract(self):
        data = self.__dict__
        if hasattr(self, 'type'):
            data["type"] = self.type
        return data



class FormModal(FormCommon):
    type = 'modal'
    button1 = None
    button2 = None

    def __init__(self, title, description, positive, negative):
        self.button1, self.button2 = positive, negative
        self.title, self.content = title, description


class Form(FormCommon):
    type = 'form'
    buttons = []

    def __init__(self, title, description, *selections):
        self.buttons = selections
        self.title, self.content = title, description


class FormCustom(FormCommon):
    type = 'custom_form'
    content = []

    def __init__(self, title, *content):
        self.title = title
        self.content = content
    def __repr__(self):
        data = self.__dict__
        if hasattr(self, 'type'):
            data["type"] = self.type
        data["content"] = [i.extract() for i in self.content]
        return json.dumps(data)