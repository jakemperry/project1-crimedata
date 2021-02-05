# Project 1 - Crime Data
**Collaborators**
- BAF95
- DavidZapataCSUF
- mbarerra2020
- jakemperry

## Project Hypothesis and Core Message
- Crimes are tied to institutions of similar nature
    - Crimes may also be associated with population
- Goals: identify trends in data to determine correlation/causation relationship

### Questions and Motivations
- Do places with casinos attract more criminal activities related to gambling crimes?
- Do gun stores increase gun crime activities?
- Is there a relationship between the number of liquor stores in an area to the number of reported crimes in the area?
- How is population related to gun crimes?

### Data Sources
- [OpenJustice website](https://openjustice.doj.ca.gov/data)
- [US Census Data API](https://www.census.gov/data/developers/data-sets.html)
- [Google Maps API](https://developers.google.com/maps/)
- [CA Dept of Alcoholic Beverage Control](https://www.abc.ca.gov/licensing/licensing-reports/licenses-by-county/)
- City of Los Angeles
- NYPD

### Data Analysis Methods
Methods include:
- Importing data from csv files
- Calling for data using an API
- Cleaning data with pandas
- Visualizing data with matplotlib

### Summary of Conclusions and Discussion
- There is no evidence casinos attract crime
- Number of gun stores have no impact on gun crime
- Population size has some correlation with gun crime, but no clear causation
- There is a relationship between the following:
    - Number of liquor licenses and number of calls
    - Number of liquor licenses and number of weapons
    - Number of liquor licenses and population
    - Population and number of calls