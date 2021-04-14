from datetime import *
from csv_reader import CSVReader
from meetings import Meetings


def convert_data(rows):
    def convert(t):
        return datetime.strptime(t, '%I:%M%p').strftime('%H:%M')

    start_of_day = '09:00'
    end_of_day = '17:00'
    array = []
    for row in rows:
        current_row = []
        for column in row:
            if column != '':
                column = convert(column)
            current_row.append(column)
        if '' in current_row:
            if current_row[0] == '':
                end_of_day = current_row[1]
            else:
                start_of_day = current_row[0]
        else:
            array.append(current_row)
    return start_of_day, end_of_day, array


data = CSVReader('times')
start, end, data = convert_data(data)
meetings = Meetings(start, end, data)
print(meetings)
conflicts, out_of_hours = meetings.report_anomalies()
print('conflicting:', conflicts)
print('out of hours:', out_of_hours)
