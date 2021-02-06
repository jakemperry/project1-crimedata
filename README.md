# Project 1 - Crime Data
**Collaborators**
- [BAF95](https://github.com/BAF95)
- [DavidZapataCSUF](https://github.com/DavidZapataCSUF)
- [mbarrera2020](https://github.com/mbarrera2020)
- [jakemperry](https://github.com/jakemperry)

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
A detailed list of data files and their sources is provided in the "Data" folder.  Data sources for this project include:
- [OpenJustice website](https://openjustice.doj.ca.gov/data)
    - Crimes and Clearances (With Arson)
    - Domestic Violence Related Calls for Service
- [US Census Data API](https://www.census.gov/data/developers/data-sets.html)
- [Google Maps API](https://developers.google.com/maps/)
- [CA Dept of Alcoholic Beverage Control](https://www.abc.ca.gov/licensing/licensing-reports/licenses-by-county/)
- [Arrest data from 2010-2019, LACity.org](https://data.lacity.org/Public-Safety/Arrest-Data-from-2010-to-2019/yru6-6re4)
    - This file is over 300MB and exceeds the GitHub file size limit.  Please download directly from the link above.  Thanks!
- [Financial Crimes Enforcement Network](https://www.fincen.gov/reports/sar-stats)
- [Casinos and Crime in the USA](https://www.researchgate.net/publication/265568177_Casinos_and_crime_in_the_USA)
- [Casinos, Crime, and Community Costs](https://www.jstor.org/stable/40042957?seq=1)
- [NYPD Shooting Incident Data (Historic), NYC OpenData](https://data.cityofnewyork.us/Public-Safety/NYPD-Shooting-Incident-Data-Historic-/833y-fsy8)
- [United States Cities Database](https://simplemaps.com/data/us-cities)

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

### Presentation
A copy of the presentation is available to view through [Google Drive](https://drive.google.com/file/d/1LQ6TOHCkjd6KEG7ucwhH50s-uqIqoiA5/view?usp=sharing)

### Good to know
- The Census and Google Maps API portions of this project require keys.  Please confirm you have an API key in a config file saved in the appropriate directory before running jupyter notebooks/python files that reference API keys.