import requests
import csv
import time


def nyt2csv(api, q, start_year, end_year):
    # Define initial variables
    output_file = f"{q}_{start_year}_{end_year}.csv"
    start_time = time.time()
    years = range(start_year, end_year)
    retry = True
    records = 0
    # Iterate over every year as defined in variable years
    for x in years:
        # Set up initial conditions for working through the year
        page = 0
        more = True
        start_date = f"{x}0101"
        end_date = f"{x}1231"
        # Check that more is available and then make a request
        while more:
            print(x, page)
            input_url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?' \
                        f'q={q}' \
                        f'&api-key={api}' \
                        f'&page={page}' \
                        f'&begin_date={start_date}' \
                        f'&end_date={end_date}'
            print(input_url)
            r = requests.get(input_url)
            r = r.json()
            # Take a look at what has returned and then process it.
            try:
                docs = r['response']['docs']
                for n in range(len(docs)):
                    raw_date = docs[n]['pub_date']
                    # This year processing is inelegant and should be improved, though it works
                    processed_date = raw_date.split("T")
                    processed_date = processed_date[0]
                    processed_date = processed_date.split("-")
                    year = int(processed_date[0])
                    month = int(processed_date[1])
                    day = int(processed_date[2])
                    url = docs[n]['web_url']
                    abstract = docs[n]['abstract']
                    abstract = f'"{abstract}"'
                    lead = docs[n]['lead_paragraph']
                    lead = f'"{lead}"'
                    headline = docs[n]['headline']['main']
                    headline = f'"{headline}"'
                    desk = docs[n]['news_desk']
                    section = docs[n]['section_name']
                    output = [year, month, day, desk, section, headline, abstract, lead, url]
                    print(output)
                    f = open(output_file, "a")
                    with f:
                        writer = csv.writer(f)
                        writer.writerow(output)
                        records += 1
                    # if we made it this far things must be working again so retry is set back to True
                    retry = True
                # Check to see if there are more available pages
                if len(docs) == 10 and page <= 200:
                    page = page + 1
                    more = True
                else:
                    more = False
            # Catch KeyError exception which indicates an error and
            # retry in two minutes if retry is True
            except KeyError:
                print(r['status'])
                if retry:
                    print("Sorry NYT. I will back off for four minutes.")
                    time.sleep(240)
                    # The retry may fail again if you have gone over the daily limit on the API
                    # Retry is thus set to False to prevent constant retrying after that limit is hit
                    # In the future a server based version will simply back off for 24 hours.
                    retry = False
                else:
                    print("Ending script due to error")
            time.sleep(10)
    end_time = time.time()
    run_time = end_time - start_time
    print(f"Run completed with {records} records processed in {run_time} seconds")


if __name__ == "__main__":
    API = ''  # Enter your NYT Developers API Key Here
    Q = ''  # Enter your query here 
    START_YEAR = 1950
    END_YEAR = 2020
    nyt2csv(API, Q, START_YEAR, END_YEAR)


