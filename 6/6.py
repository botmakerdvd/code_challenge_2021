#!/usr/bin/python3
#locales must be installed prior to executing this script
#sudo locale-gen ca_ES.UTF-8 cs_CZ.UTF-8 de_DE.UTF-8 da_DK.UTF-8 en_GB.UTF-8 es_ES.UTF-8 fi_FI.UTF-8 fr_FR.UTF-8 is_IS.UTF-8 el_GR.UTF-8 hu_HU.UTF-8 it_IT.UTF-8 nl_NL.UTF-8 vi_VN.UTF-8 pl_PL.UTF-8 ro_RO.UTF-8 ru_RU.UTF-8 sv_SE.UTF-8 sl_SI.UTF-8 sk_SK.UTF-8
locations = {
	"CA": "ca_ES.UTF-8",
	"CZ": "cs_CZ.UTF-8",
	"DE": "de_DE.UTF-8",
	"DK": "da_DK.UTF-8",
	"EN": "en_GB.UTF-8",
	"ES": "es_ES.UTF-8",
	"FI": "fi_FI.UTF-8",
	"FR": "fr_FR.UTF-8",
	"IS": "is_IS.UTF-8",
	"GR": "el_GR.UTF-8",
	"HU": "hu_HU.UTF-8",
	"IT": "it_IT.UTF-8",
	"NL": "nl_NL.UTF-8",
	"VI": "vi_VN.UTF-8",
	"PL": "pl_PL.UTF-8",
	"RO": "ro_RO.UTF-8",
	"RU": "ru_RU.UTF-8",
	"SE": "sv_SE.UTF-8",
	"SI": "sl_SI.UTF-8",
	"SK": "sk_SK.UTF-8"
}
import time
import locale
import datetime
n = int(input())
for case in range(n):
	line=input().split(":")
	date_fromline=line[0].split("-")
	location=line[1]
	#check if location exists
	if location in locations:
		locale.setlocale(locale.LC_TIME, locations[location])
		#check if it starts with year or with day
		if len(date_fromline[0]) == 2:
			#starts with day
			day = date_fromline[0]
			month = date_fromline[1]
			year = date_fromline[2]
		else:
			#starts with year
			day = date_fromline[2]
			month = date_fromline[1]
			year = date_fromline[0]

		try:
			date_read=datetime.date(int(year), int(month), int(day))
			day_name=date_read.strftime("%A").lower()
			print("Case #"+str(case+1)+": "+day_name)
		except ValueError:
			print("Case #"+str(case+1)+": INVALID_DATE")	
	else:
			print("Case #"+str(case+1)+": INVALID_LANGUAGE")