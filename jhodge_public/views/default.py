# -*- coding: utf-8 -*-

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.orm import sessionmaker

from ..models import (
    Film,
    Writing,
    Contact,
    get_engine
)

GH_MEDIA = "https://raw.githubusercontent.com/nhuntwalker/jhodge-dev/master/jhodge_public/static/MEDIA/"
GH_STATIC = "https://raw.githubusercontent.com/nhuntwalker/jhodge-dev/master/jhodge_public/static/STATIC_FILES/"


def get_session(request):
    """Start a session for model management."""
    engine = get_engine(request.registry.settings)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_slug(title):
    """Create a URL-friendly slug out of a model title."""
    slug = title.lower().replace('the', '').replace(
        "'", '').strip().replace(' ', '-')
    return slug


def get_media_path(request, media_path):
    """Get the media path given Pyramid configuration."""
    outpath = request.static_path("jhodge_public:static/MEDIA/%s" % media_path)
    return outpath


@view_config(route_name='home',
             renderer='../templates/home.jinja2')
def home(request):
    """Display data to the Home page."""
    return {
        'home': True,
        'gh_media': GH_MEDIA,
        'gh_static': GH_STATIC
    }


@view_config(route_name='about',
             renderer='../templates/about.jinja2')
def about(request):
    """Display data to the About page."""
    return {
        'project': 'jhodge_public',
        'about': True,
        'gh_media': GH_MEDIA,
        'gh_static': GH_STATIC
    }


@view_config(route_name='contact',
             renderer='../templates/contact.jinja2')
def contact(request):
    """Display data to the Contact page and handle POST requests."""
    msg = ''

    if request.method == "POST":
        new_contact = Contact(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"]
        )

        session = get_session(request)
        session.add(new_contact)
        session.commit()

        msg = "Thanks for getting in touch!"

        return HTTPFound(location=request.route_url("home"))

    return {
        'project': 'jhodge_public',
        'msg': msg,
        'contact': True,
        'gh_media': GH_MEDIA,
        'gh_static': GH_STATIC
    }


@view_config(route_name='films',
             renderer='../templates/film.jinja2')
def films(request):
    """Display data to the Film page."""
    films = request.dbsession.query(Film).all()
    slider_titles = [
        "the jump", "the kind ones", "the knockout game", "threading needles"]
    slider_films = []

    for film in films:
        film.screenshot_url = GH_MEDIA + film.screenshot
        if film.title.lower() in slider_titles:
            slider_films.append(film)

    return {
        'project': 'jhodge_public',
        'film': True,
        'all_films': films,
        'slider_films': slider_films,
        'gh_media': GH_MEDIA,
        'gh_static': GH_STATIC
    }


@view_config(route_name='film_single',
             renderer='../templates/film-single.jinja2')
def film_single(request):
    """Display data for an individual film."""
    film = request.dbsession.query(Film).get(request.matchdict["id"])
    film.screenshot_url = GH_MEDIA + film.screenshot
    full_text = film.full_text.split("\r\n")
    awards = film.awards.split("||")
    # import pdb; pdb.set_trace()

    return {
        'project': 'jhodge_public',
        'film': True,
        'the_film': film,
        "full_text": full_text,
        "awards": awards,
        'gh_media': GH_MEDIA,
        'gh_static': GH_STATIC
    }


@view_config(route_name='writings',
             renderer='../templates/writing.jinja2')
def writings(request):
    """Display data to the Writing page."""
    writings = request.dbsession.query(Writing).all()
    for writ in writings:
        writ.cover_url = get_media_path(request, writ.cover_img)
    return {
        'project': 'jhodge_public',
        'writing': True,
        'all_writings': writings
    }


@view_config(route_name='writing_single',
             renderer='../templates/writing-single.jinja2')
def writing_single(request):
    """Display data for an individual writing sample."""
    writing = request.dbsession.query(Writing).get(request.matchdict["id"])

    writing.cover_url = get_media_path(request, writing.cover_img)
    full_text = writing.full_text.split("\r\n")
    if writing.center:
        for i in range(len(full_text)):
            full_text[i] = full_text[i].split("<br/>")

    return {
        'project': 'jhodge_public',
        'writing': True,
        "the_writing": writing,
        "full_text": full_text,
    }


@view_config(route_name="awards_list",
             renderer="../templates/awards.jinja2")
def awards(request):
    """Award listing view."""
    return {
        'gh_media': GH_MEDIA,
        'awards_list': True
    }


# @view_config(route_name='create_film',
#              renderer='../templates/film-create.jinja2')
# def create_film(request):
#     """Display the form for and harvest data from a new Film entry."""
#     if request.method == "POST":
#         new_film = Film(
#             title=request.POST["title"],
#             slug=create_slug(request.POST["title"]),
#             release_date=request.POST["release_date"],
#             production=request.POST["production"],
#             production_link=request.POST["production_link"],
#             director=request.POST["director"],
#             cast=request.POST["cast"],
#             excerpt=request.POST["excerpt"],
#             full_text=request.POST["full_text"],
#             trailer=request.POST["trailer"]
#         )

#         session = get_session(request)
#         session.add(new_film)
#         session.commit()

#         return HTTPFound(location=request.route_url("home"))

#     return {'project': 'jhodge_public'}


# @view_config(route_name='create_writing',
#              renderer='../templates/writing-create.jinja2')
# def create_writing(request):
#     """Display the form for and harvest data from a new Writing entry."""
#     if request.method == "POST":
#         new_writing = Writing(
#             title=request.POST["title"],
#             slug=create_slug(request.POST["title"]),
#             release_date=request.POST["release_date"],
#             production=request.POST["production"],
#             production_link=request.POST["production_link"],
#             director=request.POST["director"],
#             cast=request.POST["cast"],
#             excerpt=request.POST["excerpt"],
#             full_text=request.POST["full_text"],
#             trailer=request.POST["trailer"]
#         )

#         session = get_session(request)
#         session.add(new_writing)
#         session.commit()

#         return HTTPFound(location=request.route_url("home"))

#     return {'project': 'jhodge_public'}


# @view_config(route_name='admin', renderer='../templates/admin.jinja2')
# def admin(request):
#     """Display the admin page with links to item creation."""
#     return {'project': 'jhodge_public'}
