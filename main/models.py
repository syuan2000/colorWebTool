from django.db import models

class Frame(models.Model):
    id = models.IntegerField(primary_key=True)
    frameid = models.BigIntegerField()
    movieid = models.ForeignKey('Movie', on_delete=models.CASCADE, db_column = 'movieid')
    image = models.ImageField(blank=True, null=True)
    top10_palette = models.CharField(max_length=100, blank=True, null=True) 
    kmeans_palette = models.CharField(max_length=100,blank=True, null=True) 
    random_palette = models.CharField(max_length=100, blank=True, null=True) 
    
    class Meta:
        unique_together = (('movieid','frameid'),)
        db_table = 'Frame'

    def __str__(self):
        return f'{self.movieid}-{self.frameid}'


class Movie(models.Model):

    title = models.CharField(max_length=50, blank=True, null=True)
    top10_palette = models.ImageField(blank=True, null=True)
    kmeans_palette = models.ImageField(blank=True, null=True)
    random_palette = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Movie'

class Participant(models.Model):

    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)  
    cb_status = models.CharField(max_length=20, blank=True, null=True)  
    media_industry = models.TextField(blank=True, null=True) 
    seen_history = models.TextField(blank=True, null=True)
    movieid = models.ForeignKey('Movie', on_delete=models.CASCADE, db_column = 'movieid')
    single_frameid = models.ForeignKey('Frame', on_delete=models.CASCADE, db_column = 'single_frameid')
    single_choise = models.CharField(max_length=20, blank=True, null=True) 
    multi_choice = models.CharField(max_length=20, blank=True, null=True)  

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Participant'


