import json
import traceback

from django.http import JsonResponse
from django.views import View

from extra.base.enums import ResponseCodeEnum

from loguru import logger


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        logger.info(f"origin request args: {request.META}")
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def response(code=ResponseCodeEnum.SUCCESS, msg='success', data=None):
        r = dict(result=code, msg=msg)
        if data:
            r['data'] = data
        return JsonResponse(r)

    @staticmethod
    def _log_error(error):
        logger.info(error)


class BasePostView(BaseView):
    req = None

    def post(self, request):
        self.req = json.loads(request.body.decode())
        try:
            return self._process(request)
        except Exception:
            self._log_error(f"post request error, msg: {traceback.format_exc()}")
            return self.response(ResponseCodeEnum.SYS_ERROR, "system error, please try again later.")

    def _process(self, request):
        raise NotImplemented("function not implement.")


class BaseGetView(BaseView):
    args = None

    def get(self, request):
        try:
            self.args = request.GET
            return self._process(request)
        except Exception:
            self._log_error(f"get request error, msg: {traceback.format_exc()}")
            return self.response(ResponseCodeEnum.SYS_ERROR, "system error, please try again later.")

    def _process(self, request):
        raise NotImplemented("function not implement.")
