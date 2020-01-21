<div align="center">
  <img src="./dotSafely/static/women-rights.svg" width="200px" height="250px"></img>

# `Safely`

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
</div> 
Safely helps women to navigate routes in a safe manner by providing three main features: 

- Safe routes
- Safety Timer alert
- SOS alerts to near ones

Allows users to mark a place as Unsafe, and displays safer routes, with timer alerts for emergency

-----------------------------------------------
## How it Works

* We use `CROWDSOURCED` Reviews of people marking a place as unsafe and  `GeoJSON Data` of Cities which inform about the shops, restaurants etc that are open along the route between source to destination

* Based on this parameters, we render two or three safest routes possible among multiple routes such that the unsafe zones are avoided and active zones are included
-----------------------------------------------


## Demo

### Home- signup/login to landing page  


![Demo](https://github.com/amisha-w/dotSafely/blob/master/gifs/3%20home.gif)  

### SafeRoute: routes alterative paths from A to B,avoiding Unsafe Places, and traversing near shops, restaurants etc that are opened at that time.  


![Demo](https://github.com/amisha-w/dotSafely/blob/master/gifs/4%20safe%20routes.gif)  

### Contribution- Users can report or mark an  area as unsafe describing their negative experience related to a place.  


![Demo](https://github.com/amisha-w/dotSafely/blob/master/gifs/9%20contribute.gif)  

### Safety Timer. A timer, when reaches a threshold, sends SOS alerts to authorities and near ones. User can use this timer in uncertainty.  


![Demo](https://github.com/amisha-w/dotSafely/blob/master/gifs/6%20safety%20timer.gif)  

### SOS feature sends SOS alerts and location of user to authorities as well as near ones.  


![Demo](https://github.com/amisha-w/dotSafely/blob/master/gifs/8%20SOS.gif)  


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

 This project was developed under 30-hours from scratch at `Dotslash 3.0 hackathon`, conducted by SVNIT, Surat and secured a `Special Mention in the All-Women's Category for hacking the theme Women's Safety`

-----------------------------------------------





