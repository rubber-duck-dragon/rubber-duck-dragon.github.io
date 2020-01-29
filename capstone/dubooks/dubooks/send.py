import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgwMjM1NjEwLCJqdGkiOiI3NjhlOWQ5MjNiZWY0MmEzODAyMDVjNzM2ZTE0MjliNyIsInVzZXJfaWQiOjF9.6rw71ronWtL25s6TbwUMX3Pm87hiz_61eRcad1jmVB4'

r = request.get('http://127.0.0.1:8000/users', headers=headers)

print(r.username)