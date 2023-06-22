from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField

yearOfRelease = (
    ('2021','2021'),
    ('2020','2020'),
    ('2019','2019'),
    ('2018','2018'),
    ('2017','2017'),
    ('2016','2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004','2004'),
    ('2003','2003'),
    ('2002','2002'),
    ('2001','2001'),
    ('2000','2000'),
    ('1995','1995'),
    ('1990','1990'),
    ('1985','1985'),
)

genre = (
    ('pop music','Поп музыка'),
    ('Rock','Рок'),
    ('Phonk','Фонк'),
    ('House','Хаус'),
    ('Electronic pop music','Электро-поп'),
    ('Indi','Инди'),
    ('Electro','Электро'),
    ('Alternative Rock','Альтернативный рок'),
    ('Dicko','Диско'),
)

language = (
    ('Hindi','Хинди'),
    ('Engligh','Английский'),
    ('Russian','Русский'),
    ('Tartarian', 'Татарский'),
    ('French','Французский')
)


tags = (
    ('Album','Альбом'),
    ('Bollywood','Болливуд'),
    ('Hollywood','Голливуд'),
)

productionHouse = (
    ('T-Series','T-Series'),
    ('Sony Music','Sony Music'),
    ('Unknown','Неизвестный')
)



# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0, verbose_name = 'Номер песни')
    name = models.CharField(max_length=200, verbose_name = 'Название')
    tags = models.CharField(choices=tags, max_length=20, default='Classical', verbose_name = 'Теги')
    genre = models.CharField(choices=genre, max_length=20, default='Album', verbose_name = 'Жанр')
    language = models.CharField(choices=language, max_length=20, default='Hindi', verbose_name = 'Язык исполнения')
    year = models.CharField(choices=yearOfRelease, max_length=20, default='2021', verbose_name = 'Год выпуска')
    singer1 = models.CharField(max_length=200, verbose_name = 'Первый исполнитель')
    singer2 = models.CharField(max_length=200, default='', verbose_name = 'Второй исполнитель')
    productionHouse = models.CharField(choices=productionHouse, max_length=20, default='Unknown', verbose_name = 'Продюсерский дом')
    movie = models.CharField(max_length=500, default="", verbose_name = 'Видео') # нужно ли это???
    image = models.ImageField(upload_to="images", verbose_name = 'Обложка')
    song = models.FileField(upload_to='songs', verbose_name = 'Песня')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    music_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = 'История'

class LikedSong(models.Model):
    liked_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    music_id = models.CharField(max_length=10000000, default="")

    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = 'Понравившиеся песни'


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    music_ids = ListCharField(base_field=models.CharField(max_length=100), size=100, max_length=(100 * 101))
    playlist_name = models.CharField(max_length=10000000, default="", verbose_name = 'Название плейлиста')
    likes = models.IntegerField(default=0, verbose_name = 'Лайки')
    followers = models.IntegerField(default=0, verbose_name = 'Подписчики')
    plays = models.IntegerField(default=0, verbose_name = 'Воспроизвести')

    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'

class Singer(models.Model):
    singer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name = 'Название')
    image = models.ImageField(upload_to="images/Singer", verbose_name = 'Обложка')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'