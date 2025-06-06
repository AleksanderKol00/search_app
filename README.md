# Search App

## General info
The goal of the App it's to be able to find the index of the given value from given list of sorted numbers
 
The file with the numbers it's loaded from a file: `data_files/input.txt`

The app exposes `GET` endpoint on path:
`http//:<host>:<port>/search/{value}/`

## Technologies
* Python version: 3.13
* FastAPI

## Setup
`make install`

`python main.py`

## Run tests
`make test`

## Documentation
Swagger - `http//:<host>:<port>/docs/`