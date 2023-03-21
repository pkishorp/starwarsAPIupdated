from flask import Blueprint
from task_four import (
    films_data,
    peoples_data,
    planets_data,
    specie_data,
    starship_data,
    vehicles_data,
)
from Utils.fetch_data import hit_url
from Utils.randgen import ProduceChars


taskfour = Blueprint("taskfour", __name__, url_prefix="/api")


@taskfour.route("/taskfour/<resource>/")
def task_four(resource, start=1, end=8, limit=3):
    starships_data = []
    film_data = []
    vehicle_data = []
    species_data = []
    character_data = []
    planet_data = []

    obj = ProduceChars(start, end, limit - 1)
    resources = [element for element in obj]

    for item in resources:
        if resource == "starships":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(starship_data()[item])
            data = response_url.json()
            starship_data.append(data)

        if resource == "films":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(films_data()[item])
            data = response_url.json()
            film_data.append(data)

        if resource == "vehicles":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(vehicles_data()[item])
            data = response_url.json()
            vehicle_data.append(data)

        if resource == "species":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(specie_data()[item])
            data = response_url.json()
            specie_data.append(data)

        if resource == "planets":
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(planets_data()[item])
            data = response_url.json()
            planet_data.append(data)
        else:
            print(f"Generating the data for {resource} id :-> {item}")
            response_url = hit_url(peoples_data()[item])
            data = response_url.json()
            character_data.append(data)

    if resource == "films":
        return film_data
    elif resource == "characters":
        return character_data
    elif resource == "species":
        return species_data
    elif resource == "starships":
        return starships_data
    elif resource == "vehicles":
        return vehicle_data
    elif resource == "planets":
        return planet_data
