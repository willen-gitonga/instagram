from django.test import TestCase
from .models import Comments,Image,Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class CommentsTestClass(TestCase):
    # set up method to test for comments and instatiating the image object

    def setUp(self):
        self.test_comments = Comments(comment_name= 'The good life')
        self.test_comments.save()

    # Testing instance 
     
    def test_instance(self):
        self.assertTrue(isinstance(self.test_comments, Comments))
    
    # Testing the saving method 

    def test_save_method(self):
        comments = Comments.objects.all()
        self.assertTrue(len(comments)>0)
    #Tear down method    

    def tearDown(self):
        Comments.objects.all().delete()
    
     # Testing delete method 
    def test_delete_comments(self):
        self.test_comments.delete()
        self.assertAlmostEqual(len(Comments.objects.all()), 0)


class ProfileTestClass(TestCase):
    # set up method to test instantiation is correct

    def setUp(self):
        self.test_profile = Profile(bio='Master willen',profile_photo='imagejpg', profile_name='willen')
        self.test_profile.save()
    
    # Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.test_profile, Profile))
    
    # Testing the save method
    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
    
    # Tear dowm method 
    def tearDown(self):
        Profile.objects.all().delete()
    
    # Testing delete method 
    def test_delete_profile(self):
        self.test_profile.delete()
        self.assertEqual(len(Profile.objects.all()), 0) 
    
class ImageTestClass(TestCase):

    # Test instance to test that objects are instantiated correctly
    def setUp(self):
        self.test_comments = Comments.objects.create(comment_name='Bless up')
        self.test_profile = Profile.objects.create(bio='Bad man shivo',profile_photo='imagejpg')
        self.test_image = Image(image='imagejpg',image_name='awesome',image_caption='Good image',profile=self.test_profile,comments=self.test_comments)
        self.test_image.save()
    
    # Testing the save method
    def test_save_method(self):
        image = Image.objects.all()
        self.assertTrue(len(image)>0)
    # Tear down method 
    def tearDown(self):
         Image.objects.all().delete()
    
  


    

    