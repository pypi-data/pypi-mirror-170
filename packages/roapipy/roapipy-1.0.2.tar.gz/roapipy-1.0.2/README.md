# roapipy Documentation
roapipy - A python wrapper for the roblox api
## class Client()
For usage of roapipy, upon importing, you need to define your client - this will be your main mode of using the wrapper. Popular names for its variable are **robloxclient, roclient & client** for the purpose of simplicity, this documentation will be using **roclient**.
If you are unsure on how to get your roblosecurity cookie, use the following [tutorial](https://ro.py.jmk.gg/dev/roblosecurity/) (link from popular roblox python api wrapper, the purpose of this wrapper is to be a simpler version of it).
```py
roclient = roapipy.Client(“.roblosecurity”)
```
**Parameters:**
* **rosec** (Optional[str]) - roblosecurity code (only required if using authenticated commands like accepting users into a group or setting shout)
### class User()
Used to interact with users
#### Info(id)
Returns information on the user with the given id
**Parameters:**
* **id** ( int ) - id of the user you wish to get information on-     
#### Activity(id)
Returns the activity of the user with the given id
**Parameters:**
* **id** ( int ) - id of the user you wish to get the activity of
#### Groups(id)
Returns the groups the user with the given id is in
**Parameters:**
* **id** ( int ) - id of the user you wish to get the groups of
### class Group()
Used to interact with groups
#### Info(id)
Returns information on the group with the given id
**Parameters:**
* **id** ( int ) - id of the group you wish to get the information on
#### Roles(id)
Returns the roles of the group with the given id
**Parameters:**
* **id** ( int ) - id of the group you wish to get the roles of
#### Shout(groupid, shout)
Sets the shout of the group with the given id
==**A [roblosecurity](https://ro.py.jmk.gg/dev/roblosecurity/) is required within the Client’s parameters for this command to work**==
**Parameters:**
* **groupid** ( int ) - id of the group you wish to set the shout of
* **shout** ( str ) - what the shout should be set to
#### Accept(groupid, userid)
Accepts the user with the given id into the group with the given id
==**A [roblosecurity](https://ro.py.jmk.gg/dev/roblosecurity/) is required within the Client’s parameters for this command to work**==
**Parameters:**
* **groupid** ( int ) - id of the group you wish to accept the user into
* **userid** ( int ) - id of the user you wish to accept into the group
#### Rank(groupid, userid, rank)
Rank the user with the given id into the group with the given id to the given rank
==**A [roblosecurity](https://ro.py.jmk.gg/dev/roblosecurity/) is required within the Client’s parameters for this command to work**==
**Parameters:**
* **groupid** ( int ) - id of the group you wish to rank the user in
* **userid** ( int ) - id of the user you wish to rank
* **rank** ( Any[int(Unique ID/Group ID (1-255)), str(rank name)] ) - the rank you wish to set the user to
#### Exile(groupid, userid)
Exiles the user with the given id from the group with the given id
==**A [roblosecurity](https://ro.py.jmk.gg/dev/roblosecurity/) is required within the Client’s parameters for this command to work**==
**Parameters:**
* **groupid** ( int ) - id of the group you wish to exile the user from
* **userid** ( int ) - id of the user you wish to exile from the group
## Credits
### jmk
Creator of original roblox api wrapper/inspiration (ropy)
[Github](https://github.com/jmkd3v) [Twitter](https://twitter.com/jmkdev)