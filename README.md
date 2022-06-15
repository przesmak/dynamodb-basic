# dynamodb-basic
Basic python setup for dynamoDB


- command to check created tables: 
`aws dynamodb list-tables --endpoint-url http://localhost:4566`
- command to check content inside Movies tables" 
`aws dynamodb scan --table-name Movies --endpoint-url http://localhost:4566`