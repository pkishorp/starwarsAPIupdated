

***********************[Project name:: starwarAPI]***********************************

Website::https://swapi.dev/documentation


PROJECT STRUCTURE
--------------------
starwarsAPI (project root directory)

  - task_one.py 
  - task_two.py
  - task_three.py
  - task_four.py
  - requirements.txt
  - README.md 
  - venv  
  - -resources
      - __init__.py
      - films.py
      - planets.py 
      - species.py
      - starships.py
      - vehicles.py
      - people.py
      - base.py
  - Subapp
      - task4_flask
      - task1_flask
  - main_flask.py

  - utils
      - __init__.py
      - fetch_data.py
      - randgen.py
      - timing.py
  - models
      - __init__.py
      - datamodels
          - __init__.py
          - films.py
          - planets.py 
          - species.py
          - starships.py
          - vehicles.py


----------------------
PROBLEM STATEMENT :: 1
----------------------
The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.
____________________________
PROBLEM STATEMENT :: 2
-----------------------------
Refined Program

The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.

____________________________
PROBLEM STATEMENT :: 3
-----------------------------
Command line application
 We have to fetch the data of first film from swapi.dev
    - After pulling out the data write json data in `output.txt`
        - Then we have to list down only first name and last name of the character who worked in 1st film [ LIST FORMAT]
        - Also we have to list down the names of planets and vehicles which are in 1st film in [ LIST FORMAT]

_______________________________
PROBLEM STATEMENT :: 4
______________________________

1. TODO - import all resource classes here -> Done
2. TODO - get count of each resource       -> Done
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty pprint output (from ppprint import ppprint)



