from atp import api_manager
from atp.models import Player, Game, GameDate, GameDateUserCan

api_manager.create_api(Player, methods=['GET', 'POST'],
                       collection_name='players')
api_manager.create_api(Game, methods=['GET', 'POST', 'PUT'],
                       collection_name='games')
api_manager.create_api(GameDate, methods=['GET', 'POST', 'DELETE'])
api_manager.create_api(GameDateUserCan, methods=['GET', 'POST', 'PUT'])
