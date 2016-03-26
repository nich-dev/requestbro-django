from models import UserPrefs


def save_profile_picture(strategy, user, response, details,
                         is_new=False,*args,**kwargs):
    print kwargs
    if 'twitch' in kwargs['backend'].name:
        social = user.social_auth.get(provider='twitch')
        token = social.extra_data['access_token']
        try:
            user_data=kwargs['backend'].user_data(token)
            prefs = UserPrefs.objects.get_or_create(user=user)[0]
            prefs.logo = user_data['logo']
            prefs.save()
        except Exception,e:
            print e
