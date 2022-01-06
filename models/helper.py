import json

with open('./data/records_existing.json') as f:
  objects = json.load(f)

def is_valid(obj):
	if obj.keys() >= {"uid", "pid", "w"}:
		return True
	return False

def form_key(obj):
	return "%s:%s" % (obj["uid"],obj["pid"])

class Helper:
	def verify_records(records):
		ary = []
		for sub_arry in records:
			if is_valid(sub_arry):
				ary.append(sub_arry)
			else:
				raise Exception("Sub array must have exactly 3 elements")
		return ary

	def existing_objects(name):
			if name in objects:
				return objects[name]
			else:
				raise Exception("No records for", name)

	def validate_new_objects(new_records, existing_records):
		for object in new_records:
			key = form_key(object)
			if key not in existing_records:
				try:
					if object["pid"].startswith('_'):
						raise Exception("Record is malformed")
					else:
						result = Result.objects.filter(Q(barcode=pid) | Q(oid=pid)).latest('created')
				except:
					raise Exception("Can't find result [%s] for w [%s]", 'pid', 'w')
					continue
			else:
				print(key, 'good')
