
from lacuna.bc import LacunaObject
from lacuna.building import MyBuilding
from lacuna.ship import TradeableShip
from lacuna.spy import Prisoner
from lacuna.plan import OwnedPlan
from lacuna.glyph import OwnedGlyph

class TradeBldg(MyBuilding):
    """ Base class for trade and transporter buildings.  """

    def __init__( self, client, body_id:int = 0, building_id:int = 0 ):
        super().__init__( client, body_id, building_id )

    @MyBuilding.call_returning_meth
    def get_ships( self, *args, **kwargs ):
        """ Get ships available to be added to a trade as merchandise.

        Returns a tuple:
            ships       List of TradeableShip objects.
            space_used  Amount of cargo space used by each ship.  
                        Always 10000.
        """
        mylist = []
        for i in kwargs['rslt']['ships']:
            mylist.append( TradeableShip(self.client, i) )
        return(
            mylist,
            kwargs['rslt']['cargo_space_used_each']
        )

    @MyBuilding.call_returning_meth
    def get_prisoners( self, *args, **kwargs ):
        """ Get prisoners available to be added to a trade as merchandise.

        Returns a tuple:
            prisoners       List of Prisoner objects.
            space_used      Amount of cargo space used by each prisoner.  
                            Always 350.
        """
        mylist = []
        for i in kwargs['rslt']['prisoners']:
            mylist.append( Prisoner(self.client, i) )
        return(
            mylist,
            kwargs['rslt']['cargo_space_used_each']
        )

    @MyBuilding.call_returning_meth
    def get_plan_summary( self, *args, **kwargs ):
        """ Get plans available to be added to a trade as merchandise.

        Returns a tuple:
            plans           List of OwnedPlan objects.
            space_used      Amount of cargo space used by each prisoner.  
                            Always 10000.
        """
        mylist = []
        for i in kwargs['rslt']['plans']:
            mylist.append( OwnedPlan(self.client, i) )
        return(
            mylist,
            kwargs['rslt']['cargo_space_used_each']
        )

    @MyBuilding.call_returning_meth
    def get_glyph_summary( self, *args, **kwargs ):
        """ Get glyphs available to be added to a trade as merchandise.

        Returns a tuple:
            glyphs          List of OwnedGlyph objects.
            space_used      Amount of cargo space used by each prisoner.  
                            Always 10000.
        """
        mylist = []
        for i in kwargs['rslt']['glyphs']:
            mylist.append( OwnedGlyph(self.client, i) )
        return(
            mylist,
            kwargs['rslt']['cargo_space_used_each']
        )

    @MyBuilding.call_returning_meth
    def view_my_market( self, page_number:int = 1, *args, **kwargs ):
        """ Shows the trades you currently have offered.

        Arguments:
            page_number     Optional integer page number to view.  25 trades 
                            shown per page.  Defaults to 1. 

        Returns a tuple:
            trades          List of ExistingTrade objects
            count           Total number of trades you have up
            page_number     The page that the "trades" list appeared on.  Same 
                            value that you passed as an argument, or 1.
        """
        mylist = []
        for i in kwargs['rslt']['trades']:
            mylist.append( ExistingTrade(self.client, i) )
        return(
            mylist,
            kwargs['rslt']['trade_count'],
            kwargs['rslt']['page_number'],
        )

    @LacunaObject.set_empire_status
    @MyBuilding.call_building_meth
    def withdraw_from_market( self, trade_id:int, *args, **kwargs ):
        """ Withdraws one of your trades from the market.  If the trade had been 
        on the SST market, refunds your 1 E posting cost.

        Arguments:
            trade_id    Integer ID of the trade to withdraw
        """
        pass

    @MyBuilding.call_returning_meth
    def view_market( self, page_number:int = 1, filter:str = '', *args, **kwargs ):
        """ Shows the trades you currently have offered.

        Arguments:
            page_number     Optional integer page number to view.  25 trades 
                            shown per page.  Defaults to 1. 
            filter          Optional string to narrow down the types of trades 
                            returned.  Valid filters:
                                energy food glyph ore plan prisoner ship waste water 

        Returns a tuple:
            trades          List of ExistingTrade objects
            count           Total number of trades you have up
            page_number     The page that the "trades" list appeared on.  Same 
                            value that you passed as an argument, or 1.
        """
        mylist = []
        for i in kwargs['rslt']['trades']:
            mylist.append( ExistingTrade(self.client, i) )
        return(
            mylist,
            kwargs['rslt']['trade_count'],
            kwargs['rslt']['page_number'],
        )

    @LacunaObject.set_empire_status
    @MyBuilding.call_building_meth
    def accept_from_market( self, trade_id:int, *args, **kwargs ):
        """ Accepts a trade from the market.  When buying from the SST market, 
        an additional 1 E processing cost is automatically charged in addition
        to the 'ask' price displayed for the trade.

        Requires captcha.

        Requires 'trade_id', integer ID of the trade to purchase.
        """
        pass

    @LacunaObject.set_empire_status
    @MyBuilding.call_building_meth
    def get_stored_resources( self, *args, **kwargs ):
        """ Returns resources stored onsite and available for trading.

        Retval includes 'resources', a dict:
            {   water:      10000,
                waste:      20000,
                bauxite:    25,
                ..self.  }
        """
        pass

class ExistingTrade():
    """ These are trades that exist on either the Trade or SST market, either 
    posted by you or another empire.

    Attributes:
        id              "id-goes-here",
        date_offered    "01 31 2010 13:09:05 +0600",
        ask             25,     # essentia
        offer           List of items
                            [   "Level 21 spy named Jack Bauer (prisoner)",
                                "4,000 bauxite",
                                "gold glyph"     ]
        empire          Info on offering empire.  Will only exist if this is a
                        trade offered by somebody else - your own trades do not
                        include this.
                            {   "id" : "id-goes-here",
                                "name" : "Earthlings"   }

        These will only be available for trades on the Trade Ministry.  The SST
        deliveries are instant, so this information doesn't pertain to the SST.

        body            Dict - info on the sending body
                            {   "id" : "id-goes-here" }
        delivery        Dict - info on delivery time (in seconds)
                            {   "duration" : "4600" }
                                    
    """
    def __init__( self, client, mydict:dict, *args, **kwargs ):
        self.client = client
        for k, v in mydict.items():
            setattr(self, k, v)





