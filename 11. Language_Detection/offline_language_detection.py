# $ sudo pip install langdetect

from langdetect import detect
detect("War doesn't show who's right, just who's left.")
#'en'
detect("Ein, zwei, drei, vier")
#'de'
detect("la vita e bella!")
#'it'
