# telegram-poll-vote
will vote in telegram poll of a telegram group. 




Getting Started
---------------------------------------------------------------------------------------------------------------------

    Configuration of .env file:

        1. Copy env.example to .env file.

        2. You need to get APP_ID and APP_HASH from registering  [here](https://my.telegram.org/auth)

        3. Assign poll group id to GROUP_ID

        4. Assign mobile number to PHONE with proper country code.



    1. clone the repo:

        git clone git@github.com:Shipu12345/telegram-poll-vote.git
    

    2. For only at the First time:
        
        a) At first need to login in the telegram.
            
            ! ./bin/deploy-login.sh
        
        b) Then Enter into docker container.

            ! docker exec -it telegram-poll-voter bash
        
        c) Then Run the login.py file.

            ! python src/login.py
        
        d) A code will be sent to your telegram; enter the code into login.py program console. After that simply exit from the container with the command:  ! exit

        e) Down the docker container.

            ! ./bin/down-login.sh
        
    
    3. After that, every time you can run the docker container with:

        ! ./bin/deploy.sh


Further Instractions:

    If you need to re-login in any probable case, delete docker-python-telegram folder from tmp, start from the begining.

        ! sudo rm -rf /tmp/docker-python-telegram










