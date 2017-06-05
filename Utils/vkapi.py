from vk import *
from vk import api
import requests.exceptions
import time
import logging
"""
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)
"""

class API(API):
    def __getattr__(self, method_name):
        return Request(self, method_name)


class Request(api.Request):
    def __getattr__(self, method_name):
        return Request(self._api, self._method_name + '.' + method_name)

    def __call__(self, **method_args):
        self._method_args = method_args
        return self.__create_request__()

    def __create_request__(self):
        try:
            data = self._api._session.make_request(self)
            #print('Create request to VK Api: {} {}'.format(self._method_name, self._method_args))
        except api.VkAPIError as ex:
            #print('Exception: {}'.format(ex))
            if ex.code == 15 or ex.code == 18 or ex.code == 5 or ex.code == 19:
                data = None
            elif ex.code == 100:
                raise ex
            elif ex.code == 6:
                time.sleep(1)
                data = self.__create_request__()
            else:
                data = self.__create_request__()
        except requests.exceptions.ReadTimeout as ex:
            # print('Exception: {}'.format(ex))
            # logging.warning('Exception: {}'.format(ex))
            time.sleep(0.1)
            data = self.__create_request__()
        except requests.exceptions.ConnectionError as ex:
            # print('Exception: {}'.format(ex))
            # logging.warning('Exception: {}'.format(ex))
            data = self.__create_request__()
        return data

