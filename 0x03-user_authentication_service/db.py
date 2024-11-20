from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User

class DB:
    # Existing methods...

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user in the database by arbitrary keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to filter users.

        Returns:
            A User object that matches the filter criteria.

        Raises:
            NoResultFound: If no user matches the filter criteria.
            InvalidRequestError: If invalid query arguments are provided.
        """
        if not kwargs:
            raise InvalidRequestError("No query parameters provided.")

        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except AttributeError:
            raise InvalidRequestError("Invalid query parameters.")
