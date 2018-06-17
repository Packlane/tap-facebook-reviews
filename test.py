import requests

ACCESS_TOKEN = 'EAACEdEose0cBAPUnMZAwezDcvfO8haKa1BZAOHsgOJZBa6i47nOS414VmHRgZBDxD04McpHZArtmP5r2zmxGINlYEras77cpr3UrjdVbLTbb2ZA3l2U12e3OmDTSARrQumnPOTw0A9BAzuqBK7mGEZCkoFpVgGM6v14BH7aBh9xEVfV0wsdPzqMfvILTzaZCa8TgwDmajNKajZAgReuA5u9xD'


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

    out = []

    for rating in r.json().get('data', []):
        user_id = rating['reviewer']['id']
        avatar = get_user_avatar(user_id)
        new_rating = rating['avatar_url'] = get_user_avatar(user_id)
        out.append({rating['reviewer']['id']: new_rating})

    return out


if __name__ == '__main__':
    print(get_facebook_ratings())
