# nyt2csv
A python script for creating csv files of New York Times articles through the use of the New York Times API.

The script is mostly intended for use in my own research, but I thought someone else might have a use for it and it was worth sharing.

To use the script first get a New York Times Developer API Key from https://developer.nytimes.com/apis. The API key is free and has a fairly generous usage policy. After you have your API key add the key to the script on the line marked "API = ''." You may also have to install the Python3 Requests package.

After you have added your API key the script can simply be run from the commandline by running the following command (on Linux, Windows and OS X may be a little different):

```
python3 nyt2csv.py search+term start_year ender_year
```

For example ``python3 nyt2csv.py labor 1970 1980`` will carry out a searh with the term labor and a year range of 1970 through 1980.


The script will then begin downloading the headline, abstract, and excerpt from each article to a CSV file with the name "search+term_startyear_endyear.csv" As the New York Times imposes a speed limit on how fast responses can be downloaded this can take some time--even hours in some cases. 

In the future I am planning on writing scripts that will parse this output into a format that works with various other programs such as DICTION and MALLET. I am also planning on writing scripts which allow you to combine multiple different CSV files while de-duplicating entries. Ultimately I will be trying to find a way to also integrate full texts. 

I'm a fairly novice programmer, it's not really my field honestly, so I'd be more than open to anyone who wants to make improvements to any of this.
