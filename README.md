# impersonator

### Update: an instance of this bot that I used to run is now down, because the feature has been integrated into [AndewBot](https://github.com/ajlee2006/discord-andewbot). However, I shall leave this code here for anyone who wants to run it on their own.

A bot that uses webhooks to pretend to be someone else, matching their username and profile picture. Big drawbacks - there is always "BOT" next to the username, and the colour of the username cannot be matched.

## Usage
Multi-word fields must be enclosed with single or double quotes.
### Impersonating with custom nickname 
```
impersonate [nickname] [optional avatar image url] [message]
```
### Impersonating a user
```
impersonate [@mention] [message]
```
### Sending embeds
Replace `[message]` with `embed [title] [description] [optional colour (rgb int)]`
### Auto-delete message
Append `delete` at the end of a message.
