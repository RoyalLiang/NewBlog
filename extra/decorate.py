from django.http import JsonResponse

from loguru import logger


def catch_page(func):

    def wrapper(self, request, *args, **kwargs):
        # page = int(request.GET.get('page', 1))
        # page_size = int(request.GET.get('pageSize', 20))
        # logger.info(f"get request page: {page}, page_size:{page_size}")
        if self.page <= 0 or self.page_size <= 0:
            logger.error(f"get error page or pagesize, return error")
            r = dict(status='fail', message='get error page or pagesize', result={}, params={'isAuthenticated': False, 'url': '', 'isUnauthenticated': True, 'method': "GET", 'routes': {}})
            return JsonResponse(r)
        return func(self, request, *args, **kwargs)
    return wrapper
