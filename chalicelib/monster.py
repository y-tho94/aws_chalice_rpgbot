from chalice import Blueprint
import json
from airtable import Airtable
import os

monsterRoutes = Blueprint(__name__)

#instantiate airtable (info from airtable.com/api)
baseKey = os.environ['MONSTERS_BASE_KEY']
secret = os.environ['AIRTABLE_API_KEY']
tbl = Airtable(baseKey, "Monsters", secret)

#Create Monster
@monsterRoutes.route('/', methods=['POST'])
def create():
  try:
    req = json.loads(monsterRoutes.current_request.raw_body)

    newMonster = {
      "Name"          :req['name'],
      "Image"         :req['img'],
      "Type"          :req['type'],
      "BaseHP"        :req['HP'],
      "BaseATK"       :req['ATK'],
      "BaseDEF"       :req['DEF'],
      "BaseSPD"       :req['SPD'],
      "BaseSPEC"      :req['SPEC'],
      "BaseWealth"    :req['Wealth'],
      "BaseXP"        :req['XP'],
      "lvlMultiplier" :req['lvlMult']
    }

    response = tbl.insert(newMonster, True) 

  except Exception as ex:
    response = {
      "data":{
        "status" : 500,
        "message" : ex
      }
    }
  finally:
    return response

#Get All
@monsterRoutes.route('/')
def getAll():
  try:
    response = tbl.get_all() 

  except Exception as ex:
    response = {
      "data":{
        "status" : 500,
        "message" : ex
      }
    }
  finally:
    return response

#Get one
@monsterRoutes.route('/{id}')
def getOne(id):
  try:
    response = tbl.get(id) 

  except Exception as ex:
    response = {
      "data":{
        "status" : 500,
        "message" : ex
      }
    }
  finally:
    return response

#Update
@monsterRoutes.route('/{id}', methods=['PUT'])
def update(id, request):
  try:
    req = json.loads(monsterRoutes.current_request.raw_body)

    monster = {
      "Name"          :req['name'],
      "Image"         :req['img'],
      "Type"          :req['type'],
      "BaseHP"        :req['HP'],
      "BaseATK"       :req['ATK'],
      "BaseDEF"       :req['DEF'],
      "BaseSPD"       :req['SPD'],
      "BaseSPEC"      :req['SPEC'],
      "BaseWealth"    :req['Wealth'],
      "BaseXP"        :req['XP'],
      "lvlMultiplier" :req['lvlMult']
    }

    response = tbl.update(id, monster, True) 

  except Exception as ex:
    response = {
      "data":{
        "status" : 500,
        "message" : ex
      }
    }
  finally:
    return response


#Delete
@monsterRoutes.route('/{id}', methods=['DELETE'])
def delete(id):
  try:
    response = tbl.delete(id) 

  except Exception as ex:
    response = {
      "data":{
        "status" : 500,
        "message" : ex
      }
    }
  finally:
    return response
