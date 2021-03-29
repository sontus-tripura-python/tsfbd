from About_app.models import *

def about_categories(request):
    about_categories = Category.objects.all()
    return {'about_categories': about_categories }