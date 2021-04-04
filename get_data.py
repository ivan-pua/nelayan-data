from facepy import GraphAPI

# Initialize the Graph API with a valid access token (optional,
# but will allow you to do all sorts of fun stuff).
oauth_access_token = "EAADzxzxyrPgBAAabsDnOHXafNwPPJif21RKdVlpNTdwGLfEk0Yn6DLQVgfYgf7hoszYwy5VyUlIVJvduAhqZAWRvZCSIBNzHJf7a4D8B4ZCp4Cmx8LbsMq1OE4IA5XOCvpxz0nB1Nj4bZA5ZBDZBrpMiNWglYrZAB0iVuzkNkJjMQg92AS5sRXnDmrf7Tv26s8ZD"
graph = GraphAPI(oauth_access_token)

# Get my latest posts
posts = graph.get('278134177245821/feed')
