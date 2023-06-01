#Importing Modules and Setting up proxies and useragents and cookie
import requests, json, random, time
from bs4 import BeautifulSoup
from pystyle import Colorate, Colors, Add, Center, Write
validReports = 0

c = open("cookies.txt", "r").readlines()
cookies = [i.replace('\n', '') for i in c]

#For Getting Stuff
class Utils:		
	def getCookie():
		cookie = random.choice(cookies)
		return cookie

	def getRequestVerificationToken(cookie):
		requestHTML = requests.get(
			"https://www.roblox.com/build/upload",
			headers = {"referer": "https://roblox.com"},
			cookies = {".ROBLOSECURITY": cookie},
		)
		
		soup = BeautifulSoup(requestHTML.text, "html.parser")
		verifyToken = soup.find("input", {"name" : "__RequestVerificationToken"}).attrs["value"]
		return verifyToken
		
	def getOutput(amount, request):

		if request.status_code == 200:
			Write.Print(f"\n[{amount}] {request.status_code} |      Report Success      | {request.reason}", Colors.green, interval=0)
			global validReports
			validReports += 1
		elif request.status_code == 429:
			Write.Print(f"\n[{amount}] {request.status_code} | Rate Limited  (Cooldown) | {request.reason}", Colors.purple_to_red, interval=0)
			time.sleep(600) #10 Minute Cooldown (in seconds)
		else:
			Write.Print(f"\n[{amount}] {request.status_code} |      Report  Failed      | {request.reason}", Colors.purple_to_red, interval=0)

#Style & Designs
def getBanner():
	bannerText = """
  __   __       __ 
 |__) |__) \_/ |__)  /\  |\ |
 |  \ |__) / \ |__) /~~\ | \| 

     Roblox Mass Reporter 
     1% it acutally bans
       [ cereb#8577 ]
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
	
def ban(victim, amount, reason, cooldown, comments):

	if amount == 0:
		amount = 999999999999999

	id = json.loads(requests.post("https://users.roblox.com/v1/usernames/users", json={
		"usernames": [victim],
		"excludeBannedUsers": "true"
	}).text)["data"][0]["id"]

	Write.Print(f"[>] Victim's User ID: {id}\n", Colors.purple_to_blue, interval=0.0025)

	for i in range(amount):
		time.sleep(cooldown)
		cookie = Utils.getCookie()
		session = requests.Session()		

		xcsrfToken = requests.post("https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie}) #xcsrfToken only works with requests, not session
		xcsrfToken = xcsrfToken.headers["x-csrf-token"]

		session.cookies.update({".ROBLOSECURITY": cookie})
		session.headers.update({"referer": "https://www.roblox.com", "x-csrf-token": xcsrfToken})

		requestHTML 			 = session.get("https://www.roblox.com/build/upload")
		soup 				     = BeautifulSoup(requestHTML.text, "html.parser")
		requestVerificationToken = soup.find("input", {"name" : "__RequestVerificationToken"}).attrs["value"]

		reportRequest = session.post(
			f"https://www.roblox.com/abusereport/userprofile?id={id}",
			data = {
				"__RequestVerificationToken": requestVerificationToken,
				"ReportCategory": reason,
				"Comment": random.choice(comments),
				"Id": id,
				"RedirectUrl": f"https://www.roblox.com/users/{id}/profile,",
				"PartyGuid": "",
				"ConversationId": ""
			}
		)
		
		Utils.getOutput(amount=i, request=reportRequest)

	Write.Print(f"\n\n[>] Finished Mass Report.\n[>] Reports Sent: {amount}\n[>] Valid Reports: {validReports}\n\n", Colors.purple_to_blue, interval=0.0025)
	Write.Input("[>] Enter to Exit...", Colors.purple_to_blue, interval=0.0025)
	
	exit()
