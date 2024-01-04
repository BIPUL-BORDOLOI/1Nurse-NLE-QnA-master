from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField(null=True, blank=True)
    username = models.CharField(unique=True, max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    interest = models.JSONField(null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)
    followed_by = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followings', blank=True)
    bookmarked_posts = models.ManyToManyField('Question', related_name='bookmarked_users', blank=True)
    profile_url = models.URLField(null=True, blank=True)

class Employement(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    currently_working = models.BooleanField(null=True, blank=True)

class Education(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    primary_major = models.CharField(max_length=255, null=True, blank=True)
    secondary_major = models.CharField(max_length=255, null=True, blank=True)
    degree_type = models.CharField(max_length=25, null=True, blank=True)
    graduation_year = models.IntegerField(null=True, blank=True)

class Location(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    loc = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    currently_living = models.BooleanField(null=True, blank=True)

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    cover_img = models.URLField(null=True, blank=True)
    name = models.CharField(unique=True, max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent_topic_id = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)
    child_topic_id = models.ManyToManyField('self', symmetrical=False, related_name='child_topics', blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    createdAt = models.DateTimeField(null=True, blank=True)
    view_count = models.IntegerField(null=True, blank=True)
    upvote_count = models.IntegerField(null=True, blank=True)
    downvote_count = models.IntegerField(null=True, blank=True)
    keywords = models.JSONField(null=True, blank=True)
    question_url = models.URLField(null=True, blank=True)

class Vote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    type = models.BooleanField(null=True, blank=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    votable_type = models.IntegerField(null=True, blank=True)
    votable_id = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    body = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    view_count = models.IntegerField(null=True, blank=True)
    upvote_count = models.IntegerField(null=True, blank=True)
    downvote_count = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    body = models.TextField(null=True, blank=True)
    comment_type = models.IntegerField(null=True, blank=True)
    commentable_id = models.CharField(max_length=255, null=True, blank=True)
    parent_comment_id = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    upvote_count = models.IntegerField(null=True, blank=True)
    downvote_count = models.IntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    content = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    upvote_count = models.IntegerField(null=True, blank=True)
    downvote_count = models.IntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)
    post_url = models.URLField(null=True, blank=True)

class Notifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    type = models.IntegerField(null=True, blank=True)
    notification_url = models.URLField(null=True, blank=True)
    seen = models.BooleanField(null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)
    readAt = models.DateTimeField(null=True, blank=True)

