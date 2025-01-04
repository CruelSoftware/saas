from django.shortcuts import render

from visits.models import PageVisits


def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    title = "About"
    try:
        percent = (page_qs.count() * 100) / qs.count()
    except Exception:
        percent = 0

    context = {
        "page_title": title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    PageVisits.objects.create(path=request.path)
    html_template = "home.html"
    return render(request, html_template, context)