from flask import Flask, render_template, request, redirect, url_for
import os
from flask_uploads import UploadSet, IMAGES, configure_uploads
import pymongo

app = Flask(__name__)

TOP_LEVEL_DIR = os.path.abspath(os.curdir) #1
upload_dir = '/static/uploads/img/' #2
app.config["UPLOADS_DEFAULT_DEST"] = TOP_LEVEL_DIR + upload_dir #3
app.config["UPLOADED_IMAGES_DEST"] = TOP_LEVEL_DIR + upload_dir #4
app.config["UPLOADED_IMAGES_URL"] = upload_dir #5

images_upload_set = UploadSet('images', IMAGES)
configure_uploads(app, images_upload_set)

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'fieldTripDB'
COLLECTION_NAME = 'fieldTripLocations'
conn = pymongo.MongoClient(MONGO_URI)
coll = conn[DATABASE_NAME][COLLECTION_NAME]

@app.route('/')
def indexTest():
    cursor = coll.find({});
    return render_template('index.template.html', results=cursor)

if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
	port=int(os.environ.get('PORT')),
	debug=True)
