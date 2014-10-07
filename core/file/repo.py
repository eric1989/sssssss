from file.models import Image, Rating

class ImageRepo():

	def getImageById(self,imageID):
		return Image.objects.get(id=imageID)

	def getImageList(self):
		return Image.objects.all()

	def getListRating(self,rating):
		return Image.objects.get(rating)

	def updateRating(self,rating,imageID):
		image = Image.objects(id=imageID)
		image.update_one(push__ratings=rating, inc__total_rating=int(rating.rating))

	def save(self,img_width, img_height, title, fileType, fileStream):
		instance = Image(img_width= img_width,img_height=img_height,title=title)
		instance.content.put(fileStream, content_type=fileType)
		instance.save()
		return instance

class RatingRepo():
	
	def getRatingByImageID(self,image):
		return Rating.objects.get(image_id=image)

	def save(self,username,image,rate,desc):
		rating = Rating(username = username)
		rating.image_id = image
		rating.rating   = rate
		rating.description = desc
		rating.save()
		return rating