from mc import *

inRunner = None
try:
    from mchat import *
except ImportError:
    inRunner = True
if inRunner: exec("from py.mchat import *")


@mcutils.listen("玩家加入")
def nicknameCon(player_p):
    #print(getActorInfo(player_p))
    Player = mcobject.Player(player_p)
    assert(not Player._playerDataDict)
    assert(not Player._actorDataDict)
    print(Player.getActorName())
    assert(Player._actorDataDict)
    assert(not Player._playerDataDict)
    print(Player.permissionLevel)
    print(Player.location)
    print(Player.getActorName())

@mcutils.listen("放置方块")
def nicknameConfigure(blockname,blockid,player,position):
    print(player)
    Player = mcobject.Player(player)
    print(Player.permissionLevel)
    print(Player.location)
    print(getPlayerItems(int(Player)))
    print(getPlayerHand(int(Player)))
    #print(getPlayerItems(player))
    
    


