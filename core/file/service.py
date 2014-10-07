from PIL import Image as pil_image
from mongoengine.python_support import StringIO
from file.models import Image, Rating
from file.repo import ImageRepo, RatingRepo

class Service():
    imageRepo  = ImageRepo()
    ratingRepo = RatingRepo()

    def handle_upload_img(self,post,files):
        size = (128,128)
        image = pil_image.open(files['img'])
        format = image.format
        width, height = image.size
        io = StringIO()
        image.save(io, format)
        io.seek(0)
        self.imageRepo.save(width, height, post['fileName'], format, io)
        

    def handle_submit_rating(self,post, imgId):
        image = self.imageRepo.getImageById(imgId)
        rating = self.ratingRepo.save(post['username'], image, post['rating'], post['description'])
        print rating
        self.imageRepo.updateRating(rating, imgId)

    def get_img_byID(self, imgId):
        return self.imageRepo.getImageById(imgId)

    def get_img_content_byID(self, imgId):
        image = self.imageRepo.getImageById(imgId)
        content = image.content
        return content

    def get_img_list(self):
        return self.imageRepo.getImageList()