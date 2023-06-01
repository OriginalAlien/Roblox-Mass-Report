#Main File
import RBXBan as RB
from pystyle import Write, Colors

print(RB.getBanner())

reasons = {
	#Add your comments in square brackets between quotes, seperated by comma. (e.g ["he is scammer", "scammed 10k bobux"])
    	1: {"reason": "Inappropriate Language - Profanity & Adult Content", "comments": ["he said slurs"]},
	2: {"reason": "Asking for or Giving Private Information",           "comments": ["he asked for my password"]},
	3: {"reason": "Bullying, Harassment, Discrimination",               "comments": ["he bullied me"]},
	4: {"reason": "Dating",                                             "comments": ["hes oding"]},
	5: {"reason": "Exploiting, Cheating, Scamming",                     "comments": ["he is scammer"]},
	6: {"reason": "Account Theft - Phishing, Hacking, Trading",         "comments": ["he hacked my account"]},
	7: {"reason": "Inappropriate Content - Place, Image, Model",        "comments": ["he uploaded hentai"]},
	8: {"reason": "Real Life Threats & Suicide Threats",                "comments": ["he threatened me"]},
	9: {"reason": "Other rule violation",                               "comments": ["he is doing offsite rule violations"]}
}

victim   = Write.Input("[?] Victim Username: ", Colors.purple_to_blue, interval=0.0025)
amount   = int(Write.Input("[?] Report Amount (0=inf): ", Colors.purple_to_blue, interval=0.0025))
reason   = int(Write.Input("[?] Reason for Report (1-9): ", Colors.purple_to_blue, interval=0.0025))
cooldown = int(Write.Input("[?] Cooldown: ", Colors.purple_to_blue, interval=0.0025))

if amount == 0:
	Write.Print(f"\n[>] Mass Reporting {victim} inf Times for {reason}...\n", Colors.purple_to_blue, interval=0.0025)
else:
	Write.Print(f"\n[>] Mass Reporting {victim} {amount} Times for {reason}...\n", Colors.purple_to_blue, interval=0.0025)

RB.ban(victim, amount, reason, cooldown, reasons[reason]["comments"])
