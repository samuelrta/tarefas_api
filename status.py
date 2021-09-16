from flask_restful import Resource, request
import json

lista_status = ['pendente', 'finalizado']

# Chama status baseado no id
class StatusAltera(Resource):
    def get(self, id):
        return lista_status[id]


# Altera nome do status baseado no id
    def put(self,  id):
        status_altera = json.loads(request.data)
        lista_status[id] = status_altera
        return status_altera

# Deleta status baseado no id
    def delete(self, id):
        lista_status.pop(id)
        return {'mensagem': 'O status de ID {} foi deletado com sucesso'.format(id)}

    # Chama todos os status
class ListaStatus(Resource):
    def get(self):
        return lista_status

    # Adiciona um status novo, com id criado.
    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_status)
        dados['id'] = posicao
        lista_status.append(dados)
        return lista_status[posicao]