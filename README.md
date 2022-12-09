# nginxLoadBalancerPythonFlask

This is a simple example of login micro services

To get this working on an Ubuntu desktop system

1. Install docker
2. Install docker-compose
3. docker-compose up
4. docker-compose ps
5. if docker-compose ps shows any running processes, then run docker-compose kill -s SIGKILL
6. For each process that you want to test, run the following commands after opening up a new terminal:

To test 'emailcheck':
    
    1. cd emailcheck
    
    2. python3 app.py
    (open new terminal)
    
    3. curl -d '{"email": "foo@bar"}' -X POST http://localhost:9000/check "Content-type: application/json"
    
    
To test 'passwordcheck':
    
    1. cd passwordcheck
    
    2. python3 app.py
    (open new terminal)
    
    3. curl -d '{"password": "xyZ123"}' -X POST http://localhost:9001/check -H "Content-type: application/json"
    
    
To test 'role':
    
    1. cd role
    
    2. python3 app.py
    (open new terminal)
    
    3. curl -d '{"email": "user_email", "newRole": "role_to_add"}' -X POST http://localhost:9002/addrole -H "Content-type: application/json"
    
    4. curl -d '{"email": "user_email", "remove_role": "role_to_remove"}' -X POST http://localhost:9002/removerole -H "Content-type: application/json"
    

To test 'twofa':
    
    1. cd twofa
    
    2. python3 app.py
    (open new terminal)
    
    3. curl -d '{"name": "first_name", "code": "code_sent_to_phone"}' -X POST http://localhost:9003/authorize -H "Content-type: application/json"
    (Note: code_sent_to_phone can equal one of three values: '3CA6BX', '2FGhiW', or 'FhQ2048j')
