from nanohttp import Controller, json
from restfulpy.controllers import RootController

import coding-style
from .foo import FooController


class ApiV1(Controller):
    foos = FooController()

    @json
    def version(self):
        return {
            'version': coding-style.__version__
        }


class Root(RootController):
    apiv1 = ApiV1()

