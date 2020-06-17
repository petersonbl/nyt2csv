# nyt2csv
A python script for creating csv files of New York Times articles through the use of the New York Times API.

The script is mostly intended for use in my own research, but I thought someone else might have a use for it and it was worth sharing. In the long run I intend to make it more user friendly and provide several other scripts to manipulate the resulting CSV files. 

Currently to use the script you need to manually enter your search term ("Q"), New York Times Developer API Key ("API_KEY"), and year range into the script itself. When you run the script it will use the NYT API to search for articles in one year blocks. The articles it finds will have their headlines, abstracts, and first-paragraphs (where available) downloaded to a CSV file. The CSV file can then be used with programs like Voyant Tools to analyze the use of words over time.

In the future I am planning on writing scripts that will parse this output into a format that works with various other programs such as DICTION and MALLET. I am also planning on writing scripts which allow you to combine multiple different CSV files while de-duplicating entries. Ultimately I will be trying to find a way to also integrate full texts. 

I'm a fairly novice programmer... My PhD is in History afterall... so I'd be more than open to anyone who wants to make improvements to any of this.
