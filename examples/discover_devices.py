import asyncio
from wifi_direct_raspi import WDScanner

    
if __name__ == "__main__":
    async def main():
        devices = await WDScanner("virtual_push_button").discover()
        
        for device in devices:
            print("-------------------")
            print(device.mac_address)
            print(device.name)
    
    asyncio.run(main())