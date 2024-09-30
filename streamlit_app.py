import os,sys
import server
import asyncio
import requests


async def main():
    try:
        print(11111)
        req=requests.get('http://localhost:8888')
        print(req.status_code)
        print('Client closed')
        sys.exit("Exiting the program.")
    except Exception as err:
        print(err)
        server.b()
        os.system('ffmpeg -stream_loop -1 -f lavfi -i anullsrc=r=16000:cl=mono -r 10 -i video.mp4 -c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 20 -b:v 2500k -c:a aac -ar 44100 -threads 0 -bufsize 512k -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/'+os.environ.get('id'))
        asyncio.run(main())
asyncio.run(main())