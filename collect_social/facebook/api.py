import facepy

class Facebook(object):
    def __init__(self,app_id=None,app_secret=None):
        auth_token = facepy.utils.get_application_access_token(app_id, app_secret, api_version='2.6')
        self._api = facepy.GraphAPI(auth_token)

    def get_comments(self,page_id):
        kwargs = {
            'path': '/'+str(post_id)+'/comments',
            'limit': 100
        }

        return self._api.get(**kwargs)

    def get_post(self,post_id):
        return self._api.get(**{'path': '/'+str(post_id)})

    def get_posts(self,page_id):
        kwargs = {
            'path': '/'+str(page_id)+'/posts',
            'limit': 5,
            'page': True
        }

        return self._api.get(**kwargs)

    def get_reactions(self,post_id):
        pass

    def get_user(self,user_id):
        return self._api.get(**{'path': '/'+str(user_id)})