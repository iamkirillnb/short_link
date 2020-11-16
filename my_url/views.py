from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Links
from .serializers import LinksSerializer

class LinksView(APIView):

    def get(self, request, url):
        try:
            get_url = get_object_or_404(Links.objects.all(), shortened=url)
            if get_url.change_flag == True:
                return Response({'status': 'error', 'detail': 'link not active'})
            get_url.change_flag = True
            get_url.save()
            return Response({'status': 'ok', 'result': get_url.link})
        except Exception:
            return Response({'status': 'error', 'detail': 'link not found'})


    def post(self, request):
        link = request.data.get('links')
        serializer = LinksSerializer(data=link)
        if serializer.is_valid(raise_exception=True):
            link_saved = serializer.save()
            short = Links.objects.all().last()
        return Response({'status': 'ok', 'result': short.shortened})
