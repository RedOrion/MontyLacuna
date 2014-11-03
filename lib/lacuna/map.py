
import lacuna.bc
import lacuna.body

class Map(lacuna.bc.LacunaObject):
    """All Map methods require a session ID, so these can only be used by a
    Member, not a Client.
    """

    path = 'map'

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.bc.LacunaObject.call_member_named_meth
    def get_star_map( self, mydict, *args, **kwargs ):
        """The passed-in dict must contain the keys top, bottom, left, right.  
        Each must be an integer within the star map (so >= -1500 and <= 1500).

        rv['stars'] contains a list of dicts.
        Sample dict:
            {
                'color': 'red',
                'id': '15320',
                'name': 'Oot Yaeplie Oad',
                'x': '288',
                'y': '-1118',
                'zone': '1|-4'
            }
        """
        pass

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.bc.LacunaObject.call_member_meth
    def get_stars( self, x1, x2, y1, y2, *args, **kwargs ):
        """ rv is the same as for get_star_map()."""
        pass

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.bc.LacunaObject.call_member_meth
    def check_star_for_incoming_probe( self, star_id, *args, **kwargs ):
        """ rv['incoming_probe'] will be 1 for true, 0 for false."""
        pass

    @lacuna.bc.LacunaObject.call_returning_meth
    def get_star( self, star_id, *args, **kwargs ):
        """ Returns a Star object.  """
        star = Star( self.client, kwargs['rslt']['star'] )
        return(star)

    @lacuna.bc.LacunaObject.call_returning_meth
    def get_star_by_name( self, star_name, *args, **kwargs ):
        """ Returns a Star object.  

            star = my_map.get_star_by_name( 'Sol' )

        star_name must be an exact name, not a partial.  rv is identical to 
        get_star().
        """
        star = Star( self.client, kwargs['rslt']['star'] )
        return star

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.bc.LacunaObject.call_member_meth
    def get_star_by_xy( self, x, y, *args, **kwargs ):
        """x and y must be exact coords, not a range.  rv is identical to get_star().  """
        pass

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.bc.LacunaObject.call_member_meth
    def search_stars( self, partial_name, *args, **kwargs ):
        """ partial_name must be at least 3 characters.  Matches up to 25 stars whose names
        START with partial_name (NOT stars whose names just contain partial_name).
        rv is a list, identical to get_star_map().
        """
        pass

    @lacuna.bc.LacunaObject.call_member_named_meth
    def probe_summary_fissures( self, mydict, *args, **kwargs ):
        """ mydict must contain the key 'zone', with a value of the zone you want to check,
        expressed in standard TLE zone notation (0|0).

        I currently can't find a zone with a fissure in it to test, but the documented value 
        of 'fissures' when one or more is found is a dict:
            "fissures" : {
                    "345" : {
                        "name"   : "Mercury",
                        "id"     : 345,
                        "orbit"  : 1,
                        "x"      : -40,
                        "y"      : 29,
                        "type"   : "habitable planet",
                        "image"  : "p13",
                        "size"   : 58,
                    },
                    "735" : {
                    ...
                    }
                }

        When there's no fissure existing (or known to you or your allies), rv is documented
        as being an empty list:
            "fissures" : None

        BE CAREFUL WITH THIS!  It looks like we're getting back a struct on a positive 
        response, but an empty list on a negative response.  Sigh.
        """
        pass

    ### 
    ### Non-API methods
    ###

    def get_orbiting_planet( self, star_name:str, planet_name:str ):
        """ Returns a Body object for a specific planet orbiting a specific 
        star.  Requires that you can see the system in your starmap.  This 
        means that you or one of your alliance mates must either have a probe 
        at the star, or have an oracle in range.

            planet = map.get_orbiting_planet( 'Star name', 'Name of planet orbiting that star' )
        """
        my_map = self.client.get_map()
        star = my_map.get_star_by_name(star_name)
        target_planet = ''
        for i in star.bodies:
            if i.name == planet_name:
                target_planet = i
        if not target_planet:
            raise KeyError("Unable to find target planet", planet_name, ".")
        return target_planet


class Star():
    """ 
    Attributes:
        color   'red',
        id      '12345',
        name    'Clou Oghofr Oap',
        x       '100',
        y       '-100',
        zone    '0|0',
        bodies: [
                    <lacuna.body.Body object>,
                    <lacuna.body.Body object>,
                    ...
                ]
    """

    def __init__( self, client, star_dict:dict, *args, **kwargs ):
        self.client = client

        if 'status' in star_dict:
            del( star_dict['status'] )

        body_objs = []
        for b in star_dict['bodies']:
            body_objs.append( lacuna.body.Body(self, b) )
        self.bodies = body_objs

        if 'bodies' in star_dict:
            del( star_dict['bodies'] )
        for k, v in star_dict.items():
            setattr(self, k, v)


