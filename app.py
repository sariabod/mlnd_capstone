from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from fastai.structured import *
from fastai.column_data import *
import pickle
import numpy as np



app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('user')
parser.add_argument('course')
parser.add_argument('category')
parser.add_argument('job')
parser.add_argument('institution')
parser.add_argument('state')

#need to load up the model and lookup table
lookup_table = None
model = None

def lookup(cat,val):
    return lookup_table[cat][val]    


def my_load_model():

    cat_vars = ['user','course','category','job','institution','state']

    with open ('models/data/final_df', 'rb') as fp:
        df = pickle.load(fp)

    with open ('models/data/ratings', 'rb') as fp:
        y = pickle.load(fp)

    with open ('models/data/val_idx', 'rb') as fp:
        val_idx = pickle.load(fp)

    with open ('models/data/emb_sizes', 'rb') as fp:
        emb_szs = pickle.load(fp)

    md = ColumnarModelData.from_data_frame("models/", val_idx, df, y.astype(np.float32), cat_flds=cat_vars, bs=128)
    m = md.get_learner(emb_szs,0 ,0.4, 1, [200,100], [0.5,0.01],y_range=(0,5))
    m.load('mdl')
    return m.model


def build_lookup_table():
    with open ('models/data/lookup_table', 'rb') as fp:
        lookup_table = pickle.load(fp)

    return lookup_table

class Predict(Resource):
    def get(self):
        return {'status': 'hey, it works!'}

    def post(self):
        args = parser.parse_args()

        user = lookup('user',args.user) 
        course = lookup('course',args.course) 
        category = lookup('category',args.category) 
        job = lookup('job',args.job) 
        institution = lookup('institution',args.institution) 
        state = lookup('state',args.state) 

        cat = V(np.array([user,course,category,job,institution,state],ndmin=2))
        prediction = to_np(model(cat,[])).tolist()
	        
        return {'rating':prediction[0][0]}

api.add_resource(Predict, '/')

if __name__ == '__main__':
    model = my_load_model() 
    model.eval()
    lookup_table = build_lookup_table()
    app.run(debug=True)
