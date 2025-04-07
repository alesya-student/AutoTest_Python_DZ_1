from Table_BD import Table_DB


db = Table_DB("postgresql://postgres:1211@localhost:5432/postgres")

# Тест. Список предметов.
def test_get_subjects():
    result = db.get_subjects()
    print(f'РЕЗУЛЬТАТ ЗАПРОСА: {result}')
    assert len(result) > 0


# Тест. Добавить новый предмет.
def test_add_new_subject():
    # получить список предметов:
    body = db.get_subjects()
    len_before = len(body)
    # добавить новый предмет:
    id = 17
    title = "Test"
    db.create_new_subject(id, title)
    max_id = db.get_max_id(id)
    body = db.get_subjects()
    len_after = len(body)
    # удалить добавленный предмет:
    db.delete_subject(max_id)
    # проверки:
    print(f'ЧТО ВОЗВРАЩАЕТ MAX_ID {max_id} ')
    assert len_after ==  max_id 
    assert len_after - len_before == 1


# Тест. Редактировать предмет.
def test_edit_subject():
    # добавить новый предмет:
    id = 17
    title = "Test"
    title = db.create_new_subject(id, title)
    max_id = db.get_max_id(id)
    # изменить название предмета:
    new_title = "Test 2.0"
    new_id = max_id
    new_title = db.edit_subject(new_title, new_id)
    # удалить добавленный предмет:
    db.delete_subject(max_id)
    # проверки:
    assert title == new_title
    assert id == new_id


# Тест. Удалить предмет.
def test_delete_subject():
    # добавить новый предмет:
    id = 17
    title = "Test"
    db.create_new_subject(id, title)
    max_id = db.get_max_id(id)
    # удалить созданный предмет:
    db.delete_subject(max_id)
    # вернуть компанию по ID
    rows = db.get_subject_by_id(max_id)
# проверки:
    assert len(rows) == 0
