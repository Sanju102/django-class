# from django.http import JsonResponse
# from watchlist_app.models import Movie

# # Create your views here.
# def movie_list(request):
#     movies=Movie.objects.all()
#     data={
#         "data":list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_deatails(request,pk):
#     movie=Movie.objects.get(pk=pk)
#     data={
#         "id":movie.id,
#         "name":movie.name,
#         "active":movie.active,
#     }

#     return JsonResponse(data)