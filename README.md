# Xfinity Gateway Stats

Gather the "Xfinity Network" stats from an Xfinity Gateway Modem and return the results as json

## Basic Usage
```
export XFG_PASSWD="my_xfinity_gw_passwrd"
./get_stats.py
{
  "XFINITY Network": {
    "Internet:": "Active",
    "Local time:": "2020-10-11 10:56:04",
    "System Uptime:": "5 days 7h: 13m: 29s",
... blah blah blah ...
    {
      "Index": "32",
      "Unerrored Codewords": "3630326681",
      "Correctable Codewords": "6",
      "Uncorrectable Codewords": "0"
    }
  ]
}
```

## Installation

- Install requirements: `pip install requirements.txt`
- Set your password: `export XFG_PASSWD="mypassword"`
  - This is the password used to log into your device
  - Typically at http://10.0.0.1
- Run the script: `./get_stats.py`
- Have a beer!

## Fields Gathered

```
./get_stats.py | jq 'keys'
[
  "CM Error Codewords",
  "Cable Modem",
  "Downstream",
  "Initialization Procedure",
  "Upstream",
  "XFINITY Network"
]
```

