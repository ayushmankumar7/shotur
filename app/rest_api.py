from flask import Flask , request, jsonify
from flask_restful import Resource, Api , reqparse
import google.cloud
import firebase_admin
import datetime
from firebase_admin import firestore
from firebase_admin import credentials

if (not len(firebase_admin._apps)):

    cred = credentials.Certificate("shotur-794d7-firebase-adminsdk-99171-09fcd0675c.json")

    default_app = firebase_admin.initialize_app(cred, { 'projectID': 'shotur-794d7'})

app = Flask(__name__)
api = Api(app)



class Items(Resource):
    def get(self, id):
        db = firestore.client()

        ref = db.collection(u'urls')

        try:
            docs = ref.get()
            dict = {}
            for doc in docs:
                dict_doc = doc.to_dict()
                print(dict_doc["my_urls"][id])
                    
            return dict_doc["my_urls"][id]
        except google.cloud.exceptions.NotFound:
            print(u"Missing data")

        
        

    def post(self, id):
        parser = reqparse.RequestParser()

        db = firestore.client()

        ref = db.collection(u'urls').document(u'all')

        
        parser.add_argument(id)


        args  = parser.parse_args()
        print(args)
        
        ref.set({f"my_urls":args}, merge = True)
  
        return args, 201



api.add_resource(Items, '/<id>')
