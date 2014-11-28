
import lacuna.bc 
import lacuna.building 
import lacuna.spy

class intelligence(lacuna.building.MyBuilding):
    path = 'intelligence'

    def __init__( self, client, body_id:int = 0, building_id:int = 0 ):
        super().__init__( client, body_id, building_id )

    @lacuna.building.MyBuilding.call_returning_meth
    def view( self, *args, **kwargs ):
        """ View stats on current spy numbers, as well as costs to train new 
        spies.

        Returns a single lacuna.spy.IntelView object.
        """
        return lacuna.spy.IntelView(self.client, kwargs['rslt']['spies'])


    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.building.MyBuilding.call_building_meth
    def train_spy( self, *args, quantity:int = 1, **kwargs ):
        """ Trains one or more spies.  "Train", in this case, means "create".
        The "quantity" argument defaults to 1.

        Returns a dict including the keys:
            - trained -- Integer number added to the training queue.  Always included in retval, but may be set to 0.
            - not_trained -- Integer number not added to the training queue.  Only appears in retval if its value is non-zero.
            - reason_not_trained -- Dict containing the reason that "not_trained" is set.  Only appears in retval if "not_trained" appears.  Includes:
                - code -- 1011,
                - message -- "Not enough food to train a spy."
        """
        pass

    @lacuna.building.MyBuilding.call_returning_meth
    def view_spies( self, page_number:int = 1, *args, **kwargs ):
        """ Returns info on one page (up to 30) spies.  There are a maximum of 
        three pages of spy data.  
        
        To get info on all of your spies at once, see also view_all_spies().

        Returns a list of up to 30 lacuna.spy.Spy objects.
        """
        spy_list = []
        for i in kwargs['rslt']['spies']:
            spy_list.append( lacuna.spy.Spy(self.client, i) )
        return spy_list

    @lacuna.building.MyBuilding.call_returning_meth
    def view_all_spies( self, *args, **kwargs ):
        """ Returns information on all of the spies controlled from this 
        planet.

        Returns a list of up to 90 lacuna.spy.Spy objects.
        """
        spy_list = []
        for i in kwargs['rslt']['spies']:
            spy_list.append( lacuna.spy.Spy(self.client, i) )
        return spy_list

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.building.MyBuilding.call_building_meth
    def burn_spy( self, spy_id:int, *args, **kwargs ):
        """ Burns (deletes) an existing spy. """
        pass

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.building.MyBuilding.call_building_meth
    def name_spy( self, spy_id:int, name:str, *args, **kwargs ):
        """ Renames an existing spy."""
        pass

    @lacuna.building.MyBuilding.call_returning_meth
    def assign_spy( self, spy_id:int, assignment:str, *args, **kwargs ):
        """ Assigns a spy to a task.
        
        Possible assignments for each spy can be found by calling view_spies() 
        or view_all_spies().  A full list of all assignments can be found at 
        https://us1.lacunaexpanse.com/api/Intelligence.html#assignment

        Requires captcha.

        Returns a tuple:
            - spy -- lacuna.spy.Spy object
            - mission_result -- lacuna.spy.MissionResult object
        """
        spy     = lacuna.spy.Spy( self.client, kwargs['rslt']['spy'] )
        rslt    = lacuna.spy.MissionResult( self.client, kwargs['rslt']['mission'] )
        return( spy, rslt )

    @lacuna.bc.LacunaObject.set_empire_status
    @lacuna.building.MyBuilding.call_building_meth
    def subsidize_training( self, *args, **kwargs ):
        """ Subsidizes training of all spies currently in the queue.

        Costs 1 E per spy.
        """
        pass

