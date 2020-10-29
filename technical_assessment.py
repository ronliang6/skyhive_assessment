import math


# Question 1 begins here
def calculate_optimal_schedule(appts: []) -> int:
    """
    Calculate the number of minutes in an optimal schedule, given a list of appointments.

    Precondition/Assumptions:
    The chiropractor must take 15-minute breaks between appointments, and therefore cannot take adjacent requests.
    The first appointment always starts on the minute the chiropractor begins working.
    The last appointment always ends on the minute the chiropractor ends working.

    Algorithm:
    This algorithm solves the problem recursively and employs memoization to optimize speed and memory. This memo
    stores solutions to the sub-problems that occur in this recursive solution, which would otherwise need to be
    recalculated. When this method attempts to solve the sub-problem at index 'index' for the second or later time,
    it will check and note that there is a memo value at this index, and return that value instead of recalculating it.
    To ensure that all permutations of schedules are accounted for, there are two recursive calls in this method. One
    to account for the current index, and skipping the next. And one that only skips the current, in order to access
    the skipped index in the first recursive call.

    :param appts: a list of integers in multiples of 30, representing back to back appointments
    :return: an int, represents the hours in an optimal schedule
    """
    return calculate_optimal_schedule_recursive(appts, 0, [None] * len(appts))


def calculate_optimal_schedule_recursive(appts: [], index: int, memo: []) -> int:
    """
    Calculate the number of minutes in an optimal schedule, given a list of appointments.

    Precondition/Assumptions:
    The chiropractor must take 15-minute breaks between appointments, and therefore cannot take adjacent requests.
    The first appointment always starts on the minute the chiropractor begins working.
    The last appointment always ends on the minute the chiropractor ends working.

    :param appts: a list of integers in multiples of 30, representing back to back appointments
    :param index: an int
    :param memo: a list of values to store calculations of sub-problems
    :return: an int, represents the hours in an optimal schedule considering only appointments at index 'index' and
    beyond
    """
    if index >= len(appts):
        return 0
    # only calculate each sub-problem when considering appointments at index 'index' and beyond once
    if not memo[index]:
        optimal_schedule_with_index = appts[index] + calculate_optimal_schedule_recursive(appts, index + 2, memo)
        # Only one appointment is skipped because chiropractor breaks will always be shorter than the next appointment

        optimal_schedule_without_index = calculate_optimal_schedule_recursive(appts, index + 1, memo)
        memo[index] = max(optimal_schedule_with_index, optimal_schedule_without_index)

    return memo[index]


# Question 2 begins here
def traversing_matrix(x_coord: int, y_coord: int) -> int:
    """
    Returns the permutations of paths from point(0, 0) to point(x_coord, y_coord) on an n by n dot matrix.

    Only the movement directions 'up' and 'right' are valid.
    This problem can be solved recursively. However, the formula below is a simpler method of calculating this
    problem. The number of 'up' and 'right' movements are fixed for any given path for any given destination.
    The only differences between paths are the order of these movements. i.e., UP UP RIGHT, UP RIGHT UP, RIGHT UP UP
    This is a mathematical combinations question and can be calculated by '(x+y)Cx' or '!(x+y)/(!x!y)' where x and y
    are distinct objects, and the order of objects of the same type do not matter.

    :param x_coord: must be inside the matrix
    :param y_coord: must be inside the matrix
    :return: the number of unique paths to reach point(x_coord, y_coord)
    """
    return int(math.factorial(x_coord + y_coord) / math.factorial(x_coord) / math.factorial(y_coord))


def main():
    appt_requests = [60, 30, 60, 120, 30, 150, 90, 60]
    print("Your appointment requests:", *appt_requests, " Optimal hours:", calculate_optimal_schedule(appt_requests))

    destination_coords = (3, 5)
    print("Your destination: ", *destination_coords,
          " Unique paths:", traversing_matrix(destination_coords[0], destination_coords[1]))


if __name__ == "__main__":
    main()
