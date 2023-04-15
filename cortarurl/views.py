from django.shortcuts import render
from django.views.generic import View
import json
from django.http import HttpResponse

def home(request):
    params = {}

    return render(request, "layout.html", params)

class CortarUrlAjax(View):
    def get(self, request):
        if request.is_ajax:
            url_original = request.GET["valor"]
            data = {}
            result = []
            data["url_cortado"] = "mipagina.com/xlkr93"

            result.append(data)
            data_json = json.dumps(result)
            print("Hola")
        else:
            data_json = "fallo"
        mimetype = "application/json"

        return HttpResponse(data_json, mimetype)
