from django import contrib
from django.shortcuts import render, redirect
from websurat.models import Surat
from websurat.forms import FormSuratKeluar
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings


# @login_required(login_url=settings.LOGIN_URL)
def surat_keluar(request):

    surat = Surat.objects.all().order_by('-nomor_surat')
    form = FormSuratKeluar()
    p = Paginator(surat, 10)

    page_num = request.GET.get('page', 1)
    print(request.user)

    template_name = None
    if request.user.is_authenticated:
        template_name = 'surat-keluar-admin.html'
    else:
        template_name = 'surat-keluar.html'

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if request.POST:
        form = FormSuratKeluar(request.POST)
        form.save()
        form = FormSuratKeluar()
        messages.success(request, "Data berhasil disimpan")
        return redirect('surat_keluar')
    else:
        form = FormSuratKeluar()

    konteks={
        'surat': page,
        'form':form,
    }

    return render(request, template_name, konteks)

def ubah_surat_keluar(request, id_surat):
    surat = Surat.objects.get(id=id_surat)
    form = FormSuratKeluar(instance=surat)
    
    if request.POST:
        form = FormSuratKeluar(request.POST, instance=surat)
        form.save()
        form = FormSuratKeluar()
        messages.success(request, "Data berhasil diperbaharui")
        return redirect('surat_keluar')

    konteks ={
        'form':form,
        'surat':surat,
    }
    return render(request, 'ubah-surat.html', konteks) 


def hapus(request, id_surat):
    surat = Surat.objects.filter(id=id_surat)
    surat.delete()
    return  redirect('surat_keluar')



def surat_masuk(request):
    return render(request, 'surat-masuk.html')

def format_surat(request):
    return render(request, 'format-surat.html')

def loginView(request):
    context = {
		'page_title':'LOGIN',
	}
    user = None

    if request.method == "GET":
        if request.user.is_authenticated:
			# logika untuk user
            return redirect('surat_keluar')
        else:
			# logika untuk anonymous
            return render(request, 'registration/login.html', context)

    if request.method == "POST":
		
        username_login = request.POST['username']
        password_login = request.POST['password']
		
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('surat_keluar')
        else:
            return redirect('masuk')
		
    return render(request, 'registration/login.html', context)

@login_required
def logoutView(request):

	logout(request)
	return redirect ('surat_keluar')

def cari(request):
    template_name = None
    if request.method == 'POST':
        search = request.POST['search']
        surat = Surat.objects.filter(nomor_surat__contains=search)
        if request.user.is_authenticated:
            template_name = 'surat-keluar-admin.html'
        else:
            template_name = 'surat-keluar.html'
    return render(request, template_name, 
            {'search':search,
              'surat':surat })    
    
    

