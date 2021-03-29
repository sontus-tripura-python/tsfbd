from Home_app.models import DeveloperInfo, TsfAboutSetting

def about_inform(request):
    about_inform = TsfAboutSetting.objects.first()
    return {'about_inform': about_inform}

def developer_info(request):
    developer_info = DeveloperInfo.objects.first()
    return {'developer_info': developer_info}