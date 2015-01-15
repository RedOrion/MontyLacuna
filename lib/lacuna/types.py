
import lacuna.exceptions as err

class Translator():
    """ Translates the human name and various misspellings of common 
    resources into the appropriate TLE system name.
    """

    def translate_shiptype( self, type:str ):
        """ Translates recognized ship type misspellings into the system ship 
        name.

        Arguments:
            - type -- String, generally passed in by the user.

        Returns the system ship name associated with the type passed in if it 
        was recognized.  Otherwise raises 
        :class:`lacuna.exceptions.NoSuchShipError`.

        Example::

            tr = lacuna.types.Translator()
            print( tr.translate_shiptype('srcs') )  # 'short_range_colony_ship'
        """

        system = [
            'barge', 'bleeder', 'cargo_ship', 'colony_ship', 'detonator', 'dory', 
            'drone', 'excavator', 'fighter', 'fissure_sealer', 'freighter', 
            'galleon', 'gas_giant_settlement_ship', 'hulk', 'hulk_fast', 
            'hulk_huge', 'mining_platform_ship', 'observatory_seeker', 'placebo',
            'placebo2', 'placebo3', 'placebo4', 'placebo5', 'placebo6', 'probe',
            'scanner', 'scow', 'scow_fast', 'scow_large', 'scow_mega',
            'security_ministry_seeker', 'short_range_colony_ship', 'smuggler_ship',
            'snark', 'snark2', 'snark3', 'space_station', 'spaceport_seeker',
            'spy_pod', 'spy_shuttle', 'stake', 'supply_pod', 'supply_pod2',
            'supply_pod3', 'supply_pod4', 'supply_pod5' 'surveyor', 'sweeper',
            'terraforming_platform_ship', 'thud',
        ]
        if type.lower() in system:
            return type.lower()

        trans = {
            "cargo": "cargo_ship",
            "cargo ship": "cargo_ship",
            "colony": "colony_ship",
            "colony ship": "colony_ship",
            "excav": "excavator",
            "fissure": "fissure_sealer",
            "fissure sealer": "fissure_sealer",
            "gg": "gas_giant_settlement_ship",
            "gas ": "gas_giant_settlement_ship",
            "gas giant": "gas_giant_settlement_ship",
            "gas giant settlement ship": "gas_giant_settlement_ship",
            "hulk fast": "hulk_fast",
            "hulk huge": "hulk_huge",
            "min": "mining_platform_ship",
            "minplat": "mining_platform_ship",
            "min plat": "mining_platform_ship",
            "mining platform ship": "mining_platform_ship",
            "obs": "observatory_seeker",
            "obs seeker": "observatory_seeker",
            "observatory seeker": "observatory_seeker",
            "placebo1": "placebo",
            "placebo 1": "placebo",
            "placebo 2": "placebo2",
            "placebo 3": "placebo3",
            "placebo 4": "placebo4",
            "placebo 5": "placebo5",
            "placebo 6": "placebo6",
            "scow fast": "scow_fast",
            "scow mega": "scow_mega",
            "sec": "security_ministry_seeker",
            "secmin seeker": "security_ministry_seeker",
            "sec min seeker": "security_ministry_seeker",
            "srcs": "short_range_colony_ship",
            "short range colony": "short_range_colony_ship",
            "short range colony ship": "short_range_colony_ship",
            "smug": "smuggler_ship",
            "smuggler": "smuggler_ship",
            "smuggler ship": "smuggler_ship",
            "snark1": "snark",
            "snark 1": "snark",
            "snark 2": "snark2",
            "snark 3": "snark3",
            "ss": "space_station",
            "hull": "space_station",
            "ss hull": "space_station",
            "space station": "space_station",
            "space station hull": "space_station",
            "sp": "spaceport_seeker",
            "sp seeker": "spaceport_seeker",
            "port seeker": "spaceport_seeker",
            "spaceport seeker": "spaceport_seeker",
            "space port seeker": "spaceport_seeker",
            "spy pod": "spy_pod",
            "shuttle": "spy_shuttle",
            "spy shuttle": "spy_shuttle",
            "supply": "supply_pod",
            "supply1": "supply_pod",
            "supply 1": "supply_pod",
            "supply pod": "supply_pod",
            "supply pod 1": "supply_pod",
            "supply2": "supply_pod2",
            "supply 2": "supply_pod2",
            "supply pod 2": "supply_pod2",
            "supply3": "supply_pod3",
            "supply 3": "supply_pod3",
            "supply pod 3": "supply_pod3",
            "supply4": "supply_pod4",
            "supply 4": "supply_pod4",
            "supply pod 4": "supply_pod4",
            "supply5": "supply_pod5",
            "supply 5": "supply_pod5",
            "supply pod 5": "supply_pod5",
            "terra": "terraforming_platform_ship",
            "terra plat": "terraforming_platform_ship",
            "terraforming platform ship": "terraforming_platform_ship",
        }
        if type.lower() in trans:
            return trans[ type.lower() ]
        raise err.NoSuchShipError( "{} is not a valid ship type.".format(type) )


