from meetings import Meetings


def test_original():
    data = [
        ('08:15', '08:30'),
        ('09:00', '10:00'),
        ('09:30', '10:30'),
        ('10:45', '13:00'),
        ('12:00', '13:00'),
        ('13:30', '15:00'),
        ('15:00', '15:30'),
        ('16:00', '17:00'),
        ('18:00', '19:00'),
        ('20:00', '21:00'),
    ]
    result = [(1, 2), (3, 4)]
    meetings = Meetings('09:00', '17:00', data)
    conflicts, _ = meetings.report_anomalies()
    assert conflicts == result


def test_no_conflicts():
    data = [
        ('08:15', '08:30'),
        ('09:00', '10:00'),
        ('10:30', '10:45'),
        ('10:45', '13:00'),
        ('13:00', '13:15'),
        ('13:30', '15:00'),
        ('15:00', '15:30'),
        ('16:00', '17:00'),
        ('18:00', '19:00'),
        ('20:00', '21:00'),
    ]
    result = []
    meetings = Meetings('09:00', '17:00', data)
    conflicts, _ = meetings.report_anomalies()
    assert conflicts == result


def test_large_overlap():
    data = [
        ('08:15', '08:30'),
        ('09:00', '10:00'),
        ('10:30', '17:00'),
        ('10:45', '13:00'),
        ('13:00', '13:15'),
        ('13:30', '15:00'),
        ('15:00', '15:30'),
        ('16:00', '17:00'),
        ('18:00', '19:00'),
        ('20:00', '21:00'),
    ]
    result = [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]
    meetings = Meetings('09:00', '17:00', data)
    conflicts, _ = meetings.report_anomalies()
    assert conflicts == result


def test_complete_overlap():
    data = [
        ('09:00', '17:00'),
        ('09:00', '10:00'),
        ('10:30', '10:45'),
        ('10:45', '13:00'),
        ('13:00', '13:15'),
        ('13:30', '15:00'),
        ('15:00', '15:30'),
        ('16:00', '17:00'),
        ('18:00', '19:00'),
        ('20:00', '21:00'),
    ]
    result = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
    meetings = Meetings('09:00', '17:00', data)
    conflicts, _ = meetings.report_anomalies()
    assert conflicts == result


def test_large_triple_overlap():
    data = [
        ('08:15', '08:30'),
        ('09:00', '10:00'),
        ('10:30', '17:00'),
        ('10:45', '13:00'),
        ('13:00', '13:31'),
        ('13:30', '15:00'),
        ('15:00', '15:30'),
        ('16:00', '18:05'),
        ('18:00', '19:00'),
        ('20:00', '21:00'),
    ]
    result = [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (4, 5)]
    meetings = Meetings('09:00', '17:00', data)
    conflicts, _ = meetings.report_anomalies()
    assert conflicts == result


def test_complete_double_overlap():
    data = [
        ('09:00', '17:00'),
        ('09:00', '10:00'),
        ('10:30', '10:45'),
        ('10:45', '13:00'),
        ('13:00', '13:45'),
        ('13:30', '15:00'),
        ('15:00', '15:30'),
        ('16:00', '17:00'),
        ('18:00', '19:00'),
        ('20:00', '21:00'),
    ]
    result = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (4, 5)]
    meetings = Meetings('09:00', '17:00', data)
    conflicts, _ = meetings.report_anomalies()
    assert conflicts == result
