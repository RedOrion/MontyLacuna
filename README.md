MontyLacuna
===========

A Python Client for The Lacuna Expanse.

This is essentially a port of the Perl Games::Lacuna::Client module to Python.  

## TBD
- assign_spies tasks should be case insensitive at least, and really should 
  have a translator set up.
    - Trying to assign guys currently on "mayhem training" to Idle (so I can 
      Do other stuff with them) results in "mayhem training is not a valid 
      task or abbreviation".  Whoops.
    - you run a spy report (which caches), then send spies to a planet that 
      needs them, then run assign_spies.  assign_spies is using the same cache 
      as spy_report, so it thinks no spies are on your target, even though you 
      just sent some.
        - Only way to clear the cache is by re-running the report script with 
          --fresh, which isn't very intuitive.


- Everything needs to be tested on Windows.  In particular:
  - bin/captcha_test.py
  - installing modules via pip or however it works on windows.
  - Run through the whole Getting Started instruction set on a fresh Python install on 
    Windows to make sure the docs are correct.
- Ack through everything for "CHECK" and fix.
  - Even if you find no CHECK marks, leave this list item here.  I have a tendency to 
    re-add these marks.

