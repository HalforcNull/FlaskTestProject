import mysql.connector
import dataEntities.DataAccess
from FlaskTestProject.dataEntities import Script
import json

#TODO: CONFIG 
hostname = 'localhost'
username = 'root'
password = 'root'
database = 'dbo'

class ScriptManager:

    def __init__(self):
        self.DataAccess = dataEntities.DataAccess.DataAccess()
        return

    def getScriptIDbyName(self, scriptName):
        #TODO
        #Do we need it????
        return 1

    def getScriptList(self):
        return self.DataAccess.GetSctriptList()

    def getInputFileRequirementListbyId(self, scriptId):
        return 1
    def getInputParmRequirementLIstbyId(self, scriptId):
        return 1
    def getInputFileDescription(self, scriptId, fileId):
        return 1
    def getInputParmDescription(self, scriptId, parmId):
        return 1


