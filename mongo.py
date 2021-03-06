from flask import Flask, render_template, request, redirect, url_for
import os
from flask_uploads import UploadSet, IMAGES, configure_uploads
import pymongo
import re
from bson.objectid import ObjectId

app = Flask(__name__)

TOP_LEVEL_DIR = os.path.abspath(os.curdir)
upload_dir = '/static/uploads/img/'
app.config["UPLOADS_DEFAULT_DEST"] = TOP_LEVEL_DIR + upload_dir
app.config["UPLOADED_IMAGES_DEST"] = TOP_LEVEL_DIR + upload_dir
app.config["UPLOADED_IMAGES_URL"] = upload_dir

images_upload_set = UploadSet('images', IMAGES)
configure_uploads(app, images_upload_set)

MONGO_URI = os.getenv('MONGO_URI')
KEY = os.getenv('KEY')
DATABASE_NAME = 'fieldTripDB'
COLLECTION_NAME = 'fieldTripLocations'
conn = pymongo.MongoClient(MONGO_URI)
coll = conn[DATABASE_NAME][COLLECTION_NAME]

themes = ["Animals", "Cultural", "Discovery", "Nature", "Occupation", "Singapore", "The World", "Transportation", "Others"]
age = ["N1", "N2", "K1","K2"]
prices = ["Free", "Paid", "Both"]


# landing page
@app.route('/')
def landingPage():
    cursor = coll.find({});
    return render_template('landing_page.template.html', results=cursor)
    
# view all 
@app.route('/all')
def index():
    cursor = coll.find({}).sort([("name", pymongo.ASCENDING)]);
    return render_template('index.template.html', results=cursor)

# add entry
@app.route('/add')
def addForm():
    return render_template('add_new.template.html', themes=themes, age=age, prices=prices)

@app.route('/add', methods=['POST'])
def add():
    
    image = request.files.get('image')
    filename = images_upload_set.save(image)
    name = request.form.get('name')
    address = request.form['address']
    email = request.form['contact']
    description = request.form['description']
    activities = request.form.get('activities')
    activitiesArr = [x.strip() for x in activities.split("\n")]
    theme = request.form.getlist('theme')
    age_group = request.form.getlist('age-group')
    price = request.form.get('price')
    
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
    
    return render_template('add_success.template.html', themes=themes, age=age, prices=prices, image=image, filename=filename, name=name, address=address, email=email, description=description, activities=activities, theme=theme, age_group=age_group, price=price)

# search entry
@app.route('/search')
def searchForm():
    
    search_name = request.args.get('search-by')
    search_age = request.args.getlist('search-age')
    search_theme = request.args.getlist('search-theme')
    search_price = request.args.get('search-price')

    search_criteria = {}
    if search_name is not "":
        search_criteria["name"] = re.compile(r'{}'.format(search_name), re.I)
        
    if len(search_age) > 0:
        search_criteria['age_group'] = {
            '$in' : search_age
        }
        
    if len(search_theme) > 0:
        search_criteria['themes'] = {
            '$all' : search_theme
        }
        
    if  search_price != "Both":
        search_criteria['price'] = search_price 
    
    projection = {
        'name', 'price', 'themes', 'age_group', 'image'
    }
    
    cursor = coll.find(search_criteria, projection).sort([("name", pymongo.ASCENDING)])
    return render_template("search.template.html", results=cursor, age=age, themes=themes,
        prices=prices, search_name=search_name, search_age=search_age,
        search_theme=search_theme, search_price=search_price)

# view an entry 
@app.route('/view/<location_id>')
def viewInfoPage(location_id):
    result = coll.find_one({
        '_id':ObjectId(location_id)
    })
    
    return render_template('view.template.html', result=result)

# edit entry
# edit contact
@app.route('/edit-location/<location_id>')
def editAddressForm(location_id):
    result = coll.find_one({
        '_id':ObjectId(location_id)
    })
    
    return render_template("edit_address.template.html", result=result, themes=themes)
    
@app.route('/edit-location/<location_id>', methods=['POST'])
def editAddress(location_id):

    name = request.form['edit-name']
    address = request.form.get('edit-address')
    email = request.form.get('edit-email')
    
    coll.update(
       { "_id": ObjectId(location_id) },
       {
         '$set': { "name": name, "address":address, "email":email},
       }
    )
    
    result = coll.find_one({
        '_id':ObjectId(location_id)
    })
    
    return render_template("view_after_edit.template.html", result=result)

# edit information
@app.route('/edit/<location_id>')
def editDetailsForm(location_id):
    result = coll.find_one({
        '_id':ObjectId(location_id)
    })
    
    
    return render_template("edit_details.template.html", result=result, themes=themes, age=age, prices=prices)
 
# after edit page  
@app.route('/edit/<location_id>', methods=['POST'])
def editDetails(location_id):
    
    description = request.form['edit-description']
    activities = request.form.get('edit-activities')
    activitiesArr = [x.strip() for x in activities.split('\n')]
    theme = request.form.getlist('edit-theme')
    age_group = request.form.getlist('edit-age-group')
    price = request.form.get('edit-price')
    
    coll.update(
       { "_id": ObjectId(location_id) },
       {
         '$set': { "description": description, "activities":activitiesArr, "themes":theme, "age_group": age_group, "price": price},
       }
    )
    
    result = coll.find_one({
        '_id':ObjectId(location_id)
    })
    
    return render_template("view_after_edit.template.html", result=result)

# deleting an entry
@app.route('/view/<location_id>', methods=['POST'])
def deleteInfo(location_id):
    
    key = request.form['delete-key']
    
    keyArr = [x.strip() for x in KEY.split(",")]
    
    for k in keyArr:
        if  k == key:
            coll.remove(
                { "_id": ObjectId(location_id) }
            )
            return redirect('/deleted')
    return redirect('/delete-invalid')

# unsuccessful delete
@app.route('/delete-invalid')
def cannotDelete():
    cursor = coll.find({}).sort([("name", pymongo.ASCENDING)]);
    return render_template('delete_invalid.template.html', results=cursor)

# successful delete 
@app.route('/deleted')
def succeed():
    cursor = coll.find({}).sort([("name", pymongo.ASCENDING)]);
    return render_template('delete_succeed.template.html', results=cursor)


if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
	port=int(os.environ.get('PORT')),
	debug=True)
