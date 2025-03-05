import requests

# URL of the API endpoint
url = "https://fasih-sm.bps.go.id/analytic/api/v2/assignment/datatable-all-user-survey-periode"

# Headers for the request
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": "fasih-sm.bps.go.id",
    "Origin": "https://fasih-sm.bps.go.id",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "X-XSRF-TOKEN": "38c3f35d-ee09-4f00-a3ea-f68ef1f74485",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

# Cookies for the request
cookies = {
  ""
}


# Payload for the request
payload = {
  "draw": 4,
  "columns": [
    {
      "data": "id",
      "name": "",
      "searchable": True,
      "orderable": False,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "codeIdentity",
      "name": "",
      "searchable": True,
      "orderable": False,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data1",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data2",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data3",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data4",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data5",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data6",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data7",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data8",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    },
    {
      "data": "data10",
      "name": "",
      "searchable": True,
      "orderable": True,
      "search": {
        "value": "",
        "regex": False
      }
    }
  ],
  "order": [
    {
      "column": 0,
      "dir": "asc"
    }
  ],
  "start": 900,
  "length": 300,
  "search": {
    "value": "",
    "regex": False
  },
  "assignmentExtraParam": {
    "region1Id": None,
    "region2Id": None,
    "region3Id": None,
    "region4Id": None,
    "region5Id": None,
    "region6Id": None,
    "region7Id": None,
    "region8Id": None,
    "region9Id": None,
    "region10Id": None,
    "surveyPeriodId": "f328c798-4279-4fb9-bccc-af35e5dbb212",
    "assignmentErrorStatusType": -1,
    "assignmentStatusAlias": None,
    "data1": None,
    "data2": None,
    "data3": None,
    "data4": None,
    "data5": None,
    "data6": None,
    "data7": None,
    "data8": None,
    "data9": None,
    "data10": None,
    "userIdResponsibility": None,
    "currentUserId": None,
    "regionId": None
  }
}


# Make the POST request
response = requests.post(url, headers=headers, cookies=cookies, json=payload)

# Print the response
print("Status Code:", response.status_code)
# export to json file
with open("data2.json", "w") as f:
    f.write(response.text)

