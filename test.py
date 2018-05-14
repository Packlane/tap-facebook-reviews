import requests

ACCESS_TOKEN = 'EAACEdEose0cBAGdLyurTx1wx9fMoNAZAvRqgr1sHy7fAMUsgjwDQR1AdIK9RgxygWI6kaGz8ToYUPjxolVAvjnBApuF3Pgwe9W9Of9L1AMf1O412M1dha9DK0aXZANyHlu53omxbDX6SnxZAX6LGOZAigeP0iY512SbiYqcZC9ZBSP9O7Q7Xo2OGZCKKCObu14ZD'


def get_user_avatar(user_id):
    """
    Retrieves a URL to the user's avatar, so that we can save it.

    :param str user_id: The user to retrieve the avatar for
    :rtype: str
    :returns: A URL to the user's avatar
    """
    r = requests.get(
        'https://graph.facebook.com/v3.0/{0}/picture?access_token={1}&redirect=0'.format(
            user_id,
            ACCESS_TOKEN,
        )
    )

    return r.json()['data']['url']

def get_facebook_ratings(limit=25, offset=0):
    """
    Fetches Facebook ratings.

    :param int limit: How many results to fetch
    :param int offset: How many results to paginate over before returning results.
    :returns:
    """
    r = requests.get(
        'https://graph.facebook.com/v3.0/Packlane/ratings?access_token={1}'.format(
            limit,
            ACCESS_TOKEN,
        )
    )

    for rating in r.json():
        user_id = rating['reviewer']['id']
        rating['reviewer']['avatar_url'] = get_user_avatar(user_id)

    return r.json()


if __name__ == '__main__':
    get_facebook_ratings()
