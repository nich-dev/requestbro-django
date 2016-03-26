from rest_framework import viewsets, permissions
import models, serializers
import permissions as mypermissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    lookup_field = ('username')
    permissions = (mypermissions.ReadOnly)


class UserPrefViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserPrefsSerializer
    queryset = models.UserPrefs.objects.all()
    permission_classes = (mypermissions.IsOwnerOrReadOnly,)


class SongViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class SongRequestViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SongRequestSerializer
    queryset = models.SongRequest.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class SongRequestDetailedViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SongRequestDetailedSerializer
    queryset = models.SongRequest.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = models.SongRequest.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        session = self.request.query_params.get('session', None)
        if session is not None:
            queryset = queryset.filter(session__pk=session)
        return queryset


class SessionDetailedViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SessionSerializer
    queryset = models.Session.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = models.Session.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class SessionSimpleViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SessionSimpleSerializer
    queryset = models.Session.objects.all()
    permission_classes = (permissions.IsAuthenticated,)