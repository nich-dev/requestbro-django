from rest_framework import viewsets, permissions
import models, serializers
import permissions as mypermissions


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    permission_classes = (mypermissions.IsOwnerOrReadOnly,)


class UserPrefViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserPrefsSerializer
    queryset = models.UserPrefs.objects.all()
    permission_classes = (mypermissions.IsOwnerOrReadOnly,)


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.GenreSerializer
    queryset = models.Genre.objects.all()


class SongViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SongRequestViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SongRequestSerializer
    queryset = models.SongRequest.objects.all()
    permission_classes = (mypermissions.IsOwnerOrReadOnly,)


class SongRequestDetailedViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.SongRequestDetailedSerializer
    queryset = models.SongRequest.objects.all()
    permission_classes = (mypermissions.IsOwnerOrReadOnly,)


