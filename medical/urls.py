from django.urls import path
from .views import OCRView ,TextView
urlpatterns=[
       path("ocr/",OCRView.as_view(),name="ocr"),
       path("text/",TextView.as_view(),name="text"),
]