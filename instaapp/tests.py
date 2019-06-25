from django.test import TestCase
from .models import Comment,Post,Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class CommentTestClass(TestCase):
    # set up method to test for comments and instatiating the image object

    def setUp(self):
        self.test_comments = Comment(comment= 'The good life',user= 'shaw',image='jpg')
        self.test_comments.save()

    # Testing instance 
     
    def test_instance(self):
        self.assertTrue(isinstance(self.test_comments, Comment))
    
    # Testing the saving method 

    def test_save_method(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)
    #Tear down method    

    def tearDown(self):
        Comment.objects.all().delete()
    
     # Testing delete method 
    def test_delete_comments(self):
        self.test_comments.delete()
        self.assertAlmostEqual(len(Comments.objects.all()), 0)


class ProfileTestClass(TestCase):
    # set up method to test instantiation is correct

    def setUp(self):
        self.test_profile = Profile(bio='Master willen',profile_photo='imagejpg')
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
    
class PostTestClass(TestCase):

    # Test instance to test that objects are instantiated correctly
    def setUp(self):
        self.test_comments = Comment.objects.create(comment='Bless up',image_id='1',user_id='1')
        self.test_profile = Profile.objects.create(bio='Bad man shivo',profile_photo='imagejpg')
        self.test_image = Post(image='imagejpg',image_name='awesome',image_caption='Good image',profile=self.test_profile,comments=self.test_comments)
        self.test_image.save()
    
    # Testing the save method
    def test_save_method(self):
        image = Image.objects.all()
        self.assertTrue(len(image)>0)
    # Tear down method 
    def tearDown(self):
         Image.objects.all().delete()
    
  


    

    