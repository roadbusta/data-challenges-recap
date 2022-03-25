# pylint: disable=missing-docstring

# import os

# def start():
#     """returns the right message"""
#     try:
#         return "Starting in " + os.environ['FLASK_ENV'] + " mode..."

#     except KeyError:
#         return "Starting in production mode..."




# if __name__ == "__main__":
#     print(start())


# import os


def start():
    """returns the right message"""
    # $CHALLENGIFY_BEGIN
    env = os.getenv('FLASK_ENV')
    if env:
        return f"Starting in {env} mode..."
    return "Starting in production mode..."
    # $CHALLENGIFY_END


if __name__ == "__main__":
    print(start())

import os


def start():
    env = os.environ['FLASK_ENV']
    if env:
        return f"Starting in {env} mode..."
    else:
        return "Starting in production mode..."


if __name__ == "__main__":
    print(start())
