This project is built using django rest framework.
In this project we created two microservices service1 and service2.
Service1 is used to authenticate the user by Tokens and Admin with a static key.
In Service2 we created few auctions with different fileds. 
once admin is authenticated he can perform operations like creation,retrive user  on users as well auctions.
once user is authenticated then they can see all the ongoing auctions and can bid(in progress).

# Service1 Endpoints

register/ = after user will enter their details, they will obtain a token and can see all the ongoing auctions.
sample/ = Only authenticated admin can access this endpoint, this end point is used to authenticate the admin. After authentication they can view all user details and create user.
addauction/ = Only authenticated admin can access this endpoint. They can view as well as create(in progress) new auction.

# Service2 Endpoints

auction/ = this endpoint will return all ongoing auction.
auction/add/ = this endpoint will let admin add new auction.
