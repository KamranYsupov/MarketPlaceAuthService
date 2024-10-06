from dependency_injector import containers, providers

from app.repositories import (
    RepositoryRefreshToken,
    RepositoryUser,
)
from app.services import (
    JWTService,
    UserService,
)
from app.db import (
    DataBaseManager,
)

from app.db.models import (
    RefreshToken,
    User,
)
    
from app.core.config import settings


class Container(containers.DeclarativeContainer):
    db_manager = providers.Singleton(DataBaseManager, db_url=settings.db_url)
    session = providers.Resource(db_manager().get_async_session)

    repository_refresh_token = providers.Singleton(
        RepositoryRefreshToken, model=RefreshToken, session=session
    )
    repository_user= providers.Singleton(
        RepositoryUser, model=User, session=session
    )
    # endregion

    # region services
    jwt_service = providers.Singleton(
        JWTService,
        repository_refresh_token=repository_refresh_token
    )
    user_service = providers.Singleton(
        UserService,
        repository_user=repository_user
    )
    # endregion


container = Container()
container.init_resources()
container.wire(modules=settings.container_wiring_modules)
