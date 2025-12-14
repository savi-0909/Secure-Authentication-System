1. Flash Running
   PS C:\Users\DELL\OneDrive\Desktop\SAS> python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 845-545-621

2. Register sucess output
   PS C:\Users\DELL\OneDrive\Desktop\SAS> Invoke-RestMethod `
>> -Uri http://127.0.0.1:5000/register `
>> -Method POST `
>> -Body '{"username":"savitha","password":"12345"}' `
>> -ContentType "application/json"
>> 

message
-------
User registered successfully

3. Login token output
   PS C:\Users\DELL\OneDrive\Desktop\SAS> Invoke-RestMethod `
>> -Uri http://127.0.0.1:5000/login `
>> -Method POST `
>> -Body '{"username":"savitha","password":"12345"}' `
>> -ContentType "application/json"
>>

token
-----
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoic2F2aXRoYSIsImV4cCI6MTc2NTcxMTI2MX0.98d5JYjRm4gjTDIKilBVv621oq-OtU2XcT5jcv5TQ4A
