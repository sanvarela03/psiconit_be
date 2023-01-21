from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from auth_app.models.user import User
from auth_app.serializers.user_serializer import UserSerializer

from rest_framework.request import Request


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):

        # token = request.META.get('HTTP_AUTHORIZATION')[7:]
        token = request.auth.token
        print("$El REQUEST:")
        print(len(request.data))
        print("$El TOKEN:")
        print(request.auth.token)
        print("$El USUARIO:")
        print(type(request.user))
        print("$EL HEADER :" + request.META.get('HTTP_AUTHORIZATION')[0:])
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        print("$Valid_data:")
        print(valid_data)

        print("$KWARGS:")
        print(kwargs)

        print("$ .authenticators : ")
        print(type(request.authenticators))
        print(len(request.authenticators))
        print(request.authenticators)

        print("$ .content_type : ")
        print(type(request.content_type))
        print(len(request.content_type))
        print(request.content_type)

        print("$ .stream : ")
        print(request.stream)

        print("$ .session (from HttpRequest) : ")
        print(type(request.session))
        print(request.session)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)
