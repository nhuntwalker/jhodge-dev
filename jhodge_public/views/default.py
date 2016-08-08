from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import sessionmaker

from ..models import (
    Film,
    Writing,
    Contact,
    get_engine
)

def get_session(request):
    engine = get_engine(request.registry.settings)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_slug(title):
    slug = title.lower().replace('the','').strip().replace(' ', '-')
    return slug

@view_config(route_name='home', renderer='../templates/home.jinja2')
def home(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='about', renderer='../templates/about.jinja2')
def about(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='contact', renderer='../templates/contact.jinja2')
def contact(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='film', renderer='../templates/film.jinja2')
def film(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='film_single', renderer='../templates/film-single.jinja2')
def film_single(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='writing', renderer='../templates/writing.jinja2')
def writing(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='writing_single', renderer='../templates/writing-single.jinja2')
def writing_single(request):
    return {'project': 'jhodge_public'}

@view_config(route_name='create_film', renderer='../templates/film-create.jinja2')
def create_film(request):
    if request.method == "POST":
        new_film = Film(
            title=request.POST["title"],
            slug=create_slug(request.POST["title"]),
            release_date=request.POST["release_date"],
            production=request.POST["production"],
            production_link=request.POST["production_link"],
            director=request.POST["director"],
            cast=request.POST["cast"],
            excerpt=request.POST["excerpt"],
            full_text=request.POST["full_text"],
            trailer=request.POST["trailer"]
        )

        session = get_session(request)
        session.add(new_film)
        session.commit()

        return HTTPFound(location=request.route_url("home"))

    return {'project': 'jhodge_public'}

@view_config(route_name='create_writing', renderer='../templates/writing-create.jinja2')
def create_writing(request):
    return {'project': 'jhodge_public'}
