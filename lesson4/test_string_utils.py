import pytest
from stringUtils import StringUtils


# 1
# @pytest.mark.test_positive
@pytest.mark.parametrize('input_text, output_text', [
    ('привет', 'Привет'),
    ('Hello!', 'Hello!'),
    ("п ", "П "),
    ('ПРИВЕТ', 'Привет'),
    ("пРИВЕТ", "Привет")
    ]
)
def test_positive_capitilize(input_text, output_text):
    stringUtils = StringUtils()
    assert stringUtils.capitilize(input_text) == output_text


# @pytest.mark.xfail
@pytest.mark.parametrize('input_text, output_text', [
    ('123', '123'),
    ("  ", "  ")
    ]
)
def test_nigative_capitilize(input_text, output_text):
    stringUtils = StringUtils()
    assert stringUtils.capitilize(input_text) == output_text


# 2
@pytest.mark.parametrize('input_text, output_text', [
    (' Игра', 'Игра'),
    (' Apple ', 'Apple '),
    ('123', '123')
    ]
)
def test_positive_trim(input_text, output_text):
    stringUtils = StringUtils()
    assert stringUtils.trim(input_text) == output_text


# @pytest.mark.xfail
@pytest.mark.parametrize('input_text, output_text', [
    (' ', '')
    ]
)
def test_nigative_trim(input_text, output_text):
    stringUtils = StringUtils()
    assert stringUtils.trim(input_text) == output_text


# 3
@pytest.mark.parametrize('input_list, output_list', [
    ("a,b,c,d", ["a", "b", "c", "d"]),
    ("1,2,3,4", ["1", "2", "3", "4"]),
    ]
)
def test_positive_to_list(input_list, output_list):
    stringUtils = StringUtils()
    assert stringUtils.to_list(input_list) == output_list


# НЕ ПОНИМАЮ КАК СОСТАВИТЬ НЕГАТИВНЫЙ ТЕСТ!!!
# @pytest.mark.xfail(reason="заведомая ошибка")
# @pytest.mark.parametrize('input_list, output_list' [
#     ("1:2:3", ["1", "2", "3"])
#     ]
# )
# def test_nigative__to_list(input_list, output_list):
#     stringUtils = StringUtils()
#     assert stringUtils.to_list(input_list) == output_list


# 4
@pytest.mark.parametrize('string, symbol, result', [
        ('SkyPro', 'S', True),
        ('Мышь', 'A', False)
        ]
)
def test_positive_containse(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == result


# @pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
        (' ', ' ', True)
        ]
)
def test_nigative_contains(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    assert res == result


# 5
@pytest.mark.parametrize('string, symbol, result', [
    ('Паравоз', 'Пара', 'воз'),
    ('12345', '34', '125'),
    ('Hello!', '!', 'Hello'),
    ('12345', '2345', '1')
    ]
)
def test_positive_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result


# @pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    (' ', ' ', ''),
    ('12 ', ' ', '12')
    ]
)
def test_nigative_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result


# 6
@pytest.mark.parametrize('string, symbol, result', [
    ('SkyPro', 'S', True),
    ('Мышь', 'П', False),
    ('Мышь', 'ш', False),
    ('12345', '1', True)
    ]
)
def test_positive_starts_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result


# @pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    (' ', '', False),
    ('v', '', False),
    (' ', ' ', True)
    ]
)
def test_nigative_starts_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result


# 7
@pytest.mark.parametrize('string, symbol, result', [
    ('SkyPro', 'o', True),
    ('Мышь', 'шь', True),
    ('Мышь', 'ш', False),
    ('12345', '5', True)
    ]
)
def test_positive_end_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result


# @pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
    ('v', '', False),
    (' ', '', False),
    (' ', ' ', True)
    ]
)
def test_nigative_end_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result


# 8
@pytest.mark.parametrize('string, result', [
    ('SkyPro', False),
    ('', True),
    (' ', True),
    ('12345', False)
    ]
)
def test_positive_is_emptyh(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result


# @pytest.mark.xfail
@pytest.mark.parametrize('string, result', [
    (' ', False)
    ]
)
def test_nigative_is_emptyh(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result


# 9
# Не поняла как можно протестировать разные разделители.
@pytest.mark.parametrize('input_list, output_list', [
    (["a", "b", "c", "d"], "a, b, c, d"),
    ([1, 2, 3, 4], "1, 2, 3, 4"),
    (["Юго" + "-" + "западный"], "Юго-западный")
    ]
)
def test_positive_list_to_string(input_list, output_list):
    stringUtils = StringUtils()
    assert stringUtils.list_to_string(input_list) == output_list


# @pytest.mark.xfail
@pytest.mark.parametrize('input_list, output_list', [
    (["", "", "", ""], ", , , "),
    ([" ", " ", " ", " "], " ,  ,  ,  "),
     ]
)
def test_nigative_list_to_string(input_list, output_list):
    stringUtils = StringUtils()
    assert stringUtils.list_to_string(input_list) == output_list
