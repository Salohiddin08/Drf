from rest_framework_simplejwt.tokens import RefreshToken


def get_user_token(user):
    refresh_token = RefreshToken.for_user(user)
    return {
        'access_token': str(refresh_token.access_token),
        'refresh_token': str(refresh_token)
    }