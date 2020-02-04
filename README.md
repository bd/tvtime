# tvtime
_eliminating needless choice in media consumption_

`tvtime` is a web application intended to eliminate the question "Which episode of my favorite show am I going to watch right now?" by the simple expedient of choosing for you.

## MVP
The minimum viable product will be take as a given that the show in question is _Bob's Burgers_. A single url (TBD) will, on page load, begin playing a randomly selected episode. Expected controls of the media viewer, e.g. start/stop/fullscreen/cc, will be accessible. 

The MVP _will_ require a base container infrastructure.

## Development Environs

``` bash 
# a few aliases will help with developing tvtime, and will serve ye well with docker in general. add em to your shell profile. E.g.
echo "alias dc='docker-compose'" >> ~/.zshrc
echo "alias dcr='docker-compose --rm --service-ports run'" >> ~/.zshrc 

# the first time you run, or whenever you have unapplied migrations
dcr web django-admin migrate`

# run the test suite
dcr web django-admin run test

# to get a bash shell on the django container
dcr web bash

# to bring up the project s.t. the site is served at localhost:8000
docker-compose up
```


## Future's Features
Advanced features and extensions are imagined, though no roadmap is currently implied, nor should the following be taken as priority-ranked.

- user accounts
    - anonymous
    - OAuth/pwd
    - linked streaming accounts
    - white/blacklist, favorites
- local media selector

    
    