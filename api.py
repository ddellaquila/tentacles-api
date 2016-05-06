from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TENTACLES = {
    '1': {'name': u"Purple Tentacle",
          'description': u"A mutant monster and lab assistant created by mad scientist Dr. Fred Edison."},
    '2': {'name': u"Green Tentacle",
          'description': u"Harmless and friendly brother of Purple Tentacle."},
    '3': {'name': u"Bernard Bernoulli",
          'description': u"Green Tentacle's friend, he's a nerd with glasses."},
}


def abort_if_doesnt_exist(_id):
    if _id not in TENTACLES:
        abort(404, message="Tentacle {} doesn't exist".format(_id))


@app.route('/')
def api_index():
    return "Welcome to the Tentacles API.\n"

class Tentacle(Resource):
    """ Show a tentacle and lets you edit/delete it.
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(Tentacle, self).__init__()

    def get(self, _id):
        abort_if_doesnt_exist(_id)
        return TENTACLES[_id]

    def delete(self, _id):
        abort_if_doesnt_exist(_id)
        del TENTACLES[_id]
        return '', 204

    def put(self, _id):
        args = self.reqparse.parse_args()
        print("args: %s" % str(args))
        name = {'name': args['name'],'description':args['description']}
        TENTACLES[_id] = name
        return TENTACLES[_id], 201


class TentacleList(Resource):
    """ Shows a list of all tentacles, and lets you add new tentacle.
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TentacleList, self).__init__()

    def get(self):
        return TENTACLES

    def post(self):
        args = self.reqparse.parse_args()
        print("args: %s" % str(args))
        _id = '%d' % (len(TENTACLES) + 1)
        TENTACLES[_id] = {'name': args['name'],
                          'description': args['description']}
        return TENTACLES[_id], 201


api.add_resource(TentacleList, '/tentacles')
api.add_resource(Tentacle, '/tentacles/<string:_id>')

if __name__ == '__main__':
	app.run(host="127.0.0.1",
                port=int("5000"),
                debug=True)
