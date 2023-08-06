from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.utils.translation import ugettext as _
from garpix_user.models import UserSession
from garpix_user.serializers import RestoreByEmailSerializer, UserSessionTokenSerializer
from garpix_user.serializers.restore_passwrod_serializer import RestoreCheckCodeSerializer, RestoreSetPasswordSerializer


class RestoreEmailPasswordView(viewsets.ViewSet):

    def get_serializer_class(self):
        if self.action == 'send_code':
            return RestoreByEmailSerializer
        if self.action == 'check_code':
            return RestoreCheckCodeSerializer
        return RestoreSetPasswordSerializer

    @extend_schema(summary='Restore password by email. Step  1')
    @action(methods=['POST'], detail=False)
    def send_code(self, request, *args, **kwargs):
        user = UserSession.get_or_create_user_session(request)
        serializer = RestoreByEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = user.send_restore_code(email=serializer.data['email'])

        if result is not True:
            result.raise_exception(exception_class=ValidationError)
        return Response(UserSessionTokenSerializer(user).data)

    @extend_schema(summary='Restore password by email. Step  2')
    @action(methods=['POST'], detail=False)
    def check_code(self, request, *args, **kwargs):
        user = UserSession.get_or_create_user_session(request)

        serializer = RestoreCheckCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = user.check_restore_code(restore_confirmation_code=serializer.data['restore_confirmation_code'])

        if result is not True:
            result.raise_exception(exception_class=ValidationError)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(summary='Restore password by email. Step 3')
    @action(methods=['POST'], detail=False)
    def set_password(self, request, *args, **kwargs):
        user = UserSession.get_or_create_user_session(request)

        serializer = RestoreSetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = user.restore_password(new_password=serializer.data['new_password'])

        if result is not True:
            result.raise_exception(exception_class=ValidationError)
        return Response(_('Password was updated!'))
