from django.db import models


class Trending(models.Model):
    tv_id = models.IntegerField(primary_key=True)
    backdrop_path = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    overview = models.TextField()
    poster_path = models.CharField(max_length=255)
    adult = models.BooleanField()

    def __str__(self):
        return self.name


class Details(models.Model):
    tv_id = models.OneToOneField(
        Trending, on_delete=models.CASCADE, primary_key=True, db_column="details_id"
    )
    last_episode_name = models.CharField(max_length=255, null=True, blank=True)
    genres = models.TextField()

    def __str__(self):
        return f"Details for {self.tv_id.name}"


class Cast(models.Model):
    tv_id = models.OneToOneField(
        Trending, on_delete=models.CASCADE, primary_key=True, db_column="cast_id"
    )
    cast_names = models.TextField()

    def __str__(self):
        return f"Cast for {self.tv_id.name}"


class Video(models.Model):
    tv_id = models.OneToOneField(
        Trending, on_delete=models.CASCADE, primary_key=True, db_column="video_id"
    )
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"Video for {self.tv_id.name}"
