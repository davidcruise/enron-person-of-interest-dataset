def removeOutlier(data_dict):

	del data_dict['LOCKHART EUGENE E']

	data_dict['BELFER ROBERT'] = {
	        'bonus': 'NaN',
	        'deferral_payments': 'NaN',
	        'deferred_income': -102500,
	        'director_fees': 102500,
	        'email_address': 'NaN',
	        'exercised_stock_options': 'NaN',
	        'expenses': 3285,
	        'from_messages': 'NaN',
	        'from_poi_to_this_person': 'NaN',
	        'from_this_person_to_poi': 'NaN',
	        'loan_advances': 'NaN',
	        'long_term_incentive': 'NaN',
	        'other': 'NaN',
	        'poi': False,
	        'restricted_stock': -44093,
	        'restricted_stock_deferred': 44093,
	        'salary': 'NaN',
	        'shared_receipt_with_poi': 'NaN',
	        'to_messages': 'NaN',
	        'total_payments': 3285,
	        'total_stock_value': 'NaN'
	}

	data_dict['BHATNAGAR SANJAY'] = {
	        'bonus': 'NaN',
	        'deferral_payments': 'NaN',
	        'deferred_income': 'NaN',
	        'director_fees': 'NaN',
	        'email_address': 'sanjay.bhatnagar@enron.com',
	        'exercised_stock_options': 15456290,
	        'expenses': 137864,
	        'from_messages': 29,
	        'from_poi_to_this_person': 0,
	        'from_this_person_to_poi': 1,
	        'loan_advances': 'NaN',
	        'long_term_incentive': 'NaN',
	        'other': 'NaN',
	        'poi': False,
	        'restricted_stock': 2604490,
	        'restricted_stock_deferred': -2604490,
	        'salary': 'NaN',
	        'shared_receipt_with_poi': 463,
	        'to_messages': 523,
	        'total_payments': 137864,
	        'total_stock_value': 15456290
	}    
	    
	    
	    
	import numpy as np
	import pandas as pd 
	df = pd.DataFrame.from_dict(data_dict, orient = 'index')
	df = df.drop(columns = "email_address")
	df = df.replace('NaN', np.nan)

	df = df.drop(['TOTAL', 'LAVORATO JOHN J', 'MCMAHON JEFFREY', 'FREVERT MARK A', 'LAVORATO JOHN J', 'WHALLEY LAWRENCE G', 'BAXTER JOHN C'],0)
	df = df.fillna(0)
	data_dict = df.to_dict(orient='index')
	
	return data_dict