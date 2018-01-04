import pafy

def mycb(total, recvd, ratio, rate, eta):
    print(recvd, ratio, eta)

if __name__ == "__main__":
    playlist = pafy.get_playlist("https://www.youtube.com/playlist?list=PLOP8MwvFE7nOmI6rezZO84ryuqaGLOe6n")

    print(playlist["items"][0]["pafy"].videoid)

    for video in playlist["items"]:
        print(video["pafy"].videoid)

        p = pafy.new(video["pafy"].videoid)
        ba = p.getbestaudio()
        filename = ba.download(quiet=True, callback=mycb)
