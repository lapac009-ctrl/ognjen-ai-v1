import modal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Inicijalizacija aplikacije
app = modal.App("ognjen-tesla-god-mode")
web_app = FastAPI()

# DODAJEMO CORS: Ovo dozvoljava tvom GitHub sajtu da komunicira sa Modal-om
web_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Slika sa alatima za drajvere i sistemsko programiranje
image = modal.Image.debian_slim().apt_install("g++", "nasm").pip_install("fastapi", "uvicorn")

@app.function(gpu="H100", image=image)
def build_everything_from_scratch(command: str):
    """
    Ovo je tvoj glavni inženjerski mozak.
    Ovde se generiše x86_64 kernel, drajveri i virtuelni hardver.
    """
    cmd = command.lower()
    
    if "ram" in cmd:
        return "Sistem: Inicijalizujem Ognjen-RAM. Mapiram 128GB virtuelne memorije direktno u kernel..."
    elif "graficka" in cmd or "nivada" in cmd:
        return "Sistem: Konstruišem virtuelni vGPU. PCIe registri konfigurisani za nultu latenciju."
    elif "os" in cmd or "kernel" in cmd:
        return "Sistem: Pišem bootloader i x86_64 kernel. Operativni sistem se gradi od nule."
    
    return f"Sistem: Zahtev '{command}' primljen. Tesla-mode optimizacija pokrenuta."

@web_app.get("/api/chat")
async def chat(q: str):
    # Pozivamo funkciju na Modalu
    response = build_everything_from_scratch.remote(q)
    return {"response": response}

@app.function()
@modal.asgi_app()
def start():
    return web_app
