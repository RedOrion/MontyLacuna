
from lacuna.building import Building

class terraformingplatform(Building):
    path = 'terraformingplatform'

    def __init__( self, client, body_id:int = 0, building_id:int = 0 ):
        super().__init__( client, body_id, building_id )
