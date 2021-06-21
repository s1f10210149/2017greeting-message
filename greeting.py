
   
from datetime import datetime
from typing import get_type_hints

def greet(mane):
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    message +=  ', ' + mane + '-san!'
    print(message)

greet('Inoue')
