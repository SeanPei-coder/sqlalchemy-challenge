# sqlalchemy-challenge

## Background

Suppose I have decided to treat myself to a long holiday vacation in Honolulu, Hawaii! To help with my trip planning, I need to do some climate analysis on the area.

## Step 1 - Climate Analysis and Exploration

To begin, I use Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

- Design a query to retrieve the last 12 months of precipitation data.


- Select only the date and prcp values.


- Load the query results into a Pandas DataFrame and set the index to the date column.


- Sort the DataFrame values by date.


- Plot the results using the DataFrame plot method.

![alt text](https://github.com/SeanPei-coder/sqlalchemy-challenge/blob/main/images/precipitation.png)

- Use Pandas to print the summary statistics for the precipitation data.

![alt text](https://github.com/SeanPei-coder/sqlalchemy-challenge/blob/main/images/describe.png)


### Station Analysis

- Design a query to calculate the total number of stations.


- Design a query to find the most active stations.

  - List the stations and observation counts in descending order.


  - Which station has the highest number of observations?


- Design a query to retrieve the last 12 months of temperature observation data (TOBS).


  - Filter by the station with the highest number of observations.


  - Plot the results as a histogram with bins=12.
  
![alt text](https://github.com/SeanPei-coder/sqlalchemy-challenge/blob/main/images/station-histogram.png) 

## Step 2 - Climate App
Now that I have completed my initial analysis, design a Flask API based on the queries that I have just developed.

- Use Flask to create my routes.

### Routes

- /


  - Home page.


  - List all routes that are available.




- /api/v1.0/precipitation


  - Convert the query results to a dictionary using date as the key and prcp as the value.


  - Return the JSON representation of your dictionary.




- /api/v1.0/stations

  - Return a JSON list of stations from the dataset.



- /api/v1.0/tobs


  - Query the dates and temperature observations of the most active station for the last year of data.


  - Return a JSON list of temperature observations (TOBS) for the previous year.




- /api/v1.0/`<start>` and /api/v1.0/`<start>`/`<end>`


  - Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  - When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

  - When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
  
## Other Analyses
  
### Temperature Analysis I

- Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?


- Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.


- Use the t-test to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II

- The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d. The function will return the minimum, average, and maximum temperatures for that range of dates.


- Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").


- Plot the min, avg, and max temperature from the previous query as a bar chart.


  - Use the average temperature as the bar height.


  - Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
  
![alt text](https://github.com/SeanPei-coder/sqlalchemy-challenge/blob/main/images/temperature.png)

### Daily Rainfall Average

- Calculate the rainfall per weather station using the previous year's matching dates.


- Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.


- Create a list of dates for the trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.


- Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.


- Use Pandas to plot an area plot (stacked=False) for the daily normals.

![alt text](https://github.com/SeanPei-coder/sqlalchemy-challenge/blob/main/images/daily-normals.png)




