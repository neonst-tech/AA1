from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def announcement_list(request):
    return render(request, "announcements/list.html")


def announcement_detail(request, pk):
    return render(request, "announcements/detail.html")
