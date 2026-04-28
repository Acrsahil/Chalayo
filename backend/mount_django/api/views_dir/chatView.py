from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Company,User
from ..serializers_dir.companySerializers import CompanySerializer
from django.db import transaction
from chatbot import chat



class ChatApiView(APIView):


    def post(self, request, id=None):
        get_input = request.data.get('input')
        chat_output = chat(get_input)
        return Response({"success": "True","chat_response": chat_output})



