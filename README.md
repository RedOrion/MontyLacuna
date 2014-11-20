MontyLacuna
===========

Python Client for The Lacuna Expanse

This is essentially a port of the Perl Games::Lacuna::Client module to Python.  
No attempt is being made to preseve the same API used by GLC, but I'd like to 
replicate all of the functionality.

The main goal is to help me learn Python, but I'd like to end up with a fully 
working package.

## Prerequisites
- virtualenv
  - You want to do this before any other installing, so the module installs will install 
    to your virtual environment.
  - $ sudo apt-get install python-virtualenv
  - Again, this probably doesn't count as a true prereq, but it's something I did.
  - After installing virtualenv, I created one for this project with:
    - $ virtualenv -p /usr/bin/python Python3
    - $ source Python3/bin/activate
      - Now "python script.py" will call Python3/bin/python.
    - You can turn that virtualenv off with just $ deactivate
- pip
  - This gets installed by virtualenv, so if you're using that, you're good.
- requests
  - pip install requests
  - CHECK It might make sense to replace this with urllib, since it's standard - one less 
    thing for the user to have to install
- beaker
  - pip install beaker

- Prereqs for documentation creation; not needed by script runners or writers
  - sphinx
    - pip install sphinx
    - This isn't really a prerequisite of using MontyLacuna, but it's (likely) what I'm 
      using to generate the documentation.
  - Sphinx Read The Docs! theme
    - pip install sphinx_rtd_theme

## Complete
Nothing.

## Working
"working" means that all functionality exists, and quickie scripts appear to 
work, but it hasn't been fully tested yet.

- Alliance
- Body
- Captcha
- Clients
- Empire
- Inbox
- Map
- Stats
- Buildings
  - "all functionality" is a bit of a stretch here.  The Buildings base class 
exists, and stub classes exist for all buildings in the game.  I need to work 
through those building stubs to make them each do whatever-it-is they're each 
supposed to do.
  - archaeology
  - blackholegenerator
  - development
  - distributioncenter
  - embassy
  - energyreserve
  - entertainment
  - foodreserve
  - geneticslab
  - intelligence
  - inteltraining
  - libraryofjith
  - mayhemtraining
  - mercenariesguild
  - miningministry
  - missioncommand
  - network19
  - observatory
  - oracleofanid
  - orestorage
  - park
  - planetarycommand
  - politicstraining
  - security
  - shipyard
  - spaceport
  - ssla
  - subspacesupplydepot
  - thedillonforge
  - thefttraining
  - themepark
  - trading (base class)
    - trade (trade ministry)
    - transporter (sst)
    - I purposely skipped some methods in both trade and transporter.  They'll never be 
      used and I'm getting bored.  Add them if you're feeling productive.  The skipped 
      methods are noted in comments at the top of both files.
 - recycler (base class)
    - wasteexchanger
    - wasterecycling
  - Space Station Modules
    - policestation

## Incomplete/Not Started
- Payments
 - There's a real good chance this will never be worked on as part of this 
   project.
- Announcement

## TBD
- The Space Station modules haven't been completed.
  - I'm up to working on Parliament, which is only partway done.
- I've started to re-organize the buildings/ modules into subdirectories for sanity.  
  Finish that.  Remember to update __init__.py when moving a file.
- Everything needs to be tested on Windows.  In particular:
  - bin/captcha_test.py
  - installing modules via pip or however it works on windows.
  - Run through the whole Getting Started instruction set on a fresh Python install on 
    Windows to make sure the docs are correct.
- Ack through everything for "CHECK" and fix.
- Whenever we instantiate a MyBuilding object, we're calling view() on that building 
  automatically - I'm not convinced that's what should be happening.  At the very least, 
  we should be caching the results.
- lacuna.bc.SubClass is idiotically named.  It's meant as a full-coverage superclass, not 
  a subclass.  Do something about that name.
- The logfile attribute of clients is meant to be optional, but ISTR getting an explosion 
  on a test at some point where I didn't have a logfile set.  Confirm that setting a 
  logfile is optional.
- I'm going to need at least a few useful scripts in bin/ before making this public.

## Documentation
http://sphinx-doc.org/tutorial.html
https://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example

- First run only:
  - In ROOT:
    - sphinx-quickstart (this starts a question-and-answer section):
      - root path: ./doc
      - I entered my name, the name of the project, and version 0.1.
      - I chose 'y' for the question about autodoc.
      - All else I accepted the defaults.
  - in ROOT/doc/:
    - Edit conf.py (which was just created):
      - Line 21 (ish):
        - sys.path.insert(0, os.path.abspath('../lib'))
      - That tells Sphinx where the code lives
  - To generate docu based on docstrings:
    - in ROOT:
      - sphinx-apidoc -o doc/ lib/ lacuna
        - http://sphinx-doc.org/invocation.html#invocation-apidoc
        - This creates several more .rst files in doc/
          - lacuna.rst
          - lacuna.buildings.rst
          - modules.rst
          - my_validate_email.rst
      - Of those generated files, the only one I'm explicitly adding to the main toctree 
        is "my_validate_email".  I don't want lacuna or modules listed there at all.  I've 
        added lacuna.buildings to the toctree of buildings.rst.
  - All of the other .rst files in doc/ were not created automatically, but by hand.  If 
    you add a new module, you'll want to copy one of the existing .rst files and edit it 
    appropriately for your new module.

- To publish the docs generated on the master branch to gh-pages:
  - The HTML pages produced by "make html" end up in {underscore}build/html/.  Those HTML 
    files contain links to _modules/, _sources/, and _static/.  For whatever reason, 
    github pages does not like the underscore on the front of directory names - it refuses 
    to host files from there.  These underscore directories and the links to them are what 
    fix_underscores.pl is fixing.
  - $ pwd
    /home/jon/work/MontyLacuna/doc
  - $ make html
  - $ perl fix_underscores.pl
  - $ cp -Rip doc/{underscore}build/html ~/Desktop
  - $ cd ..
  - $ git status
    - Commit any changes to master
  - $ git co gh-pages
  - $ rm -rf html
  - $ mv ~/Desktop/html ./
  - $ git add -A html
    - There are directories in master containing files in .gitignore.  Since those files 
      don't get commited to master, their directories don't get removed when checking out 
      gh-pages.  So don't just "git add -A .", or you'll add that extraneous crap that has 
      nothing to do with gh-pages.  Just "git add -A html".
  - $ git commit -m "docs!"
  - $ git push origin gh-pages
  - $ git co master
  - Wait a $time_period (Github claims it may take up to 10 minutes, but I've never had it 
    take more than a few seconds), and then go look at your pretty docs online.

