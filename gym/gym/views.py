from django.shortcuts import render
from gym.models import Program,Vezba,StaKoVezba
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as lgn
from django.http import HttpResponseRedirect

def naslovna(req):
    programi = Program.objects.all()
    idprograma = int(req.GET.get("program")) if req.GET.get("program") else 0
    vezbe = Vezba.objects.filter(program=idprograma)

    izlaz = render(req,"index.html",{
        "programi":programi,
        "vezbe":vezbe,
        "idprograma":idprograma
        }
    )
    return izlaz


def detalji(req,idvezbe):
    vezba = Vezba.objects.get(id=idvezbe)
    return render(req,"detalji.html",{"vezba":vezba}) 


def odabir(req,idprograma):
    korisnik = req.user
    if korisnik.is_authenticated:
        skv = StaKoVezba()
        skv.id = korisnik.id
        skv.program_vezbanja = idprograma
        skv.save()
        return render(req,"odabir.html")
    else:
        return render(req,"invaliduser.html")
    

def login(req):
    if req.method.lower() == "post":
        username = req.POST.get("username")
        passwd = req.POST.get("password")
        user = authenticate(username=username,password=passwd)
        if user:
            lgn(req,user)
            return HttpResponseRedirect("/")
        else:
            return render(req,"invaliduser.html")
    else:
        return render(req,"login.html")