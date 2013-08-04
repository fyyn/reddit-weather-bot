import pywapi
import praw
import time
print "Running"
r = praw.Reddit('Weather Forecast Bot v 0.1 by /u/fyyn')

r.login('bottomatic', 'testbot123')

already_done = ['cb56h8f']

while True:
    print "While loop"
    subreddit = r.get_subreddit('fyyntest')
    scanned_comments = subreddit.get_comments()
    for comment in scanned_comments:
        if "Forecast please" in comment.body and comment.id not in already_done:
            try:
                city = comment.body.replace("Forecast please. City: ", "")
                print str(city)
                fore = pywapi.get_weather_from_yahoo(str(city), units='metric')
                print fore
                fore_message = "The Temperature is " + fore['condition']['temp'] + "in" + city
                comment.reply(fore_message)
                already_done.append(comment.id)
                print already_done
            except:
                fore = pywapi.get_weather_from_yahoo(str(city), units='metric')
                names = pywapi.get_location_ids(city)
                comment.reply("Which location did you mean? Please reformulate your request with the correct City code:")
                citylist = ""
                for thing in names:
                    citylist += "City: " + str(names[thing]) + "Code: " + str(thing) + ","
                comment.reply(citylist)
                already_done.append(comment.id)

    time.sleep(100)


