import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .models import Bookmark


def get_bookmarks(request):
    bookmarks = Bookmark.objects.filter(read=False, deleted=False).all()

    data = []
    for bookmark in bookmarks:
        data.append(
            {
                "id": bookmark.pk,
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


@csrf_exempt
def batch_add(request):
    data = json.loads(request.body.decode("utf-8"))["data"]

    bookmarks = []
    for d in data:
        bookmarks.append(
            Bookmark(title=d["title"], url=d["url"], time=d["time"])
        )
    Bookmark.objects.bulk_create(bookmarks)

    return HttpResponse(status=201)


@csrf_exempt
def read_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, pk=id)
    bookmark.read = True
    bookmark.save()
    return HttpResponse(status=201)


@csrf_exempt
def delete_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, pk=id)
    bookmark.deleted = True
    bookmark.save()
    return HttpResponse(status=201)
