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

Update Items:

```python
...

# Update a single item or multiple items. Primary key (here 'id') is required.
item = directus_api.update_items(collection="collection_name", data=[{"title": "My updated item", "id": 1}])

```

Delete Items:

```python
...
# Delete a single item by id from a collection
item = directus_api.delete_item_by_id(collection="collection_name", id=1)

# Delete all items from a collection
item = directus_api.delete_all_items_from_collection(collection="collection_name")

```

#
...

