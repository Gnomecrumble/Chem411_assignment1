import asyncio
import aioble
from bt_esp32_api import BLE

SERVICE_UUID = "19b10000-e8f2-537e-4f6c-d104768a1214"
SENSOR_TX_UUID = "19b10001-e8f2-537e-4f6c-d104768a1214"

max_val = 2
min_val = 1
reading_val = 1.5

async def sensor_task(ble, period_ms=3000):  #sending package every 3s to not cause bluetooth to disconnect 
    while True:
        msg = f"{max_val},{min_val},{reading_val}".encode() #packs 3 readings in to a message after turning them into a string then encoding into bytes  
        ble.send(msg) #sending the package of 3 values
        print(max_val, min_val, reading_val) #testing to see that the readings are correct 
        await asyncio.sleep_ms(period_ms)


async def main():
    ble = BLE(
        name='OLLIEESP32', #needs to be same name as in client file 
        service_uuid=SERVICE_UUID,
        tx_char_uuid=SENSOR_TX_UUID,
        adv_interval_us=250_000 #250ms
        )
    await ble.start_adv()   # starts advertising to bluetooth 
    print('BLE started, advertising...')
    
    try:
        await sensor_task(ble, period_ms=3000)   #runs te sensortask def in the main function 
    finally:
        await ble.stop()  #safe stop incase errors occour
        print('stopped')
        
asyncio.run(main())  #run the main function 