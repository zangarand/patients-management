from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from class_patient import Patient
from data import patients

app = FastAPI()

class PatientSchema(BaseModel):
    id: int
    name: str
    age: int
    cpf: str
    phone_number: str
    report: str

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def menu_principal():
    return """
    <html>
        <head>
            <title>Menu do sistema</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
                .menu-container { background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); width: 400px; }
                h1 { text-align: center; color: #333; margin-bottom: 30px; }
                .botao { display: block; width: 100%; padding: 15px; margin-bottom: 15px; background-color: #007bff; color: white; text-align: center; text-decoration: none; border-radius: 5px; font-size: 16px; font-weight: bold; transition: background 0.3s; box-sizing: border-box; border: none; cursor: pointer; }
                .botao:hover { background-color: #0056b3; }
                .botao-sair { background-color: #dc3545; }
                .botao-sair:hover { background-color: #c82333; }
            </style>
        </head>
        <body>
            <div class="menu-container">
                <h1>Menu de Pacientes</h1>
                
                <a href="/docs#/Pacientes/listar_pacientes_pacientes__get" class="botao"> Lista de Pacientes</a>
                <a href="/docs#/Pacientes/adicionar_paciente_pacientes__post" class="botao"> Adicionar Paciente</a>
                <a href="/docs#/Pacientes/editar_paciente_pacientes__patient_id__put" class="botao"> Editar Paciente</a>
                <a href="/docs#/Pacientes/remover_paciente_pacientes__patient_id__delete" class="botao"> Remover Paciente</a>
                
                <button onclick="alert('Para sair do sistema, basta fechar a aba (OS PACIENTES CADASTRADOS SERÃO DELETADOS).')" class="botao botao-sair"> Sair</button>
            </div>
        </body>
    </html>
    """