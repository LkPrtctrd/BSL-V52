from Heart.Commands.LogicCommand import LogicCommand
from Heart.Messaging import Messaging
from DB.DatabaseHandler import DatabaseHandler

class SetPlayerNameColorCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["NameColor"] = calling_instance.readDataReference()[1]
        
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db = DatabaseHandler()
        pl = db.getPlayer(calling_instance.player.ID)
        pl["Namecolor"]=fields["NameColor"]
        db.updatePlayerData(pl,calling_instance)

    def getCommandType(self):
        return 527