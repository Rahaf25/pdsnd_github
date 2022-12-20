import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhat city would you like? New York City, Chicago or Washington?\n")
      if city.lower() in ('New York City', 'Chicago', 'Washington'):
         
        break
      else:
        print("Sorry, your input should be: chicago new york city or washington")
        continue

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nWhat month would you like? January, February, March, April, May, June or type 'all' \n")
      if month  in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        break
      else:
        print("Sorry, your input should be: january, february, march, april, may, june or all")
        continue
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nWhat day would you like? enter the day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'\n")
      if day  in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        break
      else:
        print("Sorry, your input should be: sunday, ... friday, saturday or all")
        continue
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_common_month = df['month'].mode()[0]
    print('Most Common Month:', popular_common_month)


    # TO DO: display the most common day of week

    popular_day_of_week  = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day_of_week )



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_common_start_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('Gender Types are:', gender_types)
    except KeyError:
      print("Gender Types are:Don't have data by this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('the earliest Year:', Earliest_Year)
    except KeyError:
      print("the earliest Year:\nDon't have data by this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('Most Recent Year:', Most_Recent_Year)
    except KeyError:
      print("Most Recent Year:\nDon't have data by this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('The most Common Year:', Most_Common_Year)
    except KeyError:
      print("The most Common Year:\nDon't have data by this month.")


    print("This will take %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1    # use index values for rows

    print('  If you want to see a few raw data from database ?')
    while True:
        raw_data = input('   (yes or no):  ')
        if raw_data.lower() == 'yes':
            print('   Display rows {} to {}:'.format(rows_start + 1, rows_end + 1))

            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows

           
            print('  if you want to see  next {} rows?'.format(show_rows))
            continue
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	    main()