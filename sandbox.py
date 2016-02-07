import fitbit
import auth

client = fitbit.Fitbit(auth.CONSUMER_KEY, auth.CONSUMER_SECRET, oauth2=True,
    access_token=auth.ACCESS_TOKEN, refresh_token=auth.REFRESH_TOKEN)


