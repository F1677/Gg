import os
import importlib
import subprocess
import webbrowser

libraries_to_install = [
    'requests', 'mechanize', 'sys', 'names', 'render', 'user_agent', 'telethon', 
    'pyfiglet', 'python-cfonts', 'colorama', 'random', 'types', 'rich', 'uuid', 
    'time', 'string', 'secrets', 'bs4', 'json', 'uuid4', 'generate_user_agent', 
    'threading', 'token_hex', 're', 'telebot', 'socket', 'urllib3', 'termcolor'
]

for library in libraries_to_install:
    try:
        importlib.import_module(library)
        print(f'{library} مثبتة بالفعل')
    except ImportError:
        print(f'تثبيت {library}')
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", library])

print('انتهى تثبيت المكتبات')
webbrowser.open('https://t.me/N_9_N_6')