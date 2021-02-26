import logging

import aiohttp
from aiohttp import web
import aiohttp_cors

from json_schema_validator.routes import routes
from json_schema_validator.settings import config


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()
    cors = aiohttp_cors.setup(app)

    app['http_session'] = aiohttp.ClientSession()
    
    app.router.add_routes(routes)

    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })

    for route in list(app.router.routes()):
        cors.add(route)

    
    app['config'] = config
    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    main()