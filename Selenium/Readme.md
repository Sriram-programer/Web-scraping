# Walmart web scraping
Web scraping can be done by various modules in python. Here I used selenium webdriver for my web scraping.

# Selenium
Selenium is a portable framework for testing web applications. Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language (Selenium IDE). It also provides a test domain-specific language (Selenese) to write tests in a number of popular programming languages, including C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala. The tests can then run against most modern web browsers. Selenium runs on Windows, Linux, and macOS. It is open-source software released under the Apache License 2.0.

Read more about selenium in this
[documentation](https://www.selenium.dev/documentation/)

Walmart is one of the e-commerce websites and from this site we are going to fetch users reviews about Clorox-Disinfecting-Wipes product. Reviews helps us to understand more about the product on practical use.

This program sorts the review based on 'newest to oldest' category and fetch the following details till December 2020.

Datas fetched by this program
1) Reviewer name
2) Review submitted date
3) Review title
4) Review body
5) Star rating given by the user

These details will be stored as a CSV file which helps to view, sort or edit the data for further analysis.
