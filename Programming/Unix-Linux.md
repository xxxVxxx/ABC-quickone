Q: Write a command to send the signal SIGTERM to the “mongo” process.
Answer: ```kill -15 mongod ```
( I am assuming the mongo deamon process here hence using *mongod* but if its a custom process then it would be  ```kill -15 mongo```

Q: Write a command to recursively delete all files named “virus” in the /usr directory.
Answer:
    Assuming that the file is "virus" and does not contain any space or newline my preference is for:
    ```find . -type f -iname "virus" -exec rm -r {}   \+```  ( assuming the server has newer version of findutils supporting the +)
    If there are chances that there might be space in name or newlines then I would do it as follows:
    ```find . -type f -iname "*virus*" -print 0 | xargs -0 rm -r``` 
