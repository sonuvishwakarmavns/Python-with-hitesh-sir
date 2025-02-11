from pymongo import MongoClient
from bson import ObjectId


client=MongoClient("mongodb+srv://youtubepy:admin1234@cluster0.bqepv.mongodb.net/ytmanager")
#Not a good idea to include id and password in code files


db=client["ytmanager"]
video_collection=db["videos"]

print(video_collection)

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time})

def list_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']},name: {video['name']} and time: {video['time']}")

def update_video(videoid, new_name, new_time): 
    video_collection.update_one({'_id': ObjectId(videoid)},
    {"$set": {"name": new_name, "time": new_time}})

def delete_video(videoid):
    video_collection.delete_one({"_id": ObjectId(videoid)})


def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice=input("Enter your choice :")

        if choice=='1':
            list_video()
        elif choice=='2':
            name=input("Enter the video name :")
            time=input("Enter the video time : ")
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter the video id to update :")
            name=input("Enter the updated video name :")
            time=input("Enter the updated video time : ")
            update_video(video_id,name,time)
        elif choice=='4':
            video_id=input("Enter the video id to delete :")
            delete_video(video_id)
        elif choice=='5':
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()