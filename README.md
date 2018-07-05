# Tap Facebook Reviews

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [Facebook](https://developers.facebook.com/docs/graph-api/)
- Extracts the following resources:
  - [User Profile Picture](https://developers.facebook.com/docs/graph-api/reference/user/picture/)
  - [Page Ratings/Reviews](https://developers.facebook.com/docs/graph-api/reference/page/ratings/)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## Connecting

### Requirements

The only required component will be a facebook API key specifically for a page.

More specifically, you will need to visit: https://developers.facebook.com/tools/explorer/

### Setup

```bash
$ mkvirtualenv -p python3 tap-facebook-reviews
$ pip install tap-facebook-reviews
```

```bash
$ git clone git@github.com:singer-io/tap-facebook-reviews.git
$ cd tap-facecbook-reviews
$ mkvirtualenv -p python3 tap-facebook-reviews
$ cd tap-facebook-reviews
$ pip install .
```

### Running it

You will need to create a `config.json` file that looks like the following:

```bash
{
  "facebook_access_token": "<access_token>",
  "start_date": "2017-01-01T00:00:00Z"
}
```

---

Copyright &copy; 2018 Stitch
