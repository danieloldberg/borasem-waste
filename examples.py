import asyncio
import aiohttp
import borasem_api_class

async def main():

    async with aiohttp.ClientSession() as session:
        
        auth = borasem_api_class.auth.Auth(session, "https://kundportal.borasem.se/EDPFutureWeb")
        api = borasem_api_class.BorasEMAPI(auth)

        # Get Waste Schedule
        schedule = await api.async_get_schedule()

        # # Print states
        # for scheduleEntry in schedule:
        #     print(f"The entry {scheduleEntry.containerId} is being picked up at {scheduleEntry.NextWastePickup}")

        # Get Waste Schedule
        addressList = await api.async_get_address('Häglared Lunden 2')

        # Print states
        for address in addressList:
            print(address)


asyncio.run(main())

