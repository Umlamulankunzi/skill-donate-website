from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def volunteer_required(func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    """Decorator for views that checks that the logged in user is a volunteer,
    redirects to the log-in page if necessary.
    """
    decorator = user_passes_test(
        lambda user: user.is_active and user.is_volunteer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if func:
        return decorator(func)
    return decorator
