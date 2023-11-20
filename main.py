import pandas as pd
import numpy as np

# IMPORTANT: please do not modify this import statement



# The data frame `df` includes the following information
#
# |            | AUD/USD | EUR/AUD |
# |------------+---------+---------|
# | 2020-09-08 | 0.7280  | 1.6232  |
# | 2020-09-09 | 0.7209  | 1.6321  |
# | 2020-09-10 | NaN     | 1.6221  |
# | 2020-09-11 | 0.7263  | 1.6282  |
# | 2020-09-14 | 0.7281  | NaN     |
# | 2020-09-15 | 0.7285  | 1.6288  |
#data = {
#    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
#    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
#    }
#index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
#df = pd.DataFrame(data, index)


#new_df = df.copy()
#new_df.loc['1', :] = 1
#a=df.loc['a':'z']
#print(a)

# You should not import any other module
import datetime as dt





import datetime as dt


def time_it(func, parms):
    """Function to measure time taken to execute the given
    function with specified parameters.

    Parameters:
        func : any function
            Function to measure its execution time
        parms : dict
            A dictionary that must be passed to given
            function to measure its execution time.

    Returns:
        A string denoting time taken for execution of
        the given function with specified parameters.
    """

    # Record the time before executing the function
    start = dt.datetime.now()

    # Execute the given function with specified parameters
    func(**parms)

    # Record the time after executing the function
    end = dt.datetime.now()

    # Measure time elapsed in executing the function
    time_taken = end - start

    # Get number of days from time_taken (a timedelta object)
    days = time_taken.days

    # Get hours from total seconds
    hours, remain = divmod(time_taken.seconds, 3600)

    # Get minutes from remaining seconds
    minutes, seconds = divmod(remain, 60)

    # Add microseconds to the second
    seconds += time_taken.microseconds / 1e6

    # Create a string to return using _mk_msg() function
    msg = _mk_msg(days=days, hours=hours, mins=minutes, secs=round(seconds, 1))

    # Return the string createrd
    return msg


def _mk_msg(days, hours, mins, secs):
    """Function that returns a string in specified format
    containing given days, hours, mins, and secs.
    """
    msg = f"It took {days:.0f} days, {hours:.0f} hours, {mins:.0f} mins, and {secs} secs to execute the function"
    return msg


def _test_time_it():
    """Function that uses time.sleep() function to test time_it() function."""

    import time

    print("Note: It will take about 1 mins to execute this test function...")

    def _my_func(secs):
        # Sleep for specified seconds
        time.sleep(secs)

    # Call time_it() to test if it is working as expected
    res = time_it(_my_func, {"secs": 64})

    # Print out the string returned by the time_it() function
    print(res)


# Driver of the program
if __name__ == "__main__":
    # Call _test_time_it() function to test
    # the user-defined time_it() function
    _test_time_it()
