import os,sys

inRunner = None
i18n = None
try:
    from mchat import i18n
except ImportError:
    inRunner = True
if inRunner: exec("from py.mchat import i18n")

i18n.set('locale', 'zh_CN')
i18n.set('file_format', 'json')
i18n.set('filename_format', '{locale}.{format}')
i18n.load_path.append(os.path.join(os.path.dirname(__file__), 'text'))
#print(i18n.translations.container)

def t(*args, **kwargs):
    return i18n.t(*args, **kwargs)