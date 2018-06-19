#!/usr/bin/env python
# -*- coding: utf-8 -*-


#   Copyright (C) 2018 Christoph Fink, University of Helsinki
#
#   This program is free software; you can redistribute it and/or
#   modify it under the terms of the GNU General Public License
#   as published by the Free Software Foundation; either version 3
#   of the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, see <http://www.gnu.org/licenses/>.


"""
Downloads images from Google image search for a specified search term,
saves list of titles and image urls to a CSV file
"""


import csv
import requests


def main():
    searchTerm = '"rhino horn"'
    apiKey = "INSERT YOUR GOOGLE CUSTOM SEARCH API KEY HERE"
    cseKey = "INSERT YOUR CUSTOM SEARCH ENGINE ID HERE (cx)"
    maxCount = 10000
    outFile = "/tmp/google-image-search.csv"

    count = 0

    with open(outFile, "a", newline="") as f:
        csvFile = csv.writer(f)
        # csvFile.writerow(["title", "link"])

        while count < maxCount:
            results = requests.get(
                "https://www.googleapis.com/customsearch/v1",
                params={
                    "searchType": "image",
                    "fields": "items(link,title)",
                    "key": apiKey,
                    "cx": cseKey,
                    "q": searchTerm,
                    "num": 10,
                    "start": (count + 1)
                }
            )

            items = results.json()["items"]

            for item in items:
                csvFile.writerow([
                    item["title"],
                    item["link"]
                ])

            count += len(items)


if __name__ == "__main__":
    main()
