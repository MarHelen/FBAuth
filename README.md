<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> be3fa6a7a31323f468e726ce99057468b8f27dda
# FBAuth
This is a simple example of using facebook authentication with Django.
python-social-auth module used.

Application has one main view with Facebook authorization, user offered to choose Login or Signup option.

If Login is chosen, but user was not create previously, it redirects to login page back.
The same redirection works for case, when Signup is chosen, but this social account is alreadt assiciate with user in the base.

Authorization process implemented with custom pipline for checking if the user is new or not.

DB is PostgreSQL based.
<<<<<<< HEAD
=======
# README #

This is only the first step, I've done simple login function via python-social-auth. 
User data doesn't store to the db yet, just login-logout. Continue working.
>>>>>>> 5b729cbd3b945f369ac16b66a24388a9439b2ca5
=======
>>>>>>> be3fa6a7a31323f468e726ce99057468b8f27dda
