MontyLacuna
===========

A Python Client for The Lacuna Expanse.

This is essentially a port of the Perl Games::Lacuna::Client module to Python.  

## TBD
- fix up stations_report.py and its library to give proper options and output 
  etc. then document it.
    - Add some printf formatting to the output -- numbers aren't lined up, 
      etc.
- Some sort of update script
    - Something that does the same job as "git pull origin master", but doesn't require 
      the user to install git.
        - for list of files and/or directories:
            - back up and archive existing stuff
            - pull down newest latest greatest from github using http
            - leave the (dated) backup lying around somewhere (var/ probably)
        - The point is to save the user from having to re-download the whole package, 
          re-create their config file again, and lose any customizations they might have 
          made to the code.
- Ack through everything for "CHECK" and fix.
  - Even if you find no CHECK marks, leave this list item here.  I have a tendency to 
    re-add these marks.

