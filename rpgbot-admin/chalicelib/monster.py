from chalice import Blueprint
import json
import os

monsterRoutes = Blueprint(__name__)

#instantiate Fauna DB
client = FaunaClient(secret= os.environ.get('faunaMonster'))

#Create Monster
@monsterRoutes.route('/', methods=['POST'])
def create():
  req = json.loads(monsterRoutes.current_request.raw_body)

  rowCount = client.query(
    q.count(q.documents(q.collection("Monsters")))
  )
  # newIndex = rowCount + 1

  # newMonster = {
  #   "id"      :newIndex,
  #   "name"    :req['name'],
  #   "type"    :req['type'],
  #   "HP"      :req['HP'],
  #   "ATK"     :req['ATK'],
  #   "DEF"     :req['DEF'],
  #   "SPD"     :req['SPD'],
  #   "SPEC"    :req['SPEC'],
  #   "Wealth"  :req['Wealth'],
  #   "XP"      :req['XP'],
  #   "lvlMult" :req['lvlMult']
  # }

  # response = client.query(
#   q.Create(
  #     q.collection("Monsters"),
  #     {"data": newMonster}
  #   )
  # )

  return rowCount

#Get All
@monsterRoutes.route('/')
def getAll():
  res = 4
  data = res['Items']
  return data

#Get one
@monsterRoutes.route('/{id}')
def getOne(id):
  res = 4
  return res['Item']

#Update
@monsterRoutes.route('/{id}', methods=['PUT'])
def update(id, request):
  return {'updated':id}

#Delete
@monsterRoutes.route('/{id}', methods=['DELETE'])
def delete(id):
  return {'deleted': id}