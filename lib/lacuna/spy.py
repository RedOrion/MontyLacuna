
class Spy():
    """
    Attributes:
        id                     "id-goes-here",
        name                   "Jason Bourne",
        assignment             "Idle",
        possible_assignments   List of SpyAssignment objects
        level                  9,
        politics               0,
        mayhem                 20,
        theft                  40,
        intel                  33,
        offense_rating         570,
        defense_rating         150,
        is_available           1,
        available_on           "01 31 2010 13:09:05 +0600", # if can't be reassigned, this 
                                                            # is when will be available
        started_assignment     "01 31 2010 13:09:05 +0600",
        seconds_remaining      45,
        assigned_to            SpyBody object
        based_from             SpyBody object
    """

    def __init__( self, client, mydict:dict, *args, **kwargs ):
        self.client = client

        assignment_list = []
        for i in mydict['possible_assignments']:
            assignment_list.append( Assignment(self.client, i) )
        del mydict['possible_assignments']

        if 'assigned_to' in mydict:
            self.assigned_to = SpyBody(self.client, mydict['assigned_to'])
            del mydict['assigned_to']

        if 'based_from' in mydict:
            self.based_from = SpyBody(self.client, mydict['based_from'])
            del mydict['based_from']

        if 'mission_count' in mydict:
            self.mission_count = MissionCount(self.client, mydict['mission_count'])
            del mydict['mission_count']

        for k, v in mydict.items():
            setattr(self, k, v)

class Assignment():
    """ A task that a spy can be assigned to.

    Attributes:
            task        "Idle",
            recovery    0,          # in seconds
            skill       "none"

    Tasks:
        Idle
            Don't do anything.
        Counter Espionage.
            Passively defend against all attackers.
        Security Sweep
            Round up attackers.
        Intel Training
            Train in Intelligence skill
        Mayhem Training
            Train in Mayhem skill
        Politics Training
            Train in Politics skill
        Theft Training
            Train in Theft skill
        Political Propaganda
            Give happiness generation a boost. Especially effective on unhappy 
            colonies, but hastens an agent toward retirement.
        Gather Resource Intelligence
            Find out what's up for trade, what ships are available, what ships 
            are being built, where ships are travelling to, etc.
        Gather Empire Intelligence
            Find out what is built on this planet, the resources of the 
            planet, what other colonies this Empire has, etc.
        Gather Operative Intelligence
            Find out what spies are on this planet, where they are from, what 
            they are doing, etc.
        Hack Network 19
            Attempts to besmirch the good name of the empire controlling this 
            planet, and deprive them of a small amount of happiness.
        Sabotage Probes
            Destroy probes controlled by this empire.
        Rescue Comrades
            Break spies out of prison.
        Sabotage Resources
            Destroy ships being built, docked, en route to mining platforms, 
            etc.
        Appropriate Resources
            Steal empty ships, ships full of resources, ships full of trade 
            goods, etc.
        Assassinate Operatives
            Kill spies.
        Sabotage Infrastructure
            Destroy buildings.
        Sabotage BHG
            Prevent enemy planet from using Black Hole Generator.
        Incite Mutiny
            Turn spies. If successful they come work for you.
        Abduct Operatives
            Kidnap a spy and bring him back home.
        Appropriate Technology
            Steal plans for buildings that this empire has built, or has in 
            inventory.
        Incite Rebellion
            Obliterate the happiness of a planet. If done long enough, it can 
            shut down a planet.
        Incite Insurrection
            Steal a planet.

    Recovery:
        The spy is currently recovering from running his previous task.  This 
        is the time remaining, in seconds, of that recovery period.  After 
        that time expires, the spy will be available for another task.

    Skill:
        Which of the spy's skills will be used to calculate success.
    """
    def __init__( self, client, mydict:dict, *args, **kwargs ):
        self.client = client
        for k, v in mydict.items():
            setattr(self, k, v)

class MissionCount():
    """ The count of missions performed by the spy.

    A spy is forcefully retired after performing 150 of either type of mission 
    (offensive or defensive).  So to get the most life out of a spy, once he 
    gets to 149 of one type of mission, you should only use him for the other 
    type from then on.

    Attributes:
        offensive   149
        defensive   149
    """
    def __init__( self, client, mydict:dict, *args, **kwargs ):
        self.client = client
        for k, v in mydict.items():
            setattr(self, k, v)

class SpyBody():
    """ A body (planet, space station, etc).  This can be where the spy is 
    currently located or his home base (from which he is controlled).

    Attributes:
        body_id     id-goes-here",
        name        Earth",
        x           40,
        y           -71
    """
    def __init__( self, client, mydict:dict, *args, **kwargs ):
        self.client = client
        for k, v in mydict.items():
            setattr(self, k, v)

