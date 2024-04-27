from django.http import HttpResponse
from rest_framework.decorators import APIView
from myapp.utils import ExportExcel


# Create your views here.


class ExportOrder(APIView):
    def get(self, request):
        print("ok")
        export = ExportExcel()
        status, response = export.get_data()
        if status:
            return response

        return HttpResponse("Something Went Wrong")



