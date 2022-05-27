#подключение модулей
import json
from jsonschema import validate

#открытие json-файла
with open('json_example_QAP.json') as file:
    template = json.load(file)

print('Содержимое json-файла:', template)
#print(type(template))

#преобразование списка в словарь
js_dict = {k: v for e in template for (k, v) in e.items()}
#print(js_dict)
#print(type(js_dict))

#with open('json_out.json', 'w') as write_file:
    #json.dump(template, write_file, indent=4)

#with open('json_out.json') as read_file:
    #print(read_file.read())

#json-схема для валидации словаря
schema = {
    "type": "object",
    "properties": {
        "timestamp": {
            "type": "integer"
            },
        "referer": {
            "type": "string",
            },
        "location": {
            "type": "string"
            },
        "remoteHost": {
            "type": "string"
            },
        "partyId": {
            "type": "string"
            },
        "sessionId": {
            "type": "string"
            },
        "pageViewId": {
            "type": "string"
            },
        "eventType": {
            "type": "string",
            "enum": ["itemBuyEvent", "itemViewEvent"]
            },
        "item_id": {
            "type": "string"
            },
        "item_price": {
            "type": "integer"
            },
        "item_url": {
            "type": "string"
            },
        "basket_price": {
            "type": "string"
            },
        "detectedDuplicate": {
            "type": "boolean"
            },
        "detectedCorruption": {
            "type": "boolean"
            },
        "firstInSession": {
            "type": "boolean"
            },
        "userAgentName": {
            "type": "string"
            },
        },
    "required": ["timestamp", "referer", "location", "remoteHost", "partyId", "sessionId", "pageViewId", "eventType", "item_id","item_price", "item_url", "basket_price", "detectedDuplicate", "detectedCorruption", "firstInSession", "userAgentName"]
    }

#правильный словарь, проходящий условия схемы
message_right = {
        "timestamp": 1555296301000,
        "referer": "https://b24-d2wt09.bitrix24.shop/katalog/item/dress-spring-ease/",
        "location": "https://b24-d2wt09.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:PvFIq25Zl1esub4LGUQ75xAuoYH0XAlj",
        "eventType": "itemViewEvent",
        "item_id": "bx_40480796_7_52eccb44ded0bb34f72b273e9a62ef02",
        "item_price": 2331,
        "item_url": "https://b24-d2wt09.bitrix24.shop/katalog/item/t-shirt-mens-purity/",
        "basket_price": "",
        "detectedDuplicate": False,
        "detectedCorruption": False,
        "firstInSession": True,
        "userAgentName": "TEST_UserAgentName"
}

#неправильный словарь, не проходящий условия схемы
message_wrong = {
        "timestamp": 1555296301000,
        "referer": "https://b24-d2wt09.bitrix24.shop/katalog/item/dress-spring-ease/",
        "location": "https://b24-d2wt09.bitrix24.shop/",
        "remoteHost": "test0",
        "partyId": "0:aFpLgMBB:BcYmReGvvFOxrDyWtwCqiHHYMmKlLWiH",
        "sessionId": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
        "pageViewId": "0:PvFIq25Zl1esub4LGUQ75xAuoYH0XAlj",
        "eventType": "itemViewEent",
        "item_id": "bx_40480796_7_52eccb44ded0bb34f72b273e9a62ef02",
        "item_price": 2331,
        "item_url": "https://b24-d2wt09.bitrix24.shop/katalog/item/t-shirt-mens-purity/",
        "basket_price": "",
        "detectedDuplicate": 123,
        "detectedCorruption": False,
        "firstInSession": "False",
        "userAgentName": "TEST_UserAgentName"
}

#проверка верного словаря
if validate(message_right, schema)==None:
    print('Pass')
else:
    print(validate(message_right, schema))

#проверка верного словаря
if validate(js_dict, schema)==None:
    print('Pass')
else:
    print(validate(message_right, schema))

#проверка неверного словаря, раскоментить для проверки
#if validate(message_wrong, schema)==None:
#    print('Pass')
#else:
#    print(validate(message_wrong, schema))