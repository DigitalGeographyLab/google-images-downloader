# Download images from Google image search

Adapt [\_\_main\_\_.py](__main__.py) to include your [Google Custom Search API key](https://developers.google.com/custom-search/json-api/v1/overview) and the [ID of your “Custom Search Engine”](https://developers.google.com/custom-search/docs/xml_results#cxsp), as well as a search term and the number of image records to return (cf. [Pricing](https://developers.google.com/custom-search/json-api/v1/overview#pricing) of the API access; currently 100 requests á 10 records free per day, then 5$/1000 requests up to 10000)

Then run `python .` and find an output CSV file in the location specified in the script (default: `/tmp/google-image-search.csv`).
