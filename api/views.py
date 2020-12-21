from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import InputNumberSerializer
from .tasks import root_of_number


class RootApiView(APIView):
    def post(self, request):
        serializer = InputNumberSerializer(data=request.data)
        if serializer.is_valid():
            root_of_number.delay(serializer.data.get('input_number'))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
