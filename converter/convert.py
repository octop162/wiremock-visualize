import json
import requests
from jinja2 import Environment, FileSystemLoader, select_autoescape

response = requests.get('http://wiremock:8080/__admin/')
mappings = response.json().get('mappings')

if mappings is None:
    print('FILE ERROR.')
    exit(1)

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)
template = env.get_template("template.html")
print(template.render(mappings=mappings))