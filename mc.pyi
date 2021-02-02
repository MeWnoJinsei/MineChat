from typing import Literal
adapted_version = [0, 1, 7]


def logout(cmdout: str) -> bool: ...


def runcmd(cmd: str) -> bool: ...


def setTimer(func: function, delay: int) -> bool: ...


def removeTimer(func: function) -> Literal[True]: ...


def setListener(key: str, func: function) -> bool: ...


def setShareData(index: str, data: any) -> bool: ...


def getShareData(index: str) -> any: ...


def setCommandDescription(cmd: str, description: str) -> bool: ...


def getPlayerList() -> list: ...


def sendCustomForm(player_ptr: int, json: str) -> int: ...


def sendModalForm(player_ptr: int, title: str, content: str,
                  button1: str, button2: str) -> int:
    """clicking on button1 sets "selected" True and vice versa."""


def sendSimpleForm(player_ptr: int, title: str,
                   content: str, buttons: str) -> int: ...


def transferServer(player_ptr: int, server_address: str,
                   port: int) -> bool:
    """return if it is successful."""


def getActorInfo(player_ptr: int) -> dict: ...


def getPlayerInfo(player_ptr: int) -> dict: ...


def getPlayerPerm(player_ptr: int) -> int: ...


def setPlayerPerm(player_ptr: int, perm: int) -> bool: ...


def addLevel(player_ptr: int, lv: int) -> bool: ...


def setName(player_ptr: int, newName: str) -> bool: ...


def getPlayerScore(player_ptr: int, objectiveName: str) -> int: ...


def modifyPlayerScore(player_ptr: int, objectiveName: str, score: int, mode: int) -> bool:
    """
    mode 0: set
    mode 1: add
    mode 2: remove
    """


def talkAs(player_ptr: int, msg: str) -> bool: ...


def runcmdAs(player_ptr: int, cmd: str) -> bool: ...


def teleport(player_ptr: int, x: int, y: int,
             z: int, dimensionId: int) -> bool: ...


def tellraw(player_ptr: int, msg: str) -> bool: ...


def setBossBar(player_ptr: int, title: str, percentage: float) -> bool: ...


def removeBossBar(player_ptr: int) -> bool: ...


def getScoreBoardId(player_ptr: int) -> int: ...


def createScoreBoardId(player_ptr: int) -> bool: ...


def setDamage(damage: int) -> bool:
    """modify the damage value when an actor get hurt."""


def setServerMotd(motd: str) -> bool: ...


def addItemEx(player_ptr: int, items: str) -> bool: ...


def getPlayerItems(player_ptr: int) -> str: ...  # does not work so far


def getPlayerHand(player_ptr: int) -> str: ...


def getPlayerItem(player_ptr: int, slotid: int) -> str: ...


def setPlayerItems(player_ptr: int, items: str) -> bool: ...


# def getPlayerEnderChests(player_ptr: int) -> str: ... # does not exist


def setPlayerEnderChests(player_ptr: int, items: str) -> bool: ...


def setSidebar(player_ptr: int, title: str, data: str) -> bool: ...


def removeSidebar(player_ptr: int) -> None: ...
