
watch_url = "https://www.youtube.com/watch?v="


###### functions

def is_valid_url(url):
        return url.startswith(watch_url) and len(url) > len(watch_url)

def get_video_id(url):
  
    id_start_index = len(watch_url)

    id_end_index = len(url)

    id = url[id_start_index : id_end_index]

    return id

def get_thumbnail_url(video_id):
    return f"http://i3.ytimg.com/vi/{video_id}/maxresdefault.jpg"

##### end of functions


ext = 'n'

while ext.lower() == 'n':

    video_url = input("Enter video URL: ")
    video_url = video_url.strip() # Remove whitespaces

    while not is_valid_url(video_url):
        video_url = input("Invalid URL! Please enter a valid video URL: ").strip()

    video_id = get_video_id(video_url)

    thumbnail_url = get_thumbnail_url(video_id)

    print("Thumbnail URL: " + thumbnail_url)

    print() # New line

    ext = input("Exit [y/n]?: ")
