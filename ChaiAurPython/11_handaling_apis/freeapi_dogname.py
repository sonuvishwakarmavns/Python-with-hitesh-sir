import requests

def fetch_random_dogapi():
    url="https://api.freeapi.app/api/v1/public/dogs"
    response=requests.get(url)
    data=response.json()
    #print("API Response:", data) 

    if data["success"] and "data" in data:
      dogdata_list = data["data"]["data"]
    if dogdata_list:
            dogdata = dogdata_list[0]  # Access the first dog entry in the list
            #print("Dog Data:", dogdata)  # Debugging line to print the dog data
            dog_name = dogdata.get("name", "Unknown")  # Use get to avoid KeyError
            dog_origin = dogdata.get("origin", "Unknown")  # Use get to avoid KeyError
            return dog_name, dog_origin
    else:
        raise Exception("Faild to fetch data of dog")



def main():
    try:
        dog_name,dog_orgin=fetch_random_dogapi()
        print(f"dogname:{dog_name} \ndogorgin:{dog_orgin}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
