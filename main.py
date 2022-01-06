from models.helper import *

def valid_new_objects(records, name, send=False, code=None):
	incoming_objects = Helper.verify_records(records)
	existing_objects = Helper.existing_objects(name)
	return Helper.validate_new_objects(incoming_objects, existing_objects)

class Test:
	with open('./data/records_test.json') as f:
	  records = json.load(f)['Good']

	valid_new_objects(records, "Bob")
