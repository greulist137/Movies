import media

toy_story = media.Movie("Toy Story", "A story about a boy and his toys that come to life", "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A Marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(toy_story.storyline)
print(avatar.storyline)
avatar.show_trailer()
