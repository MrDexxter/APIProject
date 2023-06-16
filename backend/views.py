from rest_framework.views import APIView
from rest_framework.response import Response

class CapitalizeView(APIView):
    def post(self, request, format=None):
        data = request.data
        input_string = data.get('input_string', '')
        return Response({'result': input_string.upper()})
