

class Meetings:

    """
        Expect a list of pairs, (meeting start time, meeting end time) in 24h times
    """

    def __init__(self, start, end, meetings):
        self._meetings = meetings
        self._start = start
        self._end = end
        meetings.sort(key=lambda x: x[0])

    def __str__(self):
        return '\n'.join([', '.join(x) for x in [y for y in self._meetings]])

    def report_anomalies(self):
        """
            We sorted the list of meeting by starting time so that if the end time of a meeting
            is before the beginning of the following one, we can stop looking at that meeting
            and move on to the next.
        """
        conflicts = []
        out_of_hours = []
        for i in range(len(self._meetings)):
            current_start, current_end = self._meetings[i]
            if current_start < self._start or current_end > self._end:
                out_of_hours.append(i)
            else:
                for j in range(i+1, len(self._meetings)):
                    next_start, next_end = self._meetings[j]
                    if next_start < current_end:
                        conflicts.append((i, j))
                    else:
                        break
        return conflicts, out_of_hours
