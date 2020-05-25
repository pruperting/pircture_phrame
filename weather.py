import requests
import feedparser

#code to base weather on
#d = feedparser.parse('https://weather-broker-cdn.api.bbci.co.uk/en/observation/rss/bs16')
#entry = d.entries[0]
#windir = entry.summary.split("Wind Direction: ", 1)[-1].split(",")[0]
#windspeed = float(entry.summary.split("Wind Speed: ", 1)[-1].split("mph,")[0])
#print(windir)


d = feedparser.parse('https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/bs16')
#today/tonight
entry = d.entries[0]
#windir = entry.summary.split("Wind Direction: ", 1)[-1].split(",")[0]
#print("The 0 dic")
#print(windir)
fore1 = d['entries'][0]['title']
fore2 = d['entries'][1]['title']
fore3 = d['entries'][2]['title']
fore1cond = fore1.split(",", 1)[0]
fore1min = fore1.split("Minimum Temperature: ", 1)[-1].split(" ")[0]
fore1max = fore1.split("Maximum Temperature: ", 1)[-1].split(" ")[0]
fore1overall = "%s. Min: %s Max: %s" % (fore1cond, fore1min, fore1max)
fore2cond = fore2.split(",", 1)[0]
fore2min = fore2.split("Minimum Temperature: ", 1)[-1].split(" ")[0]
fore2max = fore2.split("Maximum Temperature: ", 1)[-1].split(" ")[0]
fore2overall = "%s. Min: %s Max: %s" % (fore2cond, fore2min, fore2max)
fore3cond = fore3.split(",", 1)[0]
fore3min = fore3.split("Minimum Temperature: ", 1)[-1].split(" ")[0]
fore3max = fore3.split("Maximum Temperature: ", 1)[-1].split(" ")[0]
fore3overall = "%s. Min: %s Max: %s" % (fore3cond, fore3min, fore3max)
text_file = open("/home/pi/fore1.txt", "w")
n = text_file.write(fore1overall.encode("utf-8", errors="ignore"))
text_file.close()
text_file = open("/home/pi/fore2.txt", "w")
n = text_file.write(fore2overall.encode("utf-8", errors="ignore"))
text_file.close()
text_file = open("/home/pi/fore3.txt", "w")
n = text_file.write(fore3overall.encode("utf-8", errors="ignore"))
text_file.close()


##no  more from here
#tomorrow
#entry1 = d.entries[1]
#print("The 1 dic")
#print(entry1)
#the following day
#entry2 = d.entries[2]
#print("The 2 dic")
#print(entry2)

