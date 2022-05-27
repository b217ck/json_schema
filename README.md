# json_schema

Скрипт для автоматизации проверки ответа API от сервера
---
Актуальная версия - js_check.py
---
**Для запуска требуется установка интерпретатора Python**

*Задание на автоматизацию проверки ответа API от сервера.*

*У вас есть следующие требования к ответу:*

- timestamp: int
- referer: string (url)
- location: string (url)
- remoteHost: string
- partyId: string
- sessionId: string
- pageViewId: string
- eventType: string (itemBuyEvent или itemViewEvent)
- item_id: string
- item_price: int
- item_url: string (url)
- basket_price: string
- detectedDuplicate: bool
- detectedCorruption: bool
- firstInSession: bool
- userAgentName: string
Вот здесь можно взять пример json с ответами некоего интернет-магазина, составленный по этим правилам.

*Вам нужно написать простой тест, который проверяет json на правильность полей. То есть проверяет, что каждый объект в json:*

*Содержит все перечисленные в требованиях поля.
Не имеет других полей.*
Все поля имеют именно тот тип, который указан в требованиях:
- int — это значит целое число;
- string — произвольная строка;
- string (url) — это строка с url. В рамках этого задания проверяем, что url начинается c http:\\ или https:\\;
- string (itemBuyEvent или itemViewEvent) — это строка, в которой может быть только эти конкретные два значения и никакие другие;
- bool — булево значение, то есть True или False.
*Тест должен вернуть Pass или список значений, которые тест посчитал ошибочными, и причину, почему они ошибочные.*

