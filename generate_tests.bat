@echo off
curl.exe -s -X POST http://127.0.0.1:5000/accounts -H "Content-Type: application/json" -d "{\"name\":\"John Doe\",\"email\":\"john@email.com\"}" > rest-create-done.txt
curl.exe -s -X GET http://127.0.0.1:5000/accounts > rest-list-done.txt
curl.exe -s -X GET http://127.0.0.1:5000/accounts/1 > rest-read-done.txt
curl.exe -s -X PUT http://127.0.0.1:5000/accounts/1 -H "Content-Type: application/json" -d "{\"name\":\"John Doe\",\"email\":\"john@email.com\",\"phone_number\":\"555-1234\"}" > rest-update-done.txt
curl.exe -s -X DELETE http://127.0.0.1:5000/accounts/1 > rest-delete-done.txt
