# Webscraping-Yelp-Restaurants

### Demonstration Link: https://youtu.be/gGuXr16btzU

## Description:
The objective of this project is to develop a web scraping application using Python and Selenium to extract information about the best Thai restaurants in Santa Ana, CA from the Yelp website. The application will retrieve details such as the restaurant's website, phone number, location, top 3 most popular dishes, average prices, minimum price dish, and maximum price dish (if available) for each restaurant. The extracted data will then be stored in a CSV file for further analysis.

## Key Steps:
1) Searching for Thai Restaurants: The application will utilize the Yelp website and search for the "best Thai restaurants" in Santa Ana, CA. It will navigate to the search results page and extract the list of restaurants displayed on the front page.
2) Restaurant Details: For each restaurant on the search results page, the application will click on the restaurant's Yelp page to gather additional details. The details to be extracted include the company website, phone number, location, top 3 most popular dishes, average prices, minimum price dish, and maximum price dish (if available).
3) Web Scraping with Selenium: Selenium, a web scraping framework, will be used to interact with the Yelp website. The application will automate the process of clicking on restaurant pages, retrieving the desired information, and navigating back to the search results page to continue gathering data for other restaurants.
4) Data Extraction: The application will extract the required information from the restaurant pages by locating and parsing the relevant HTML elements using Selenium's functions. For example, it will identify and extract the restaurant's website URL, phone number, location details, popular dishes, and pricing information.
5) Data Storage: The extracted data will be stored in a CSV file. Each restaurant's details will be recorded in a separate row, with columns corresponding to the information collected (e.g., website, phone number, location, dishes, average prices, minimum price dish, maximum price dish).
6) Error Handling: The application will implement error handling mechanisms to handle cases where certain information is not available for a restaurant. If any variable is not accessible, it will be set as "None" in the CSV file. Additionally, the application will log any errors encountered during the scraping process and provide appropriate feedback to the user.
7) Scalability and Performance: The project will be designed to efficiently handle a large number of restaurants. Techniques like asynchronous scraping or parallel processing can be implemented to speed up the data retrieval process and optimize performance.

## Conclusion
By automating the process of finding the best Thai restaurants in Santa Ana, CA and extracting relevant details from Yelp, this project aims to provide users with a consolidated dataset for analysis and decision-making. Users can utilize the CSV file to explore the collected information, compare different restaurants, or even build applications on top of the gathered data.
