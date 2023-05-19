import jmespath

data = {
    "heroes": [
        {"name": "Spider-Man", "power": "web-slinging"},
        {"name": "Iron Man", "power": "genius "},
        {"name": "Captain America", "power": "super strength"}
    ]
}


query = "heroes[*].name"


result = jmespath.search(query, data)

print(result)
