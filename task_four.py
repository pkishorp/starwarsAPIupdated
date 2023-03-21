"""
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

"""

import argparse
from pprint import pprint

from Utils.randgen import ProduceChars
from Utils.fetch_data import hit_url
from Utils.timing import timeit
from task_one import get_url


# resource class
from resources.flims import Film
from resources.planets import Planet
from resources.vehicles import Vehicle
from resources.species import Species
from resources.people import People
from resources.starships import Starship
from resources.people import People

# pydantic classes(models)
from models.datamodels.people import People_
from models.datamodels.planets import Planet_
from models.datamodels.species import Specie_
from models.datamodels.starships import Starship_
from models.datamodels.films import Film_
from models.datamodels.vehicles import Vehicle_


def films_data():
    """
    Getting count of Films; Validating Characters data; Generates list of all Characters
    URLs
    """
    film_object = Film()
    total_films = film_object.get_count()
    print("Total films::", total_films)
    film_data = film_object.get_sample_data()
    film_data = Film_(**film_data)
    print("Film data is ::", film_data)
    global film_urls
    film_urls = film_object.get_resource_urls()
    print("Get all films urls::", film_urls)


def planets_data():
    """
    Getting count of Planets; Validating Characters data; Generates list of all Characters
    URLs
    """
    planet_object = Planet()
    total_planet = planet_object.get_count()
    print("Total Planet::", total_planet)
    planet_data = planet_object.get_sample_data()
    planet_data = Planet_(**planet_data)
    print("Planet data is ::", planet_data)

    global planet_urls
    planet_urls = planet_object.get_resource_urls()
    print("Get all planet urls::", planet_urls)


def vehicles_data():
    """
    Getting count of Vehicles; Validating Characters data; Generates list of all Characters
    URLs
    """
    vehicle_object = Vehicle()
    total_vehicle = vehicle_object.get_count()
    print("Total Vehicle ::", total_vehicle)
    vehicle_data = vehicle_object.get_sample_data(id_=4)
    print("Vehicle data is::", vehicle_data)
    global vehicle_urls
    vehicle_urls = vehicle_object.get_resource_urls()
    print("Get all vehicle urls::", vehicle_urls)


def specie_data():
    """
    Getting count of Species; Validating Characters data; Generates list of all Characters
    URLs
    """
    species_object = Species()
    total_species = species_object.get_count()
    print("Total Species::", total_species)
    species_data = species_object.get_sample_data()
    species_data = Specie_(**species_data)
    print("Species data::", species_data)
    global species_urls
    species_urls = species_object.get_resource_urls()
    print("Get all species urls::", species_urls)


def peoples_data():
    """
    Getting count of People; Validating Characters data; Generates list of all Characters
    URLs
    """
    people_object = People()
    total_people = people_object.get_count()
    print("Total People::", total_people)
    people_data = people_object.get_sample_data()
    people_data = People_(**people_data)
    print("People data::", people_data)
    global character_urls
    character_urls = people_object.get_resource_urls()
    print("Get all people url::", character_urls)


def starship_data():
    """
    Getting count of Starships; Validating Characters data; Generates list of all Characters
    URLs
    """
    starships_object = Starship()
    total_starships = starships_object.get_count()
    print("Total Starships::", total_starships)
    starships_data = starships_object.get_sample_data(id_=9)
    starships_data = Starship_(**starships_data)
    print("Starships data::", starships_data)

    global starship_urls
    starship_urls = starships_object.get_resource_urls()
    print("Get all starships url::", starship_urls)


@timeit
def main():
    films_data()
    planets_data()
    starship_data()
    vehicles_data()
    peoples_data()
    specie_data()


@timeit
def random_data():
    """
    Generates Three random numbers and fetch data for each resource's given by user, default:people
    Returns: List
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", default=3, type=int)
    parser.add_argument("-s", "--start", default=1, type=int)
    parser.add_argument("-e", "--end", default=5, type=int)
    parser.add_argument(
        "-r",
        "--resource",
        default="people",
        choices=["people", "planets", "films", "species", "vehicles", "starships"],
    )
    argument = parser.parse_args()
    print(f"parsed arguments are - {argument}")
    obj = ProduceChars(argument.start, argument.end, argument.limit)
    resources = [element for element in obj]

    for item in resources:
        if argument.resource == "films":
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            # response_url = get_url(film_urls[item], argument.resource)
            data = hit_url(film_urls[item])
            data = data.json()
            pprint(data)

        if argument.resource == "planets":
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            # response_url = get_url(planet_urls[item], argument.resource)
            data = hit_url(planet_urls[item])
            data = data.json()
            pprint(data)

        if argument.resource == "species":
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            # response_url = get_url(species_urls[item], argument.resource)
            data = hit_url(species_urls[item])
            data = data.json()
            pprint(data)

        if argument.resource == "starships":
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            # response_url = get_url(starship_urls[item], argument.resource)
            data = hit_url(starship_urls[item])

            data = data.json()
            pprint(data)

        if argument.resource == "vehicles":
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            # response_url = get_url(vehicle_urls[item], argument.resource)
            data = hit_url(vehicle_urls[item])
            data = data.json()
            pprint(data)

        else:
            print(f"\nGenerating the data for {argument.resource} id :-> {item}\n")
            # response_url = get_url(character_urls[item], argument.resource)
            data = hit_url(character_urls[item])
            data = data.json()
            pprint(data)


if __name__ == "__main__":
    main()
    random_data()
