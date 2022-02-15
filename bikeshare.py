import time
import pandas as pd
import numpy as np
import calendar  #to help me write the time_stats():
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input("Please choose the city that you want data for from chicago , new york city , washington: ").lower()
        if city not in CITY_DATA:
            print("Your choice is incorrect , please choose again")
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('Please choose the month that you want or type "all" to display all months ').lower()
        months=['january','february','march','april','may','june']
        if month != "all" and month not in months:
         print('Please try entering a valid month name ')
        else:
            break
        

         
 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('Please choose the day of week that you want or type "all" to display all the days ').lower()
        days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        if day != "all" and day not in days:
         print('Please try entering a valid day name ')
        else:
           break

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
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() 
    
    if month != 'all':
        months= ['january','february','march','april','may','june']
        month= months.index(month) + 1
        
        df= df[df['month'] == month]
        
    if day != 'all':
        df=df[df['day_of_week'] == day.title()] # i used .title() to capitalize the week days to adapt with the data set
            
    return df

def raw_data(df):
    i=0
    input_by_me= input("would you like me to show you the first 5 rows of data ? , choose yes/no :  ").lower()
    pd.set_option('display.max_columns',None)
    
    while True:
        if input_by_me == "no":
            break
        else:
            print(df[i:i+5])
            input_by_me = input( "would you like to see more  5 rows of this data ? , choose yes/no: ").lower()
            i+=5
            
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    most_common_month = df['month'].mode()[0]
    print('most common month is :', calendar.month_name[most_common_month])
    
    most_common_day = df['day_of_week'].mode()[0]
    print(' most common day:',most_common_day)
    
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('most common start hour is :', most_common_start_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    commonly_used_start_station=df['Start Station'].mode()[0]
    print('most common station used as a start is :', commonly_used_start_station)
    
    commonly_used_end_station=df['End Station'].mode()[0]
    print('most common station used as an end is:', commonly_used_end_station)
    
    common_start_end_stations = (df['Start Station'] + ' , ' + df['End Station']) .mode()[0]
    print('most frequent combination of start and end stations :', common_start_end_stations)
    
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time=df['Trip Duration'].sum()
    print("total travel time",total_travel_time, 'seconds, or ' , total_travel_time/3600,'hours')
    
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is: ' , mean_travel_time, 'seconds, or ' ,mean_travel_time/3600 , 'hours')
    
    
    

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('counts of user types:\n',df['User Type'].value_counts())
    
    if "gender" in df:
        print('\n counts of gender:\n', df['gender'].value_counts())
        
        
    if "birth year" in df:
        earliest_year_of_birth = int(df['birth year'].min())
        print('\n earliest year of birth is : \n'  , earliest_year_of_birth)
        most_recent_year_of_birth =int(df['birth year'].max())
        print('\n most recent year of birth is :\n', most_recent_year_of_birth)
        most_common_year_of_birth=int(df['birth year'].mode()[0])
        print('\n most common year of birth is : \n' , most_common_year_of_birth)
                                      

        

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
