import redis
from flask import Flask

# redis
redis_cache = redis.Redis(host='localhost', port=6379, db=0, password="")

# flask app
app = Flask(__name__)

# set with expire
@app.route('/set/<string:key>/<string:value>/<int:expired>')
def set_with_expire(key, value, expired):
	if redis_cache.exists(key):
		pass
	else:
		redis_cache.set(key, value, ex=expired)
	return "OK"

# set
@app.route('/set/<string:key>/<string:value>')
def set(key, value):
	if redis_cache.exists(key):
		pass
	else:
		redis_cache.set(key, value)
	return "OK"

# get
@app.route('/get/<string:key>')
def get(key):
	if redis_cache.exists(key):
		return redis_cache.get(key)
	else:
		return f"{key} is not exists"

# expire
@app.route('/expire/<string:key>/<int:expired>')
def expire(key, expired):
	if redis_cache.exists(key):
		# ref: https://realpython.com/python-redis/
		# ref: https://redis-py.readthedocs.io/en/stable/_modules/redis/client.html#Redis.expire
		# redis_cache.expire(key, timedelta(seconds=expired))
		print(f"Set expire {key} after {expired} seconds!")
		redis_cache.expire(key, expired)
		return "Done, expire set!"
	else:
		return f"{key} is not exists, please set this at the first"


if __name__ == "__main__":
	app.run("127.0.0.1", port="5000", debug=True)
