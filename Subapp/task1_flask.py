import json
import requests
from flask import Blueprint, Response
from Utils.randgen import ProduceChars
from task_one import get_url


# Flask is a class we used to instantiate an application
flask1 = Blueprint("flask1 ", __name__, url_prefix="/api")


@flask1.route("/flask1/<resource>/<int:count>/<int:start>/<int:end>")
def task_one(resource, count, start, end):
    obj = ProduceChars(start, end, count)

    resources_ids = [element for element in obj]
    print(f"[ INFO ] fetching data for following ids :{resources_ids}")
    content = []
    content2 = []
    for resource_id in resources_ids:
        print(f"[ INFO ] fetching data for resource id number : {resource_id}")

        url = get_url(resource, resource_id)
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            try:
                content.append(result["name"])
            except KeyError as ex:
                content2.append(result.get("title"))

    if content:
        output = {"Count": len(content), "Names": content}
        return content
    elif content2:
        output = {"Count": len(content2), "Names": content2}
        return content2

    # return Response(json.dumps(output), status=200, mimetype="application/json")
