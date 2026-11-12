# Your web map doesn't need a third-party service, just GeoDjango

Conf42 Blog, 2021-05-27. https://www.conf42.com/blog/python2021/geodjango-maps-spatialite-to-postgis

In short: Paolo Melchiorre (20tab) at Conf42 Python 2021 on building web maps with GeoDjango, from a SpatiaLite file to PostGIS and a bounding-box API

A map on your site doesn't have to mean shipping your data to an external service and paying for every tile of it. At Conf42 Python 2021, Paolo Melchiorre, CTO of 20tab and a Django contributor, builds a web map from an empty Django project to an interactive map backed by PostGIS and a REST API, using only GeoDjango, Leaflet and free software.

The narrative device is a mountain hike: each stage of the climb (he quotes the altitude, 1,883 m at the start, 2,793 m at the summit) maps to a stage of the code, from a gentle stretch to the part where things get steep. Fittingly, the map he builds is the one where he pins the peaks he's reached.

## Why keep the geodata in your own database?

The abstract makes the case: outsourcing the map often turns into a data and cost management problem. Keeping geographic data in your own database lets you run geospatial queries on it, and Django has had the tools for this for years. The talk's history of GeoDjango is a good reminder: `django.contrib.gis` arrived around Django 1.0 (about 2008), SpatiaLite support in 1.1, multiple backends in 1.2, OpenLayers widgets in 1.6, the GeoJSON serializer in 1.8 and GeoIP2 in 1.9.

## Stage one: an empty map in a few files

The first stretch is ordinary Django (3.1 in the demo, on Python 3.9): `startproject mymap`, `startapp markers`, a `TemplateView` and a template. Then Leaflet, which he picks for being free software, mobile friendly, well documented and light, around 39 KB of gzipped JavaScript. A `div` with id `map`, a full-screen CSS rule, an OpenStreetMap tile layer and `map.fitWorld()`, and you have a blank world map served by `runserver`.

## Stage two: GeoDjango on a single SQLite file

Next comes the geographic part. Install GDAL (the OSGeo library for reading and writing raster and vector formats), add `django.contrib.gis` to the installed apps, and switch the database engine to SpatiaLite, the spatial extension for SQLite. Its appeal is the simple architecture: a complete database is an ordinary file.

The model is two fields, a `name` and a `PointField` called `location`. To enter data without building a form, he registers it with GeoDjango's `OSMGeoAdmin`, which gives the admin a map widget where you click to place a point. The view serializes all markers to GeoJSON, the template embeds them with Django's `json_script` tag, and Leaflet's `L.geoJSON` draws them with popups.

It works, and it's fast with a handful of markers. Melchiorre is upfront about the limit: put many more markers inside the page and loading gets much slower, with Leaflet struggling to render them all.

## Stage three: PostGIS and only the markers you can see

The summit push swaps SpatiaLite for PostGIS, which he calls the best GeoDjango backend, for its spatial types, indexes and functions. The requirements file grows to psycopg2, Django REST framework, djangorestframework-gis and django-filter.

The API is small. A `GeoFeatureModelSerializer` with `location` as the geo field, a `ReadOnlyModelViewSet` using the `InBBoxFilter` on `location`, and a default router under `/api/`. On the front end, the page no longer knows where the markers are, so it tries `map.locate()` to centre on the user and falls back to a low-zoom default. An async function fetches `/api/markers/?in_bbox=...` with the current map bounds, and it runs on Leaflet's `moveend` event.

The result is a map that stays fluid with any number of markers in the database: requests fire only when the user stops panning, and only for the visible area, so both the data traffic and Leaflet's rendering work shrink to what is on screen.

## What he would add next, and where to learn

His list of next steps: marker customisation, filtering on related data, clustering on both front end and back end, and geocoding to place markers from an address. His tips: the GeoDjango docs on djangoproject.com, the query details on postgis.net, the source code on GitHub, and gis.stackexchange.com, where he suggests trying to answer questions yourself. On reading the code, Paolo Melchiorre said at Conf42 Python 2021: "there is something you can learn only from the code." The slides are released under CC BY-SA 4.0.

## Who should watch

Django developers who have a map on the backlog and assumed it meant a paid API. It's a hands-on walkthrough with every file shown, not a GIS theory talk.

## Related Conf42 talks

- AbdurRahmaan Janhangeer on [Shopyo, Flask with Django-style organisation](https://www.conf42.com/Python_2021_AbdurRahmaan_Janhangeer_shopyo_flask), from the same event.
- Vishrut Kohli on [production-ready task queues with Celery and Django](https://www.conf42.com/Python_2021_Vishrut_Kohli_productionready_distributed_task_queue_system_celery_django_queing).
- Craig West on [agentic AI with Django](https://www.conf42.com/Python_2025_Craig_West_agentic_ai_django) at Conf42 Python 2025.

[Watch Paolo Melchiorre's talk](https://www.conf42.com/Python_2021_Paolo_Melchiorre_Django_Web_Development_Rest_APIs_Map_GeoDjango_SpatiaLite_SQLite_PostGI) from [Conf42 Python 2021](https://www.conf42.com/python2021).

## From 20tab

20tab is the Rome-based Python software company where Paolo Melchiorre is CTO; the team has built many maps with Django.

- 20tab: [20tab.com](https://www.20tab.com/en/)

[Watch the talk on YouTube](https://youtu.be/9dPQ0DDGVO4).

## Watch the talk

[Maps with Django](https://www.conf42.com/Python_2021_Paolo_Melchiorre_Django_Web_Development_Rest_APIs_Map_GeoDjango_SpatiaLite_SQLite_PostGI) at Conf42 Python 2021.
