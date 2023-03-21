from typing import List
from pydantic import parse_obj_as
from multiprocessing.pool import ThreadPool
from resources.flims import Film

from models.datamodels.films import Film_
from models.datamodels.species import Specie_
from models.datamodels.vehicles import Vehicle_
from models.datamodels.people import People_
from models.datamodels.planets import Planet_
from models.datamodels.starships import Starship_

from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from Utils.fetch_data import fetch_data_new
from Utils.timing import timeit

pool = ThreadPool(8)


def store_characters_data():
    characters = film_data.characters
    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "homeworld",
        "created",
        "edited",
        "url",
    ]

    characters_data = pool.map(fetch_data_new, characters)
    chars_data = parse_obj_as(List[People_], characters_data)
    for char_data in chars_data:
        char_data = People_(**dict(char_data))
        char_values = [
            char_data.name,
            char_data.height,
            char_data.mass,
            char_data.hair_color,
            char_data.skin_color,
            char_data.eye_color,
            char_data.birth_year,
            char_data.gender,
            char_data.homeworld,
            char_data.created.strftime("%y-%m-%d"),
            char_data.edited.strftime("%y-%m-%d"),
            char_data.url,
        ]
        char_id = int(char_data.url.split("/")[-2])
        insert_resource("characters", "char_id", char_id, char_columns, char_values)


def store_planets_data():
    planets = film_data.planets
    planet_columns = [
        "name",
        "rotation_period",
        "orbital_period",
        "diameter",
        "climate",
        "gravity",
        "terrain",
        "surface_water",
        "population",
        "created",
        "edited",
        "url",
    ]

    planets_data = pool.map(fetch_data_new, planets)
    planets_data = parse_obj_as(List[Planet_], planets_data)
    for planet_data in planets_data:
        planet_data = Planet_(**dict(planet_data))
        planet_values = [
            planet_data.name,
            planet_data.rotation_period,
            planet_data.orbital_period,
            planet_data.diameter,
            planet_data.climate,
            planet_data.gravity,
            planet_data.terrain,
            planet_data.surface_water,
            planet_data.population,
            planet_data.created.strftime("%y-%m-%d"),
            planet_data.edited.strftime("%y-%m-%d"),
            planet_data.url,
        ]

        planet_id = int(planet_data.url.split("/")[-2])
        insert_resource("planet", "planet_id", planet_id, planet_columns, planet_values)


def store_vehicles_data():
    vehicles = film_data.vehicles
    vehicle_columns = [
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "crew",
        "passengers",
        "cargo_capacity",
        "consumables",
        "vehicle_class",
        "created",
        "edited",
        "url",
    ]

    vehicles_data = pool.map(fetch_data_new, vehicles)
    vehicles_data = parse_obj_as(List[Vehicle_], vehicles_data)
    for vehicle_data in vehicles_data:
        vehicle_data = Vehicle_(**dict(vehicle_data))
        vehicle_values = [
            vehicle_data.name,
            vehicle_data.model,
            vehicle_data.manufacturer,
            vehicle_data.cost_in_credits,
            vehicle_data.length,
            vehicle_data.max_atmosphering_speed,
            vehicle_data.crew,
            vehicle_data.passengers,
            vehicle_data.cargo_capacity,
            vehicle_data.consumables,
            vehicle_data.vehicle_class,
            vehicle_data.created.strftime("%y-%m-%d"),
            vehicle_data.edited.strftime("%y-%m-%d"),
            vehicle_data.url,
        ]

        vehicle_id = int(vehicle_data.url.split("/")[-2])

        insert_resource(
            "vehicle", "vehicle_id", vehicle_id, vehicle_columns, vehicle_values
        )


def store_starships_data():
    starships = film_data.starships
    starship_columns = [
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "max_atmosphering_speed",
        "crew",
        "passengers",
        "cargo_capacity",
        "consumables",
        "hyperdrive_rating",
        "MGLT",
        "starship_class",
        "created",
        "edited",
        "url",
    ]

    starships_data = pool.map(fetch_data_new, starships)
    starships_data = parse_obj_as(List[Starship_], starships_data)
    for starship_data in starships_data:
        starship_data = Starship_(**dict(starship_data))
        starship_values = [
            starship_data.name,
            starship_data.model,
            starship_data.manufacturer,
            starship_data.cost_in_credits,
            starship_data.length,
            starship_data.max_atmosphering_speed,
            starship_data.crew,
            starship_data.passengers,
            starship_data.cargo_capacity,
            starship_data.consumables,
            starship_data.hyperdrive_rating,
            starship_data.MGLT,
            starship_data.starship_class,
            starship_data.created.strftime("%y-%m-%d"),
            starship_data.edited.strftime("%y-%m-%d"),
            starship_data.url,
        ]

        starship_id = int(starship_data.url.split("/")[-2])

        insert_resource(
            "starship", "starship_id", starship_id, starship_columns, starship_values
        )


def store_species_data():
    species = film_data.species
    specie_columns = [
        "name",
        "classification",
        "designation",
        "average_height",
        "skin_colors",
        "hair_colors",
        "eye_colors",
        "average_lifespan",
        "homeworld",
        "language",
        "created",
        "edited",
        "url",
    ]

    species_data = pool.map(fetch_data_new, species)
    species_data = parse_obj_as(List[Specie_], species_data)
    for specie_data in species_data:
        specie_data = Specie_(**dict(specie_data))
        specie_values = [
            specie_data.name,
            specie_data.classification,
            specie_data.designation,
            specie_data.average_height,
            specie_data.skin_colors,
            specie_data.hair_colors,
            specie_data.eye_colors,
            specie_data.average_lifespan,
            specie_data.homeworld,
            specie_data.language,
            specie_data.created.strftime("%y-%m-%d"),
            specie_data.edited.strftime("%y-%m-%d"),
            specie_data.url,
        ]

        specie_id = int(specie_data.url.split("/")[-2])

        insert_resource(
            "species", "species_id", specie_id, specie_columns, specie_values
        )


@timeit
def main():
    store_characters_data()
    store_planets_data()
    store_vehicles_data()
    store_starships_data()
    store_species_data()


if __name__ == "__main__":
    film_obj = Film()
    film_ = film_obj.get_sample_data(id_=1)
    film_data = Film_(**film_)

    # establishing the connection
    conn = get_db_conn()

    film_columns = [
        "title",
        "episode_id",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]
    film_values = [
        film_data.title,
        film_data.episode_id,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]
    film_id = int(film_data.url.split("/")[-2])
    result = insert_resource("film", "film_id", film_id, film_columns, film_values)
    main()
