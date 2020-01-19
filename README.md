# `Safely`

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

Safely helps women to navigate routes in a safe manner by providing three main features: 

- [ x ] Safe routes
- [ x ] Safety Timer alert
- [ x ] SOS alerts to near ones

Allows users to mark a place as Unsafe, and displays safer routes, with timer alerts for emergency

-----------------------------------------------
## How it Works

* We use `CROWSDOURCED` Reviews of people marking a place as unsafe and  `GeoJSON Data` of Cities which inform about the shops, restaurants etc that are open along the route between source to destination

* Based on this parameters, we render two or three safest routes possible among multiple routes such that the unsafe zones are avoided and active zones are included
-----------------------------------------------


## Demo

![Demo]()
![Demo]()
![Demo]()

-----------------------------------------------

## Getting Started

### Prerequisites

* Django Framework
* MongoDB Cloud Storage



### API Integrations


* [Get the Leaflet JS CDN](https://leafletjs.com/)
* [ Get the HERE Maps app code and app id ](https://developer.here.com/c/mapAPIs?cid=Other-Google-MM-T4-Dev-Brand-E&utm_source=Google&utm_medium=ppc&utm_campaign=Dev_PaidSearch_DevPortal_AlwaysOn&gclid=CjwKCAiAh5_uBRA5EiwASW3IaplFdLkFaSmTyjhYPlNGVZLHpIdJ8wmXqqaPy1JkK6OucFfYFrWLwhoC6F4QAvD_BwE&gclsrc=aw.ds)

Setup project environment with virtualenv and pip.
```
$ virtualenv venv
$ venv/scripts/activate
$ pip install -r https://github.com/amisha-w/dotSafely/blob/master/requirements.txt


$ cd projectname/
$ python manage.py migrate
$ python manage.py runserver

```

### Database Setup

Create Mongo Collections for:
* CrowdSourcing Data
* GeoJSON Data of Cities
* User Information



-----------------------------------------------
## Built With

* [Django](https://www.djangoproject.com)
* [HEREMaps](https://developer.here.com/c/mapAPIs?cid=Other-Google-MM-T4-Dev-Brand-E&utm_source=Google&utm_medium=ppc&utm_campaign=Dev_PaidSearch_DevPortal_AlwaysOn&gclid=CjwKCAiAh5_uBRA5EiwASW3IaplFdLkFaSmTyjhYPlNGVZLHpIdJ8wmXqqaPy1JkK6OucFfYFrWLwhoC6F4QAvD_BwE&gclsrc=aw.ds) - The MAPs API
* [LeafletJS](https://leafletjs.com/)

-----------------------------------------------
## Future Enhancements

- [ ] Include Live Traffic Data as a parameter for safety metric 
- [ ] The data can be passed to civil authorities that can make use of it and improvise the safety conditions of the marked places


-----------------------------------------------

## Contributions

 We're are open to `enhancements` & `bug-fixes`

 ----------------------------------------------- 

## Contributors
* [Gayatri Srinivasan](https://github.com/gayatri-01)
* [Amisha Waghela](https://github.com/amisha-w)
* [Het Joshi](https://github.com/hrj-star)


-----------------------------------------------

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

-----------------------------------------------





