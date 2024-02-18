from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from client_comments.models import ClientComment
from massage_masters.models import MassageMaster


@receiver(post_save, sender=ClientComment)
def post_save_comment(sender, instance, created, **kwargs):
    if created:
        print('Comment saved. Calculate new rating')
        recalculate_master_rating(instance_master=instance.master)


@receiver(post_delete, sender=ClientComment)
def post_delete_comment(sender, instance, **kwargs):
    print('Comment deleted. Calculate new rating')
    recalculate_master_rating(instance_master=instance.master)


def recalculate_master_rating(instance_master: MassageMaster):
    comments = instance_master.comments.all()
    total_rating = sum(comment.rating for comment in comments)
    instance_master.master_rating = round(total_rating/len(comments), 1) if comments else 0
    instance_master.save()
