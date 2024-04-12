from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    if request.method == "POST":
        user: str = get_value_by_id(request, 'ingUsuario')
        rol: str = get_value_by_id(request, 'ingPassword')
        is_valid_crendential: bool = user == 'admin' and rol == 'admin'
        if not is_valid_crendential:
            error = "Las credenciales son erroneas"
            return render(request, 'login.html', {"error": error})
        return HttpResponseRedirect(reverse('dashboard'))
    
    return render(request, 'login.html')


def get_value_by_id(request, id_control):
    return request.POST.get(id_control)

   