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
        os.system('ffmpeg -stream_loop -1 -re -i video4.mp4 -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://a.rtmp.youtube.com/live2/'+os.environ.get('id'))
        asyncio.run(main())
asyncio.run(main())