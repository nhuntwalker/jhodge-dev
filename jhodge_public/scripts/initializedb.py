import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from ..models import (
    Writing,
    Film,
    Contact
)

from .media_data import (
    FILMS,
    WRITINGS,
    AWARDS
)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    settings["sqlalchemy.url"] = os.environ["DATABASE_URL"]

    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        add_these = []

        for film in FILMS:
            # import pdb; pdb.set_trace()
            film_awards = [AWARDS[award] for award in film["awards"]]
            new_film = Film(
                title=film["title"],
                release_date=film["release_date"],
                production=film["production"],
                slug=film["slug"],
                excerpt=film["excerpt"],
                slider_text=film["slider_text"],
                home_text=film["home_text"],
                full_text="\r\n".join(film["full_text"]),
                trailer=film["trailer"],
                screenshot=film["screenshot"],
                awards="||".join(film_awards)
            )
            add_these.append(new_film)

        for writing in WRITINGS:
            new_script = Writing(
                title=writing["title"],
                published_on=writing["published_on"],
                publisher=writing["publisher"],
                slug=writing["slug"],
                full_text="\r\n".join(writing["full_text"]),
                external_link=writing["external_link"],
                cover_img=writing["cover_img"],
                center=writing["center"]
            )
            add_these.append(new_script)

        dbsession.add_all(add_these)
