
import argparse, lacuna, os, sys

class BuildShips:

    def __init__(self):
        self.bindir = os.path.abspath(os.path.dirname(sys.argv[0]))

        parser = argparse.ArgumentParser(
            description = 'This will build as many of a single type of ship as you want, up to the maximum that can be built across all shipyards on your planet.  If there are already ships in your build queue, this will figure that out and only build what it can.',
            epilog      = 'EXAMPLE: python bin/build_ships.py "Earth" sweeper (fills the build queues of all shipyards on Earth with sweepers).',
        )
        ### https://docs.python.org/3.4/library/argparse.html#the-add-argument-method
        parser.add_argument( 'name', 
            metavar     = '<planet>',
            action      = 'store',
            help        = 'Name of planet on which to build ships.'
        )
        parser.add_argument( 'type', 
            metavar     = '<shiptype>',
            action      = 'store',
            help        = "Type of ship to build (eg 'scow_mega')."
        )

        parser.add_argument( '--num', 
            metavar     = '<count>',
            action      = 'store',
            type        = int,
            default     = 0,
            help        = "Number of ships to build.  Defaults to 'fill up all available build queue slots'.  If you request more ships than your shipyards can queue, as many as possible will be built."
        )
        parser.add_argument( '--level', 
            metavar     = '<lvl>',
            dest        = 'min_lvl',
            action      = 'store',
            type        = int,
            default     = 1,
            help        = 'Minimum shipyard level to use for building.  Defaults to 1.'
        )
        parser.add_argument( '--file', 
            dest        = 'config_file',
            metavar     = '<config_file>',
            action      = 'store',
            default     = self.bindir + "/../etc/lacuna.cfg",
            help        = "Path to the config file.  Defaults to 'ROOT/etc/lacuna.cfg'"
        )
        parser.add_argument( '--section', 
            dest        = 'config_section',
            metavar     = '<section>',
            action      = 'store',
            default     = 'sitter',
            help        = "Config file section.  Defaults to 'sitter'."
        )
        parser.add_argument( '--quiet', 
            dest        = 'quiet',
            metavar     = '<quiet>',
            action      = 'store',
            help        = "Silence all output."
        )

        self.args   = parser.parse_args()


    def connect( self ):
        return lacuna.clients.Member(
            config_file     = self.args.config_file,
            config_section  = self.args.config_section
        )


    def get_shipyards( self, planet ):
        yards = planet.get_buildings_bytype( 'shipyard', self.args.min_lvl )
        if not yards:
            raise RuntimeError("You don't have any shipyards of the required level.")
        return( yards )


    ### CHECK
    ### see comments in the script about this.
    def determine_buildable(self, yards):
        """ Ensures we can actually build the requested ship type, and figures 
        out how many of them we should build.

        Returns the number of ships we should queue across all shipyards.

        This number to be built does not take current build queues into 
        account.  Four level 30 SYs are going to return 120, no matter what 
        those SYs are currently doing.

        Raises KeyError if the shiptype isn't buildable for whatever reason.
        """
        ships, docks_avail, build_queue_max, build_queue_used = yards[0].get_buildable()
        if not docks_avail:
            raise KeyError("You don't have any docks available to hold more ships.")
        if not build_queue_max:
            raise KeyError("All of your build queue slots are occupied.")
        if not len([ i for i in ships if i.type == self.args.type ]):
            raise KeyError( "The type of ship requested, {}, cannot be built.".format(self.args.type) )
        ### If the 'num to build' arg is 0, we're to build all we can.
        requested_num = self.args.num if self.args.num > 0 else build_queue_max
        ### If we were asked to build more than we can, back off to just 
        ### building what we can.
        num_to_build = requested_num if requested_num < build_queue_max else build_queue_max
        return num_to_build


