# FBAuth
This is a simple example of using facebook authentication with Django.
python-social-auth module used.

Application has one main view with Facebook authorization, user offered to choose Login or Signup option.

If Login is chosen, but user was not create previously, it redirects to login page back.
The same redirection works for case, when Signup is chosen, but this social account is alreadt assiciate with user in the base.

Authorization process implemented with custom pipline for checking if the user is new or not.

DB is PostgreSQL based.
