from django.http import JsonResponse


def catch_page(func):

    def wrapper(request, *args, **kwargs):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('pageSize', 20))
        if page <= 0 or page_size <= 0:
            r = dict(status='fail', message='fail', result={}, params={'isAuthenticated': False, 'url': '', 'isUnauthenticated': True, 'method': "GET", 'routes': {}})
            return JsonResponse(r)
        return func(request, *args, **kwargs)
    return wrapper
