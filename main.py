from flask import Flask, jsonify, request
import json
app = Flask (__name__)
# A API TERÁ UMA LISTA DE TAREFAS QUE DEVERÁ TER OS SEGUINTES CAMPOS: ID, RESPONSÁVEL, TAREFA E STATUS
tarefas = [
    {   'id':0,
        'responsável': 'Samuel',
        'tarefa': 'Desenvolver metodo GET',
        'status': 'pendente'    },
    {   'id':1,
        'responsavel': 'Rodrigues',
        'tarefa': 'Desenvolver PUT',
        'status': 'finalizado'  },
    {   'id':2,
        'responsavel': 'Tavares',
        'tarefa': 'Desenvolver DELETE',
        'status': 'finalizado'  },
    {   'id':3,
        'responsavel': 'Alves',
        'tarefa': 'Desenvolver POST',
        'status': 'pendente'}
]

@app.route('/<int:id>/', methods={'GET', 'PUT', 'DELETE'})

def tarefa(id):     #A API DEVERÁ PERMITIR CONSULTAR UMA TAREFA ATRAVÉS DO ID
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem ='Tarefa de ID {} inexistente'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure responsavel pela API'
            responsa = {'status':'fatal erro', 'mensagem':mensagem}
        return (response) # Implemente uma mensagem que foi retornado com sucesso!
    elif request.method == 'PUT': #aqui ele modifica qualquer valor / implementar somente o status
        modifica_status = json.loads(request.data) #json.loads (para modificar)
        tarefas[id] = modifica_status
        return jsonify(modifica_status)
    elif request.method == 'DELETE':    #TAMBÉM EXCLUIR UMA TAREFA.
        tarefas.pop(id) #nome da lista.pop para deletar
        return jsonify({'mensagem':'O ID {} foi deletado com sucesso'.format(id)})

@app.route('/tarefas/', methods=['POST', 'GET'])
def lista_tarefas():
    if request.method =='POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro inserido com ID {}'.format(posicao)})
        # Lista todos os devs
    elif request.method == 'GET':
        return jsonify(tarefas)  # Necessário return para trazer json.

if __name__ == '__main__':
    app.run(debug=True)
