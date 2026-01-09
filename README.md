# Intro
Shlink works great but it only has an admin web interface. There is no simple interface you can provide users to generate URL easily without having to setup API key and then asking user authenticate to the server with API key through the admin web interface.

This web app serves as a simple front-end for Shlink service where anyone can enter a url, the server in turn sends it to your Shlink server via REST API and returns the shortened URL.

Once the URL is shortened, it is displayed on-screen and allows user to copy it to clipboard or generate a QR code (done locally via qrcodejs library)

> [!NOTE]
> I am not a UI/UX designer, AI was used to assist in creating html templates.

# Demo
[Watch demo video](assets/demo.mp4)

# Setup
Note: copy to clipboard option will not work unless you are setup behind reverse proxy/SSL.

You will need to generate an API key from Shlink server.

See documentation for that here: https://shlink.io/documentation/api-docs/authentication/

Clone repo and build docker image.

**The following environmental variables are required!**
- `SHLINK_API_KEY`: Generated from the Shlink server
- `host`: The hostname of your Shlink server
- `tag`: Tag that will be applied to links in the Shlink admin interface to differentiate the use of this API key from your other users/keys.

## Pre-built Image
`docker pull hbuilder/shlink-shortener`

`docker run --name shlink-shortener -p 5000:5000 -e SHLINK_API_KEY=GeneratedFromShlinkDockerContainer -e host=https://YourShlinkServer.com -e tag=shlinkshortener --restart unless-stopped hbuilder/shlink-shortener`

## Build Image
`cd shlink-shortener`

`docker build -t shlink-shortener .`

Compose file:
```
services:
    shlink-shortener:
        container_name: shlink-shortener
        ports:
            - 5000:5000
        environment:
            - SHLINK_API_KEY=GeneratedFromShlinkDockerContainer
            - host=https://YourShlinkServer.com
            - tag=shlinkshortener
        image: shlink-shortener
        restart: unless-stopped
```

