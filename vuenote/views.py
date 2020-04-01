#from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from vuenote.models import Note
from vuenote.serializers import NoteSerializer


# Note viewset
# Create, edit or display our notes via the API
class NoteViewSet(viewsets.ModelViewSet):
    #Check permissions

    #permission_classes = (IsAuthenticated,)
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    authentication_classes = (TokenAuthentication,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'id'