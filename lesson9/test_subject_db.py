from SubjectTable import SubjectTable

db = SubjectTable('postgresql://postgres:2921@localhost:5432/test')


def test_add_subject():
    # 1.запросить список, взять длину
    result = db.get_subjects()
    len_before = len(result)
    # 2.добавить новый предмет
    subject_title = 'Sports'
    subject_id = 20
    db.add_subject(subject_title, subject_id)
    # 3.запросить список, взять длину
    result = db.get_subjects()
    len_after = len(result)
    # 4.сравнить длину
    assert len_after - len_before == 1
    # 5.удалить предмет
    db.delete_subject(subject_id)


def test_update_subject():
    # 1.добавить новый предмет
    subject_title = 'Sports'
    subject_id = 20
    db.add_subject(subject_title, subject_id)
    # 2.изменить название предмета
    new_title = 'Gym'
    db.update_subject(new_title, subject_id)
    # 3.сравнить что айдишник тот же, описание равно новому
    result = db.get_subject_by_id(subject_id)
    assert result['subject_title'] == new_title
    # 4.удалить предмет
    db.delete_subject(subject_id)


def test_delete_subject():
    # 1.добавить предмет
    subject_title = 'Sports'
    subject_id = 20
    db.add_subject(subject_title, subject_id)
    # 2.удалить предмет
    db.delete_subject(subject_id)
    # 3.запросить список по idшнику (через длину)
    result = db.get_subject_by_id(subject_id)
    # 4.сравнить, что длина равна 0
    assert result is None
