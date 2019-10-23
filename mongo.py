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

@app.route('/test')
def indexTest():
    cursor = coll.find({});
    return render_template('index.template.html', results=cursor)
    
@app.route('/')
def landingPage():
    return render_template('landing_page.template.html')

@app.route('/add')
def addForm():
    themes = ["Occupation", "Nature", "Conservation", "Museums", "Others"]
    age = ["N1", "N2", "K1","K2", "All"]
    prices = ["Free", "Paid"]
    
    return render_template('add_new.template.html', themes=themes, age=age, prices=prices)

@app.route('/add', methods=['POST'])
def add():
    image = request.files.get('image') #1 -- get the uploaded image
    filename = images_upload_set.save(image)
    name = request.form.get('name')
    address = request.form['address']
    email = request.form['contact']
    description = request.form['description']
    activities = request.form.get('activities')
    activitiesArr = [x.strip() for x in activities.split(',')]
    theme = request.form.getlist('theme')
    age_group = request.form.getlist('age-group')
    price = request.form.get('price')
    
    themes = ["Occupation", "Nature", "Conservation", "Museums", "Others"]
    age = ["N1", "N2", "K1","K2", "All"]
    prices = ["Free", "Paid"]
    
    coll.insert({
        "name" : name,
        "address" : address,
        "email": email,
        "description": description,
        "activities": activitiesArr,
        "themes": theme,
        "age_group": age_group,
        "price": price,
        "image": {
                'image_url' : images_upload_set.url(filename)
            }
    })
    
    return render_template('add_new.template.html', themes=themes, age=age, prices=prices, image=image, filename=filename, name=name, address=address, email=email, description=description, activities=activities, theme=theme, age_group=age_group, price=price)


if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
	port=int(os.environ.get('PORT')),
	debug=True)
