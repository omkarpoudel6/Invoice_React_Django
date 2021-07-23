from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostModelSerializer
from ..models import Post


@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        qs=Post.objects.all()
        serializer=PostModelSerializer(qs,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=PostModelSerializer(data=request.data)
        if serializer.is_valid():
            #add_logic
            return Response(serializer.data,status=status.HTTP_201_Created)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)