import json


class YourClass:

    def __init__(self, *args):
        pass


def object_to_json(obj):
    return json.dumps(obj.__dict__)


def json_to_object(js):
    js_obj = json.loads(js)
    obj = YourClass(js_obj)

