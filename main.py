import os

from thispersondoesnotexist import get_online_person, get_checksum_from_picture, Person


def generate_avatar(time, checksum_first_pic, checksum_second_pic):
    check_dir()
    for i in range(time):
        if checksum_first_pic == checksum_second_pic:
            break
        fetch_online_person_and_save()


def fetch_online_person_and_save():
    person = Person(fetch_online=True)
    picture = get_online_person()
    checksum_pic = get_checksum_from_picture(picture)
    person.save("avatars/" + checksum_pic + ".jpg")


def check_dir():
    if not os.path.exists("avatars"):
        os.makedirs("avatars")


if __name__ == "__main__":
    checksum, checksum2 = str(1).encode(), str(2).encode()
    generate_avatar(int(input("How many avatars do you want to generate? ")), checksum, checksum2)
