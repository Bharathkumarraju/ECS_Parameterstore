# ECS_Parameterstore
AWS ECS with aws system Parameter stores

### Application can be accessed here

http://AWSEcsApplicationLoadbalancer-2024742083.ap-southeast-1.elb.amazonaws.com

### Environment varibales can be used as here

![aws_system_parameterstore](variables.png)

### Environment Variables

To access the each parameter inside the container definition use ARN as below for each environment.

The beauty of this parameter store is, it is hierarchical means you can give permission based on `/app` level `/app/miyazaki` level or `/app/miyazaki/<parameter>` level

That means we cab give permission to certain users to access certain hierarchy etc...
```
lets say you have /dev/app/<app1>
                  /stage/app/<app2>
                  /prod/app/<app3> 
 we can restrict users not to access prod app parameter variables etc...
```
In order to access the parameter store variable we have to use ARN's like below.

SSM ARN - arn:aws:ssm:ap-southeast-1:172586632398:parameter/<name>


- /app/miyazaki/DBHOST : XXXXXXXXX  -> arn:aws:ssm:ap-southeast-1:172586632398:parameter/app/miyazaki/DBHOST

- /app/miyazaki/DBPORT : 3306 -> arn:aws:ssm:ap-southeast-1:172586632398:parameter/app/miyazaki/DBPORT

- /app/miyazaki/DBPWD : XXXXXX -> arn:aws:ssm:ap-southeast-1:172586632398:parameter/app/miyazaki/DBPWD

- /app/miyazaki/DBUSER : XXXXX -> arn:aws:ssm:ap-southeast-1:172586632398:parameter/app/miyazaki/DBUSER

- /app/miyazaki/DATABASE : XXXXX  -> arn:aws:ssm:ap-southeast-1:172586632398:parameter/app/miyazaki/DATABASE

### use above values in contianer defintions as below that are defined in Parameter store

![Contianer_Definiton](container_definition.png)