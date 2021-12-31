# midterm-project-2021

INTRO TO CS MIDTERM PROJECT: ANIMATED CHOROPLETH MAP

by: yi-an liao

due date: january 3, 2022

**files included:**
- energy-cons-cleaned.csv (cleaned data for global energy consumption)
- energy-cons.csv (original data for global energy consumption; not cleaned)
- test.csv (sample data from energy-cons.csv for testing)
- choropleth-map-FINAL.py (final program)

**data cleaning process:**
1. delete rows without iso-3 country codes to get rid of regional and continent data.
2. delete rows that have data earlier than 1980 or later than 2015.
3. delete all data from years that aren't a decade marker or half a decade.
4. reset index starting from 0 afterwards because why not and it looks better.
5. end product: data is only from countries and the only years i have data for are 1980, 1985, 
1990,1995, 2000, 2005, 2010, and 2015.
