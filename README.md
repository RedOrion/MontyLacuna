MontyLacuna
===========

[![Join the chat at https://gitter.im/tmtowtdi/MontyLacuna](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/tmtowtdi/MontyLacuna?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A Python Client for The Lacuna Expanse.

This is essentially a port of the Perl Games::Lacuna::Client module to Python.  

## TBD
- ships_report.py doesn't appear to be reporting on fighters that have been 
  recalled from a deployment
  - Are we just reporting on Docked ships?  If so, the report should have the 
    option of displaying other tasks, and should make clear what it's 
    displaying.
- see stats.py for how methods should be documented throughout.
- Ack through everything for "CHECK" and fix.
  - Even if you find no CHECK marks, leave this list item here.  I have a tendency to 
    re-add these marks.
- Add a per-user planet-name-abbreviation setup somehow (config file?  maybe an 
  interactive script that stores the abbreviations in a database?).  To allow the user to 
  just type "1.1" as an argument instead of "My Planet Number 1.1" wherever a script needs 
  a planet or station name.
  - Working on this -- see bin/abbrv.py and its library.

## Docs Fixes
Except for stats, I'm working in alpha order and recording everything I've checked.
- stats
- bc
- caching
- body
- building
- captcha
- client
- empire
- exceptions
- glyphs
- inbox
- map
- plan
- resource
- ship
- spy
- trading
- types

...That's it for the root.  

