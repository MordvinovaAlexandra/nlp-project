import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    # def __init__(self):
    #     super().__init__()
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

        

data = {'id': id(1000), 'username': 'helloword', 'date': datetime.today(), 120: None, 'is_guest': False}

with open('data.json', 'w') as f:
    json.dump(data, f, cls=CustomEncoder)

with open('data_2.json', 'w') as f:  
    # print(json.dumps(data))
    f.write(json.dumps(data, cls=CustomEncoder))

with open('data.json') as f:
    data = json.load(f)
    print(data)

with open('data.json') as f:
    data = json.loads(f.read())
    print(data)