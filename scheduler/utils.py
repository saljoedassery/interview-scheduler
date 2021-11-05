from datetime import timedelta


def time_format(timeslots):
    """
    Formatting the datetime to %Y-%m-%d %H:%M:%S format
    @param timeslots:
    @return:
    """
    result = []
    for start_time, end_time in timeslots:
        result.append((start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')))
    return result


def find_common_timeslots(timeslots):
    """
    function to find the common time slots between interviewer and candidate
    @param timeslots: list of timeslots with user, start_time, end_time
    @return: List common available timeslots of interviewer and candidate
    """
    result = []
    candidate_timeslots, interviewer_timeslots = group_timeslots_by_user(timeslots)
    candidate_timeslots_intervals = split_timeslots_into_1_hr_periods(candidate_timeslots)
    interviewer_timeslots_intervals = split_timeslots_into_1_hr_periods(interviewer_timeslots)

    result_set = candidate_timeslots_intervals.intersection(interviewer_timeslots_intervals)

    for start_time, end_time in result_set:
        result.append((start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')))
    return result


def group_timeslots_by_user(timeslots):
    """
    Group the timeslots based on the user (interviewer/candidate)
    @param timeslots:
    @return: two list of tuple. One list for candidate and another for interviewer
    """
    candidate_timeslots = []
    interviewer_timeslots = []
    for timeslot in timeslots:
        if timeslot.user.role == "candidate":
            candidate_timeslots.append((timeslot.start_time, timeslot.end_time))
        elif timeslot.user.role == "interviewer":
            interviewer_timeslots.append((timeslot.start_time, timeslot.end_time))
    return candidate_timeslots, interviewer_timeslots


def split_timeslots_into_1_hr_periods(timeslots):
    """
    Splits the timeslots in the any range to 1 hour range
    @param timeslots: list of tuples [(start_time, end_time)]
    @return: set of tuples of intervals [(start_time, end_time), (), ...]
    """

    result = set()
    for start_time, end_time in timeslots:
        temp = start_time

        while temp < end_time:
            result.add((temp, temp + timedelta(hours=1)))
            temp = temp + timedelta(hours=1)

    return result

