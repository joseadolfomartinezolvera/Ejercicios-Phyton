
import asyncio
async def turno(espera, cantidad):
    """Produce números de 0 a *cantidad* cada *espera* segundos."""
    for i in range(cantidad):
        yield i
        await asyncio.sleep(espera)
async def main():
    async for x in turno(4,100):
        print("🐘"*(x+1))
        if x < 1:
            print (f"{x+1} Elefante se balanceaba sobre la tela de un araña")
            print("como la tela se resistía fue a llamar otro elefante 🎶")
        else:
            print (f"{x+1} Elefantes se balanceaban sobre la tela de un araña")
            print("como la tela se resistía fueron a llamar otro elefante 🎶")
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
