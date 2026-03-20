import asyncio
from bt_python_api import BLEClient

SERVICE_UUID = "19b10000-e8f2-537e-4f6c-d104768a1214"
SENSOR_UUID  = "19b10001-e8f2-537e-4f6c-d104768a1214"

def on_data(sender, data: bytes):   #data being recived from sender via bytes 
    try:
        decoded = data.decode().strip() #converts package to string 
        parts = decoded.split(",")  #splits the 3 parts of the package from each other 

        if len(parts) == 3: #checks to make sure there are 3 parts to the spliting of the package
            max_val = int(parts[0]) #converts the package strgs to intergers 
            min_val = int(parts[1])
            reading = int(parts[2])

            print(f"Max={max_val}, Min={min_val}, Reading={reading}") #print the values to ensure they were sent correctly 
        else:
            print("Bad format:", decoded)   #lets know if the package was not sent in the expected format 

    except Exception as e:  #stops any errors from directly crashing the program while saving what the error was 
        print("Error:", data, e)    

async def main():
    client = BLEClient(name="ESP32", service_uuids=[SERVICE_UUID])
    try:
        await client.connect()
        await client.start_notify(SENSOR_UUID, on_data)

        print("Listening...")
        await asyncio.Event().wait()

    finally:
        await client.disconnect()       # safe disconnect 

asyncio.run(main())