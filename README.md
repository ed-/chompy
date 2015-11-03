Chompy drills into JSON documents based on the command-line arguments supplied.

    $ cat rainfall.json | chom.py 'City name=Brisbane' Population
    "1857594"


Stompy prefixes the complete path to every value in a JSON document.

    $ cat rainfall.json | stom.py | grep -e City.name -e Rainfall | grep -B1 Darwin
    2.Annual Rainfall = 1714.7
    2.City name = Darwin


Whompy converts PrettyTable documents into JSON, for further parsing.

    $ cat rainfall.table | whom.py | chom.py 'City name=Perth' Population
    "1554769"
