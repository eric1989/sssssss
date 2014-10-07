import datetime
from mongoengine import *
from config.settings import DBNAME

connect(DBNAME)

class File(Document):
	content = FileField()
	title   = StringField(max_length=120)

	meta    = {'allow_inheritance': True}

class Image(File):
	img_width  = IntField(min_value=1, required=True)
	img_height = IntField(min_value=1, required=True)
	total_rating = FloatField() 
	ratings = ListField(ReferenceField('Rating')) #Since the user will not have the fuction to delete the rating there is no need to delete (or use reverse delete here)
	

class Rating(Document):
	username = StringField(max_length=120) #just a user inputed field
	image_id = ReferenceField(Image) #id from the image
	rating = StringField(max_length=120) #user can input 1, 2, 3, 4 or 5 
	description = StringField(max_length=5000) 
	#add something here for video

# Create your models here.
