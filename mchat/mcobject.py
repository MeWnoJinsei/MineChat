from mc import *
inRunner = None
mci18n = None
try:
    from mchat import mci18n
except ImportError:
    inRunner = True
if inRunner:
    exec("from py.mchat import mci18n")


class Position:
    x = None
    y = None
    z = None

    def __init__(self, position):
        self.x, self.y, self.z = position

    def __str__(self):
        return str.format("{} {} {}", self.x, self.y, self.z)


class Dimension:
    id = None

    def __init__(self, dimensionId):
        self.id = dimensionId

    def __str__(self):
        dimName = mci18n.t("mcobject.dimension.unknown")
        if self.id == 0:
            dimName = mci18n.t("mcobject.dimension.world")
        elif self.id == 1:
            dimName = mci18n.t("mcobject.dimension.nether")
        elif self.id == 2:
            dimName = mci18n.t("mcobject.dimension.end")
        return dimName


class Location:
    position = None
    dimension = None

    def __init__(self, position, dimension):
        self.position, self.dimension = position, dimension

    def __str__(self):
        return str.format("{} {}", self.position, self.dimension)


class PermissionLevel:
    id = None

    def __init__(self, id):
        self.id = id

    def __str__(self):
        if self.id == 0:
            permName = mci18n.t("mcobject.permissionLevel.notOperator")
        elif self.id == 1:
            permName = mci18n.t("mcobject.permissionLevel.operator")
        else:
            permName = mci18n.t("mcobject.permissionLevel.unknown")
        return permName


class Health:
    """
    A valid health object should have its max health greater than or equal to current health, and both are >= 0. 
    """
    _current = None
    _max = None

    def __init__(self, health, maxHealth):
        if maxHealth >= 0 and health <= maxHealth and health >= 0:
            self._current, self._max = health, maxHealth
        else:
            raise ValueError(
                f"invalid health({health}) or maxHealth({maxHealth})")

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        if value >= self._max:
            value = self._max
        elif value < 0:
            value = 0
        self._current = value

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        if value < 0:
            raise ValueError(f"invalid maximum of health({value})")
        elif self._current > value:
            self._current = value
        self._max = value


class PointerObject:
    pointer = None

    def __init__(self, pointer):
        self.pointer = pointer

    def update(self, obj=None):
        if obj:
            raise NotImplementedError(
                f"{obj}.update() on a {type(self)} object is not implemented.")

    def __int__(self):
        return self.pointer


class Actor(PointerObject):
    _actorDataDict = None

    def __init__(self, pointer):
        super(__class__, self).__init__(pointer)

    def update(self, obj=None):
        if not obj:
            super(__class__, self).update()
        elif __class__ == obj:
            self._actorUpdate()
        else:
            super(__class__, self).update(obj=obj)

    def _actorUpdate(self):
        self._actorDataDict = getActorInfo(self.pointer)

    def _getActorInfo(self, key, update=True):
        if update or self._actorDataDict == None:
            self.update(obj=__class__)
        return self._actorDataDict[key]

    def getActorName(self, update=True):
        return self._getActorInfo("entityname", update=update)

    def getActorPosition(self, update=True):
        return Position(self._getActorInfo("XYZ", update=update))

    def getActorDimension(self, update=True):
        return Dimension(self._getActorInfo("dimensionid", update=update))

    def getPlayerLocation(self, update=True):
        return Location(self.getActorPosition(update=update), self.getActorDimension(update=update))

    def getActorIsStanding(self, update=True):
        return bool(self._getActorInfo("isstand", update=update))

    def getActorHealth(self, update=True):
        return Health(self._getActorInfo("health", update=update), self._getActorInfo("maxhealth", update=update))

    @property
    def name(self): return self.getActorName()
    @property
    def name_noupdate(self): return self.getActorName(update=False)
    @property
    def position(self): return self.getActorPosition()
    @property
    def position_noupdate(self): return self.getActorPosition(update=False)
    @property
    def dimension(self): return self.getActorDimension()
    @property
    def dimension_noupdate(self): return self.getActorDimension(update=False)
    @property
    def location(self): return self.getActorLocation()
    @property
    def location_noupdate(self): return self.getActorLocation(update=False)
    @property
    def isStanding(self): return self.getActorIsStanding()
    @property
    def isStanding_noupdate(self): return self.getActorIsStanding(update=False)
    @property
    def health(self): return self.getActorHealth()
    @property
    def health_noupdate(self): return self.getActorHealth(update=False)


class Player(Actor):
    _playerDataDict = None

    def __init__(self, pointer):
        super(__class__, self).__init__(pointer)

    def update(self, obj=None):
        if not obj:
            super(__class__, self).update()
        elif __class__ == obj:
            self._playerUpdate()
        else:
            super(__class__, self).update(obj=obj)

    def _playerUpdate(self):
        self._playerDataDict = getPlayerInfo(self.pointer)

    def _getPlayerInfo(self, key, update=True):
        if update or self._playerDataDict == None:
            self.update(obj=__class__)
        return self._playerDataDict[key]

    def getPlayerName(self, update=True):
        return self._getPlayerInfo("playername", update=update)

    def getPlayerXuid(self, update=True):
        return self._getPlayerInfo("xuid", update=update)

    def getPlayerPosition(self, update=True):
        return Position(self._getPlayerInfo("XYZ", update=update))

    def getPlayerDimension(self, update=True):
        return Dimension(self._getPlayerInfo("dimensionid", update=update))

    def getPlayerLocation(self, update=True):
        return Location(self.getPlayerPosition(update=update), self.getPlayerDimension(update=update))

    def getPlayerIsStanding(self, update=True):
        return bool(self._getPlayerInfo("isstand", update=update))

    def getPlayerHealth(self, update=True):
        return Health(self._getPlayerInfo("health", update=update), self._getPlayerInfo("maxhealth", update=update))

    def getPlayerPermissionLevel(self):
        return PermissionLevel(getPlayerPerm(self.pointer))

    def setPlayerPermissionLevel(self, value):
        assert(isinstance(value, PermissionLevel))
        setPlayerPerm(self.pointer, value.id)

    @property
    def name(self): return self.getPlayerName()
    @property
    def name_noupdate(self): return self.getPlayerName(update=False)
    @property
    def xuid(self): return self.getPlayerXuid()
    @property
    def xuid_noupdate(self): return self.getPlayerXuid(update=False)
    @property
    def position(self): return self.getPlayerPosition()
    @property
    def position_noupdate(self): return self.getPlayerPosition(update=False)
    @property
    def dimension(self): return self.getPlayerDimension()
    @property
    def dimension_noupdate(self): return self.getPlayerDimension(update=False)
    @property
    def isStanding(self): return self.getPlayerIsStanding()
    @property
    def isStanding_noupdate(
        self): return self.getPlayerIsStanding(update=False)

    @property
    def location(self): return self.getPlayerLocation()
    @property
    def location_noupdate(self): return self.getPlayerLocation(update=False)
    @property
    def health(self): return self.getPlayerHealth()
    @property
    def health_noupdate(self): return self.getPlayerHealth(update=False)
    @property
    def permissionLevel(self): return self.getPlayerPermissionLevel()
    @permissionLevel.setter
    def permissionLevel(
        self, value): return self.setPlayerPermissionLevel(value)

    def addLevels(self, explevels):
        return addLevel(self.pointer, explevels)

    def teleport(self, location):
        assert(isinstance(location, Location))
        return teleport(self.pointer, location.position.x, location.position.y, location.position.z,
                        location.dimension.id)

    def runCommand(self, command):
        return runcmdAs(self.pointer, command)

    def talk(self, msg):
        return talkAs(self.pointer, msg)


