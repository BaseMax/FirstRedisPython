# FirstRedisPython

## Using

```
flask run
```

## Routes

**Set a new key with value:**
`http://127.0.0.1:5000/set/name/Max`

**Get value of a key:**
`http://127.0.0.1:5000/get/name`

**Set value to a key with expire time:**
`http://127.0.0.1:5000/set/name/Max/5`

**Set expire time on a key:**
`http://127.0.0.1:5000/expire/name/10`

**Delete a key:**
`http://127.0.0.1:5000/delete/name`

**Note:** You do not have to put `/` at the last of the URL, this is not allowed.

### References

- https://redis.io/commands/expire
- https://stackoverflow.com/questions/36000981/storing-keys-with-prefix-that-expire-in-redis
- https://redis-py.readthedocs.io/en/stable/
- https://realpython.com/python-redis/
- https://stackoverflow.com/questions/36000981/storing-keys-with-prefix-that-expire-in-redis
- https://redis-py.readthedocs.io/en/stable/_modules/redis/client.html#Redis.expire
- https://medium.com/@ashok.tankala/how-to-write-your-own-redis-key-expire-listener-in-python-53e531a97f36

© Copyright Max Base, 2021
