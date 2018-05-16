from django.http import JsonResponse

from .models import Bookmark


def get_bookmarks(request):
    bookmarks = Bookmark.objects.all()

    data = []
    for bookmark in bookmarks:
        data.append(
            {
                "title": bookmark.title,
                "url": bookmark.url,
                "time": bookmark.time,
                "read": bookmark.read,
                "deleted": bookmark.deleted,
                "created_at": bookmark.created_at,
                "updated_at": bookmark.updated_at,
            }
        )

    return JsonResponse({"data": data})
