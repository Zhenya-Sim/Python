from SubjectTable import SubjectTable

db = SubjectTable('postgresql://postgres:2921@localhost:5432/test')


def test_add_subject():
    result = db.get_subjects()
    len_before = len(result)
    subject_title = 'Sports'
    subject_id = 20
    db.add_subject(subject_title, subject_id)
    result = db.get_subjects()
    len_after = len(result)
    assert len_after - len_before == 1
    db.delete_subject(subject_id)


def test_update_subject():
    subject_title = 'Sports'
    subject_id = 20
    db.add_subject(subject_title, subject_id)
    new_title = 'Gym'
    db.update_subject(new_title, subject_id)
    result = db.get_subject_by_id(subject_id)
    assert result['subject_title'] == new_title
    db.delete_subject(subject_id)


def test_delete_subject():
    subject_title = 'Sports'
    subject_id = 20
    db.add_subject(subject_title, subject_id)
    db.delete_subject(subject_id)
    result = db.get_subject_by_id(subject_id)
    assert result is None
