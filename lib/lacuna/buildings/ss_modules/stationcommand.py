
import lacuna.bc
import lacuna.building
import lacuna.ship

class stationcommand(lacuna.building.MyBuilding):
    path = 'stationcommand'

    def __init__( self, client, body_id:int = 0, building_id:int = 0 ):
        super().__init__( client, body_id, building_id )

