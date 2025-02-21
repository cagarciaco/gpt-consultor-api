from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ProyectoInput(BaseModel):
    empresa: str
    tipo_intervencion: str
    analista_info: str

class FinanzasInput(BaseModel):
    financial_data: str

class InformeInput(BaseModel):
    tipo_informe: str

class GPTCedec:
    def __init__(self):
        self.empresa = None
        self.tipo_intervencion = None
        self.analista_info = None
        self.financial_data = None
        self.kit_consultor_recs = []
        self.informes = {}
    
    def iniciar_proyecto(self, empresa, tipo_intervencion, analista_info):
        self.empresa = empresa
        self.tipo_intervencion = tipo_intervencion
        self.analista_info = analista_info
        return {"message": f"Proyecto para {self.empresa} iniciado en área de {self.tipo_intervencion}."}
    
    def interpretar_finanzas(self, financial_data):
        self.financial_data = financial_data
        return {"message": "Análisis financiero completado. Se identifican riesgos en liquidez y rentabilidad."}
    
    def recomendar_kit_consultor(self):
        self.kit_consultor_recs = ["Plantilla DAFO", "Guía de Análisis de Riesgos", "Matriz CAME"]
        return {"message": f"Se recomiendan las siguientes herramientas: {', '.join(self.kit_consultor_recs)}"}
    
    def generar_informe(self, tipo_informe):
        informes = {
            "A12": "Plan de trabajo: Definir estructura y objetivos.",
            "A16": "Informe diario: Actividades realizadas y próximas acciones.",
            "A13": "Informe semanal: Seguimiento y ajuste de estrategia.",
            "A13B": "Informe de cierre: Evaluación de resultados y recomendaciones."
        }
        return {"message": informes.get(tipo_informe, "Tipo de informe no reconocido.")}

cedec_gpt = GPTCedec()

@app.post("/iniciar_proyecto")
def iniciar_proyecto(data: ProyectoInput):
    return cedec_gpt.iniciar_proyecto(data.empresa, data.tipo_intervencion, data.analista_info)

@app.post("/interpretar_finanzas")
def interpretar_finanzas(data: FinanzasInput):
    return cedec_gpt.interpretar_finanzas(data.financial_data)

@app.get("/recomendar_kit_consultor")
def recomendar_kit_consultor():
    return cedec_gpt.recomendar_kit_consultor()

@app.post("/generar_informe")
def generar_informe(data: InformeInput):
    return cedec_gpt.generar_informe(data.tipo_informe)
