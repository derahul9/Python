import requests
import json

username = ''

token = '1b8f43f38925b82b23a643364fadf51392c04f74'

repos_url = 'https://api.github.com/repos/derahul9/Python'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
repos = json.loads(gh_session.get(repos_url).text)

# print the repo names
for item in repos.items():
    print (item)

'''
API Theory
Protocols: REST, SOAP, RPC, REST being the most popular choice
REST (short for Representational State Transfer) is a web services API. REST APIs are a key part of modern web applications, including Netflix, Uber, Amazon, and 
many others. For an API to be RESTful, it must adhere to the following rules:

Stateless— REST API is stateless in nature, Client-Server Architecture
Uniform Interface— client and server should communicate with one another via HTTP (HyperText Transfer Protocol) using URIs (Unique Resource Identifiers), 
CRUD (Create, Read, Update, Delete), and JSON (JavaScript Object Notation) conventions.
Client-Server— The client and server should be independent of each other. The changes you make on the server shouldn’t affect the client and vice versa.
Cache— The client should cache the responses as this improves the user experience by making them faster and more efficient.
Layered— The API should support a layered architecture, with each layer contributing to a clear hierarchy. Each layer should be loosely coupled and allow for 
encapsulation.

API Authentication: Basic Auth and OAuth-
-----------------------------------------
HTTP Basic Auth-
-----------------
HTTP Basic Auth is a simple method that creates a username and password style authentication for HTTP requests. HTTP Basic Auth is a standardized way to send 
credentials. The header always looks the same, and the components are easy to implement. It’s easy to use and might be a decent authentication for applications 
in server-to-server environments.

Benefits
HTTP Basic Auth is a standardized way to send credentials. The header always looks the same, and the components are easy to implement. It’s easy to use and might 
be a decent authentication for applications in server-to-server environments.

Drawbacks
When a user is authenticated, the application is required to collect the password. From the user perspective, it’s not possible to know what the app does with the 
password. The application will gain full access to the account, and there’s no other way for the user to revoke the access than to change the password. Passwords 
are long-lived tokens, and if an attacker would get a hold of a password, it will likely go unnoticed. When used to authenticate the user, multi-factor 
authentication is not possible.

Token-based Authentication Using OAuth 2.0-
---------------------------------------------
The basic idea behind Token's are - say you're a user accessing the Rumba application using your username/password such that user has the access to the Rumba
application. If you want to allow a 3-rd party application to collect your data from Rumba for analysis you can either hand them over your username/password 
which is not secure as they would basially have access to your account or you could authorize a token to that application specifying the desired access to the
Rumba application. They can use the token to access the information without having to give them your credentials.

https://nordicapis.com/the-difference-between-http-auth-api-keys-and-oauth/

The Anatomy Of A Request:
----------------------------
The endpoint
The method
The headers
The data (or body)

The endpoint (or route) is the url you request for. It follows this structure: root-endpoint/?

The Method -The method is the type of request you send to the server. You can choose from these five types below:
GET - This request is used to get a resource from a server. If you perform a `GET` request, the server looks for the data you requested and sends it back to you. 
In other words, a `GET` request performs a `READ` operation. This is the default request method.
POST - This request is used to create a new resource on a server. If you perform a `POST` request, the server creates a new entry in the database and tells you 
whether the creation is successful. In other words, a `POST` request performs an `CREATE` operation.
PUT and PATCH - These two requests are used to update a resource on a server. If you perform a `PUT` or `PATCH` request, the server updates an entry in the database and 
tells you whether the update is successful. In other words, a `PUT` or `PATCH` request performs an `UPDATE` operation.
DELETE - This request is used to delete a resource from a server. If you perform a `DELETE` request, the server deletes an entry in the database and tells you 
whether the deletion is successful. In other words, a `DELETE` request performs a `DELETE` operation.

HTTP Header types:
------------------
Headers can be grouped according to their contexts:

General headers apply to both requests and responses, but with no relation to the data transmitted in the body.
Request headers contain more information about the resource to be fetched, or about the client requesting the resource.
Response headers hold additional information about the response, like its location or about the server providing it.

Authentication
Caching
Client hints
Conditionals
Connection management
Content negotiation
Controls
Cookies
Proxies
Redirects
Request context:
----------------
From-Contains an Internet email address for a human user who controls the requesting user agent.
Host-Specifies the domain name of the server (for virtual hosting), and (optionally) the TCP port number on which the server is listening.
Referer-The address of the previous web page from which a link to the currently requested page was followed.
Referrer-Policy-Governs which referrer information sent in the Referer header should be included with requests made.
User-Agent-Contains a characteristic string that allows the network protocol peers to identify the application type, operating system, software vendor or software version of the requesting software user agent. See also the Firefox user agent string reference.

Response context:
-----------------
Allow-Lists the set of HTTP request methods supported by a resource.
Server-Contains information about the software used by the origin server to handle the request.
'''