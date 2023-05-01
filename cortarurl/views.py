from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
import json
from django.http import HttpResponse
from .models import Listurls
from . import codigo_generar

def home(request):
    params = {}

    return render(request, "layout.html", params)

class CortarUrlAjax(View):
    def get(self, request):
        if request.is_ajax:
            url_original = request.GET["valor"]
            if Listurls.objects.filter(urloriginal=url_original).count() == 1:
                url_cortado = Listurls.objects.get(urloriginal=url_original)
                url_cortado = url_cortado.urlcorto
            else:      
                url = Listurls()
                url.urloriginal = url_original
                url.urlcorto = codigo_generar.codigo_url()
                url.save()
                url_cortado = Listurls.objects.get(urloriginal=url_original)
                url_cortado = url_cortado.urlcorto
            data = {}
            result = []
            data["url_cortado"] = "http://127.0.0.1:8000/"+str(url_cortado)

            result.append(data)
            data_json = json.dumps(result)
        else:
            data_json = "fallo"
        mimetype = "application/json"

        return HttpResponse(data_json, mimetype)


def url_corto(request, urlcorto):
    urloriginal = get_object_or_404(Listurls, urlcorto=urlcorto)
    urloriginal = urloriginal.urloriginal

    return redirect(urloriginal)