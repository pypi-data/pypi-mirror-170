# Directus-Python-Client

This library aims to provide a simple and easy to use interface to the Directus API. It is written in Python and uses
the requests library.

## Motivation

Working with APIs can sometimes be a bit cumbersome. If you are not careful, boilerplates can quickly lead to code
duplication. Most of the time they come from similar workflows. Like authentication, request header configuration or
just the execution of the request itself.

## Documentation

### Authentication

```python
from directus_api import DirectusApi

# Authentication
directus_api = DirectusApi(username="username", password="password", endpoint="https://directus.example.com")
```

```python```

### Items

Retrieve Items:

```python
...

# Get all items from a collection
items = directus_api.get_items(collection="collection_name")

# Get only 42 items from a collection
items = directus_api.get_items(collection="collection_name", limit=42)

print(items)
```

Create Items:

```python
...

# Create a single item or multiple items
item = directus_api.create_items(collection="collection_name", data=[{"title": "My new item"}])

```