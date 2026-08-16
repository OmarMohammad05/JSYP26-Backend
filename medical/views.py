from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from.services.ocr_service import OCRService
from .serializers import OCRSerializer ,TextSerializer
import os
import tempfile
from .services.text_processor import TextProcessor
# Create your views here.
class OCRView(APIView):
    def post(self,request):
        serializer=OCRSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image=serializer.validated_data["image"]
        # save a  image as file bacause the ocr function take a path and after extract text delete image.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            for chunck in image.chunks(): #  chunks  to sperate an image to batchies. because django to able to take all image in once time.
                temp_file.write(chunck)
            temp_path=temp_file.name
        try:
            ocr_obj = OCRService()
            text=ocr_obj.extract_text(temp_path)

            if not text:
                return Response({"details":"No text was detected in the image"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
            return Response(
            text,
            status=status.HTTP_200_OK
            )
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

class TextView(APIView):
    def post(self,request):
        serializer= TextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text=serializer.validated_data["text"]
        processed_obj=TextProcessor()
        claim=processed_obj.clean(text)

        if not text:
            return Response({"details":"No text in the message"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(claim,status=status.HTTP_200_OK)
