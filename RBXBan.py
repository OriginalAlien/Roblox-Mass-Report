#Importing Modules and Setting up proxies and useragents and cookie
import requests, json, lxml, random, time
from bs4 import BeautifulSoup
from pystyle import Colorate, Colors, Add, Center, Write
validReports = 0

c = open("cookies.txt", "r").readlines()
u = open("useragents.txt", "r").readlines()
p = open("proxy.txt", "r").readlines()

cookies    = []
useragents = []
proxies    = []
for i in c:
	cookies.append(i.replace('\n', ''))
	
for i in u:
	useragents.append(i.replace('\n', ''))

for i in p:
	proxies.append(i.replace('\n', ''))

#For Getting Stuff
class Utils:
	def getProxy():
		proxy = random.choice(proxies)
		return proxy
		
	def getUserAgent():
		useragent = random.choice(useragents)
		return useragent
		
	def getCookie():
		cookie = random.choice(cookies)
		return cookie

	def getXCsrf(cookie):
	    xcsrfRequest = requests.post("https://auth.roblox.com/v2/logout",
									 
		headers = {"referer": "https://roblox.com", "User-Agent": Utils.getUserAgent()},
		cookies = {".ROBLOSECURITY": cookie},
		proxies = {"http": Utils.getProxy()})
	    return xcsrfRequest.headers["x-csrf-token"]

	def getRequestVerificationToken(cookie):
		useragent = Utils.getUserAgent()
		requestHTML = requests.get(
			"https://www.roblox.com/build/upload",
			headers = {"referer": "https://roblox.com", "User-Agent": useragent},
			cookies = {".ROBLOSECURITY": cookie},
			proxies = {"http": Utils.getProxy()})
		try:
			soup = BeautifulSoup(requestHTML.text, "lxml")
			verifyToken = soup.find("input", {"name" : "__RequestVerificationToken"}).attrs["value"]
			return verifyToken
			
		except AttributeError as E:
			Write.Print(f"\n\n[>] User-Agent Used: {useragent}", Colors.purple_to_red, interval=0.0025)
			Write.Print(f"\n[>] Error: {E}\n[>] Continuing...\n", Colors.purple_to_red, interval=0.0025)
			pass
			return "Skipped"

	def getOutput(amount, request, proxy, useragent):
		global validReports
		if request.status_code == 200:
			Write.Print(f"\n[{amount}] {request.status_code} |  {proxy}{(25-(len(proxy)))*' '} |   {useragent}", Colors.green, interval=0)
			validReports += 1
		else:
			Write.Print(f"\n[{amount}] {request.status_code} |  {proxy}{(25-(len(proxy)))*' '} |   {useragent}", Colors.purple_to_red, interval=0)
#Style & Designs		
def getBanner():
	bannerText = """
     __   __       __ 
    |__) |__) \_/ |__)  /\  |\ |
    |  \ |__) / \ |__) /~~\ | \|
	
       Roblox Mass Reporter
         [ Dreamer#5114 ] 
"""
	
	bannerLogo = """
         ⣴⣶⣄
       ⣴⣿⣇⡙⢿⣷⣄
     ⣴⣿⣿⣄⠨⣍⡀⠙⣿⡇
   ⣴⣿⣿⡈⣉⠛⢷⣌⣻⣿⠟
 ⣴⠿⢋⣉⠻⢧⡈⢴⣦⣾⠟
 ⢿⣷⣌⠁⣶⢌⣿⣾⠟⢡⣶⣄
  ⠙⢿⣷⣤⣾⠟   ⠙⢿⣷⣄
             ⠙⢿⣷⣄
               ⠙⢿⣷⣄
                 ⠙⢿⣷⣄
                   ⠙⡙⣴⣦⠙
                    ⣌⠛⢋⣴


"""

	banner = Colorate.Vertical(Colors.purple_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner

#Report Function
	
def report(victim, amount, reason, cooldown, descriptions):
	
	if amount == 0:
		amount = 999999999999999
		
	id = json.loads(requests.get(
		f"https://api.roblox.com/users/get-by-username?username={victim}",
		headers={
			"referer": "https://www.roblox.com",
			"User-Agent": Utils.getUserAgent()
		},

		proxies = {
			"http": Utils.getProxy()
		}).text)["Id"]

	Write.Print(f"[>] Victim's User ID: {id}\n", Colors.purple_to_blue, interval=0.0025)

	for i in range(amount):
		time.sleep(cooldown)
		proxy     = Utils.getProxy()
		useragent = Utils.getUserAgent()
		cookie    = Utils.getCookie()
		reportRequest = requests.post(
			f"https://www.roblox.com/abusereport/userprofile?id={id}",
			data = {
				"__RequestVerificationToken": Utils.getRequestVerificationToken(cookie),
				"ReportCategory": reason,
				"Comment": random.choice(descriptions),
				"Id": id,
				"RedirectUrl": f"https://www.roblox.com/users/{id}/profile,",
				"PartyGuid": "",
				"ConversationId": ""
			},
			
			headers = {
				"x-csrf-token": Utils.getXCsrf(cookie),
				"User-Agent": useragent,
				"referer": "https://www.roblox.com"
			},

			proxies = {
				"http": proxy
			},

			cookies = {
				".ROBLOSECURITY": cookie
			}
		)		
		Utils.getOutput(i, reportRequest, proxy, useragent)

	Write.Print(f"\n\n[>] Finished Mass Report.\n[>] Reports Sent: {amount}\n[>] Valid Reports: {validReports}\n\n", Colors.purple_to_blue, interval=0.0025)
	Write.Input("[>] Enter to Exit...", Colors.purple_to_blue, interval=0.0025)
	
	exit()
#gig
