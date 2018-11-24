# Sport
Sport related scripts/tutorials/web scraping. Several things I automated with python or have been built on top of other python packages, like Garmin Connect Export (https://github.com/pe-st/garmin-connect-export).

The motivation of this repository is simple: Get your data out of the data silos. Exported files or any other content
should be in an open format with which you can do anything you like.

## Lapscrap
Lapscrap is a small python script that scrapes the data from mylaps.com and export this to a CSV file. mylaps.com publishes metrics of sport events, but the metrics are not easy to export. The script is 'smart' enough to understand that the tables of most events are slighty different. Be aware that published the exported data in the public is not allowed in Europe due to the new GDPR laws.  

Lapscrap needs several libraries, these can be installed with pip.
* urllib2
* BeautifulSoup

