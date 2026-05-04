$ docker run --name some-mysql -p 8400:3306 -v /aql-tata/my/custom:/etc/mysql/conf.d -e MYSQL_ROOT_USERNAME=root -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest

 environment:
      MYSQL_ROOT_USERNAME=root
      MYSQL_ROOT_PASSWORD: example


docker build -t pyapp:0.1 .
docker run -d --name pyapp -p 8000:8000 pyapp:0.1

docker compose ap -d
