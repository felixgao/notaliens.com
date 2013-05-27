from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')

    config = Configurator(
        settings=settings
        , session_factory=session_factory
    )

    config.add_static_view('static', 'static', cache_max_age=3600)

    config.include('notaliens.core')
    config.include('notaliens.people', route_prefix='/people')
    config.include('notaliens.identity', route_prefix='/identity')

    config.scan()

    return config.make_wsgi_app()