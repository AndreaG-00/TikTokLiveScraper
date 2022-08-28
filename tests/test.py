from TikTokLive import TikTokLiveClient

client = TikTokLiveClient(unique_id="livanessa_montero")

@client.on("follow")
async def on_follow(event):
    print(f"{event.user.uniqueId} followed the streamer")

if __name__ == '__main__':
    client.run()