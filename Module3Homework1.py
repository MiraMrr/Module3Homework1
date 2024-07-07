calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]


print(string_info('Urban University'))
print(string_info('London is the capital of Great Britain'))
print(string_info('Hello world'))
print(is_contains('Three', ['ONE', 'two', 'tHrEe', 'fOuR']))
print(is_contains('Pink', ['red', 'gReEn', 'BLUE']))
print(calls)
