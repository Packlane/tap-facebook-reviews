# Tap Facebook

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

---

Copyright &copy; 2018 Stitch
