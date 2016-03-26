import json
from django.shortcuts import render, HttpResponse
from django.views.generic import (TemplateView, FormView, RedirectView,
                                  UpdateView, CreateView, View)
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login
import models, forms
from django.contrib.auth.models import User
from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa
from djrequest.decorators import render_to


def get_theme_color(obj):
    if obj.request.user.id:
        return models.UserPrefs.objects.get_or_create(user=obj.request.user)[0].color
    return "blue"


class Landing(TemplateView):
    def get_template_names(self):
        if self.request.user.id:
            if self.request.is_ajax():
                return ['dash.html']
            else:
                return ['container/dash.html']
        if self.request.is_ajax():
            return ['base.html']
        else:
            return ['container/base.html']

    def get_context_data(self, **kwargs):
        context = super(Landing, self).get_context_data(**kwargs)
        context['theme'] = get_theme_color(self)
        return context


class Profile(TemplateView):
    def get_template_names(self):
        if self.request.is_ajax():
            return ['user.html']
        else:
            return ['container/user.html']

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        try:
            username = self.kwargs['username']
            if username is None or username is "" or username is "profile":
                username = self.request.user.username
        except:
            username = self.request.user.username
        try:
            lookup_user = User.objects.get(username=username)  # get the viewable user
            context['lookup_user'] = lookup_user
            context['lookup_user_prefs'] = models.UserPrefs.objects.get_or_create(user=lookup_user)[0]
            context['theme'] = context['lookup_user_prefs'].color
            return context
        except Exception, e:
            print e
            context['theme'] = get_theme_color(self)
            return context


class UserEdit(FormView):
    model = models.UserPrefs
    form_class = forms.UserPrefForm
    success_url = '/accounts/profile/'

    def get_template_names(self):
        if self.request.is_ajax():
            return ['user.edit.html']
        else:
            return ['container/user.edit.html']

    def get_initial(self):
        initial = super(UserEdit, self).get_initial()
        user_pref = models.UserPrefs.objects.get_or_create(user=self.request.user)[0]
        initial['default_link'] = user_pref.default_link
        initial['banned_users'] = user_pref.banned_users.all()
        initial['banned_songs'] = user_pref.banned_songs.all()
        initial['following_users'] = user_pref.following_users.all()
        initial['mod_users'] = user_pref.mod_users.all()
        initial['banned_songs_by_word'] = user_pref.banned_songs_by_word
        initial['dark'] = user_pref.dark
        initial['color'] = user_pref.color
        return initial


class SessionFormView(FormView):
    model = models.Session
    form_class = forms.SessionForm
    success_url = '/'  # TODO

    def get_template_names(self):
        if self.request.is_ajax():
            return ['session.form.html']
        else:
            return ['container/session.form.html']


class SongFormView(FormView):
    model = models.Song
    form_class = forms.SongForm
    success_url = '/'  # TODO

    def get_template_names(self):
        if self.request.is_ajax():
            return ['song.form.html']
        else:
            return ['container/song.form.html']


class SongRequestFormView(FormView):
    model = models.SongRequest
    form_class = forms.SongRequestForm
    success_url = '/'  # TODO

    def get_template_names(self):
        if self.request.is_ajax():
            return ['song_request.form.html']
        else:
            return ['container/song_request.form.html']


class LoginRedirect(RedirectView):
    def dispatch(self, request, *args, **kwargs):
        return RedirectView.dispatch(self, request, *args, **kwargs)


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


def context(**extra):
    return dict({
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)


@render_to('home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return context()


@login_required
@render_to('home.html')
def done(request):
    """Login complete view, displays user data"""
    return context()


@render_to('home.html')
def validation_sent(request):
    return context(
        validation_sent=True,
        email=request.session.get('email_validation_address')
    )


@render_to('home.html')
def require_email(request):
    backend = request.session['partial_pipeline']['backend']
    return context(email_required=True, backend=backend)


@psa('social:complete')
def ajax_auth(request, backend):
    if isinstance(request.backend, BaseOAuth1):
        token = {
            'oauth_token': request.REQUEST.get('access_token'),
            'oauth_token_secret': request.REQUEST.get('access_token_secret'),
        }
    elif isinstance(request.backend, BaseOAuth2):
        token = request.REQUEST.get('access_token')
    else:
        raise HttpResponseBadRequest('Wrong backend type')
    user = request.backend.do_auth(token, ajax=True)
    login(request, user)
    data = {'id': user.id, 'username': user.username}
    return HttpResponse(json.dumps(data), mimetype='application/json')
