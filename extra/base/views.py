import json
import traceback

from django.http import JsonResponse
from django.views import View

from extra.base.enums import ResponseCodeEnum

from loguru import logger


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        param_dict = request.META
        log_params = dict(
            path=param_dict.get('PATH_INFO'), query=param_dict.get('QUERY_STRING'), remote=param_dict.get('REMOTE_ADDR'),
            body=request.body.decode()
        )
        self._log_info(f'get request msg: {log_params}')
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def response(code=ResponseCodeEnum.SUCCESS, msg='success', data=None):
        r = dict(result=code, message=msg)
        if data is not None:
            r['data'] = data
        return JsonResponse(r)

    @staticmethod
    def _log_error(error):
        logger.info(error)

    @staticmethod
    def _log_info(info):
        logger.info(info)


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
    page = None
    page_size = None

    def get(self, request):
        try:
            self.args = request.GET
            self.page = int(self.args.get('page', 1))
            self.page_size = int(self.args.get('pageSize', 20))
            return self._process(request)
        except Exception:
            self._log_error(f"get request error, msg: {traceback.format_exc()}")
            return self.response(ResponseCodeEnum.SYS_ERROR, "system error, please try again later.")

    def _process(self, request):
        raise NotImplemented("function not implement.")