#Main File
import RBXBan as RB
from pystyle import Write, Colors

print(RB.getBanner())

reasonDescriptions = {
	#ADD DESCRIPTIONS FOR REPORTS HERE, THE TEXT IN EACH KEY JUST REPRESENTS WHAT THE NUMBER MEANS
    1: ["Inappropriate Language - Profanity & Adult Content"],
	2: ["Asking for or Giving Private Information"],
	3: ["Bullying, Harassment, Discrimination"],
	4: ["Dating"],
	5: ["Exploiting, Cheating, Scamming"],
	6: ["Account Theft - Phishing, Hacking, Trading"],
	7: ["Inappropriate Content - Place, Image, Model"],
	8: ["Real Life Threats & Suicide Threats"],
	9: ["Other rule violation"]
}

try:
	victim   = str(Write.Input("[?] Victim Username: ", Colors.purple_to_blue, interval=0.0025))
	amount   = int(Write.Input("[?] Report Amount (0=inf): ", Colors.purple_to_blue, interval=0.0025))
	reason   = int(Write.Input("[?] Reason for Report (1-9): ", Colors.purple_to_blue, interval=0.0025))
	cooldown = int(Write.Input("[?] Cooldown: ", Colors.purple_to_blue, interval=0.0025))
except Exception as E:
	Write.Print(f"\n[>] Error: {E}", Colors.purple_to_red, interval=0.0025)
	Write.Print("\n[>] Enter to Exit...", Colors.purple_to_red, interval=0.0025)
	input()
	exit()

if amount == 0:
	Write.Print(f"\n[>] Mass Reporting {victim} inf Times for {reason}...\n", Colors.purple_to_blue, interval=0.0025)
	
else:
	Write.Print(f"\n[>] Mass Reporting {victim} {amount} Times for {reason}...\n", Colors.purple_to_blue, interval=0.0025)

RB.report(victim, amount, reason, cooldown, reasonDescriptions[reason])
#gig
