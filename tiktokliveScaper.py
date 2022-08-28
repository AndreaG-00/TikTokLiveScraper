from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent, FollowEvent, ViewerCountUpdateEvent

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="alexim801", **(
        {
            "enable_extended_gift_info": True
        }
    )
)

@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"{event.user.uniqueId} -> {event.comment}")


@client.on("gift")
async def on_gift(event: GiftEvent):
    print(f"{event.user.uniqueId} sent a {event.gift.gift_id}!")
    for giftInfo in client.available_gifts:
        if giftInfo["id"] == event.gift.gift_id:
            print(f"Name: {giftInfo['name']} Image: {giftInfo['image']['url_list'][0]} Diamond Amount: {giftInfo['diamond_count']}")


@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.uniqueId} has liked the stream {event.likeCount} times, there is now {event.totalLikeCount} totals likes!")


@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.uniqueId} followed the streamer")


@client.on("share")
async def on_share(event: ShareEvent):
    print(f"{event.user.uniqueId} shared the streamer")


@client.on("viewer_count_update")
async def on_connect(event: ViewerCountUpdateEvent):
    print("Received a new viewer count:", event.viewerCount)


if __name__ == '__main__':
    client.run()

