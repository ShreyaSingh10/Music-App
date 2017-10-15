from django.db import models

# Create your models here.

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=3000)

	def __str__(self):#string representation of Album Object
		return self.album_title +' - '+self.artist


#each song will be linked to an album 
class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE) #whenever we delete
	#the album red for eg. all the songs in dat album will also be deleted
	#album has pk which is primary key dat becms the dforeign key for song
	file_type = models.CharField(max_length=20)
	song_title = models.CharField(max_length=250)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):#string representation of Album Object
		return self.song_title

