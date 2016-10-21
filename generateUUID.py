
import uuid
import hashlib

def get_uuid(number):

	# add_hash = hashlib.md5()
	uu_id = str(uuid.uuid4())
	# uu_id = add_hash.update(uu_id)
	# uu_id = uu_id.hexdigest()

	uuid_list = []

	for i in xrange(number):
		uuid_list.append(uu_id)

	return uuid_list

def get_encode(text, number):
	add_hash = hashlib.md5()
	add_hash.update(text)
	return add_hash.hexdigest()
