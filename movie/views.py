from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import json
import pandas as pd
def movie_(request, date):
	boxoffice = pd.read_csv("kofic_boxoffice_10_07.csv", parse_dates = 'date')
	daily_audi = boxoffice.groupby('date')['audiCnt'].sum()
	target = daily_audi[date]
	# target = "hi hello 안녕"
	data = {'requested date': date, 'total audience': str(target)}
	json_formatted = json.dumps(data)
	return HttpResponse(json_formatted)