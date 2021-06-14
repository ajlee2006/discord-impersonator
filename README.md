# impersonator

A bot that uses webhooks to pretend to be someone else, matching their username and profile picture. Big drawback - there is always "BOT" next to the username.

An instance is currently running off this source code on Heroku. **[Invite link](https://discord.com/api/oauth2/authorize?client_id=853267048679211009&permissions=2751982656&scope=bot)**

### Usage
Multi-word fields must be enclosed with single or double quotes.
#### Impersonating with custom nickname 
```
impersonate [nickname] [optional avatar image url] [message]
```
#### Impersonating a user
```
impersonate [@mention] [message]
```
#### Sending embeds
Replace `[message]` with `embed [title] [description] [optional colour (rgb int)]`
#### Auto-delete message
Append `delete` at the end of a message.
