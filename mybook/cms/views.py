from django.shortcuts import render
from django.http import HttpResponse

def book_list(request):
    return HttpResponse('書籍の一覧')

def book_edit(request):
    return HttpResponse('書籍の編集')

def book_del(request):
    return HttpResponse('書籍の削除')


