# webserver
Veloxity Central Web Server (This is a PROD REPO)

# Database structure:
Test Schema / User table =
=> 
username,"",varchar(255),true,"",NORMAL
name,"",varchar(255),false,"",NORMAL
password,"",varchar(255),false,"",NORMAL
email,"",varchar(255),false,"",NORMAL
employee,"",tinyint(1),false,"",NORMAL
admin,"",tinyint(1),false,"",NORMAL
locked,"",tinyint(1),false,"",NORMAL


Data Schema / {user.id} =
=>
timestamp,"",datetime,false,"",NORMAL
expense,"","decimal(10,2)",false,"",NORMAL
revenue,"","decimal(10,2)",false,"",NORMAL
