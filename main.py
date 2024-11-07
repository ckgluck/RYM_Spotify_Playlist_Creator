from src.create_playlist import create_playlist, get_authenticated_user_id


# Main function to test the playlist creation
def main():
    # Authenticate user and get the username (user ID)
    username = get_authenticated_user_id()

    # Define playlist name and the songs to add
    playlist_name = "My Playlist"
    song_data = [
        "Vampire Weekend - The Surfer",
        "Vampire Weekend - Campus",
        "Steely Dan - Deacon Blues"
    ]

    # Create the playlist and add songs
    create_playlist(username, playlist_name, song_data)


if __name__ == "__main__":
    main()