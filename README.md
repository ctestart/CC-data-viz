# CC-data-viz
Code for scraping Customer Cone and AS relationship data needed for UROP visualization project.

1- Run 'python gettingASRelData.py 20171201 20201001' to download AS relationship data for all months starting in Dec 2017 and ending in Oct 2020.
bz2 files will be downloaded to the same folder your script is.

2- Run 'python gettingLinkData.py 20191201 20201001' to scrappe the downloaded data. It outputs a the dictionary of link: list of (date,relationship) as a json object.

3- 20171201_20201001.link-date-rel is a sample output of gettingLinkData.

4- readLinkData.py is a basic script that loads the json object dumped by gettingLinkData.
