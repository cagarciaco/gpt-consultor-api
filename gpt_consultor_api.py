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
    
    def preparar_intervencion(self, empresa, tipo_intervencion, analista_info):
        self.empresa = empresa
        self.tipo_intervencion = tipo_intervencion
        self.analista_info = analista_info
        return {"message": f"Preparación de la intervención iniciada para {self.empresa}. Objetivos identificados y estrategia inicial definida."}
    
    def conferencia_apertura(self):
        return {"message": "Conferencia de Apertura realizada. Se han establecido expectativas, objetivos y plan de trabajo inicial."}
    
    def desarrollo_intervencion(self):
        return {"message": "Desarrollo de la intervención en curso. Metodologías aplicadas, herramientas implementadas y seguimiento en proceso."}
    
    def interpretar_finanzas(self, financial_data):
        self.financial_data = financial_data
        return {"message": "Análisis financiero completado. Se identifican riesgos en liquidez y rentabilidad. Estrategia de mitigación recomendada."}
    
    def recomendar_kit_consultor(self):
        if not self.financial_data:
            return {"message": "Error: El análisis financiero debe completarse antes de recomendar herramientas."}
        self.kit_consultor_recs = ["Plantilla DAFO", "Guía de Análisis de Riesgos", "Matriz CAME"]
        return {"message": f"Se recomiendan las siguientes herramientas: {', '.join(self.kit_consultor_recs)}"}
    
    def generar_informe(self, tipo_informe):
        if not self.kit_consultor_recs:
            return {"message": "Error: Se deben recomendar herramientas antes de generar el informe."}
        informes = {
            "A12": "Plan de trabajo: Definir estructura y objetivos.",
            "A16": "Informe diario: Actividades realizadas y próximas acciones.",
            "A13": "Informe semanal: Seguimiento y ajuste de estrategia.",
            "A13F": "Informe de cierre: Evaluación de resultados y recomendaciones."
        }
        return {"message": informes.get(tipo_informe, "Tipo de informe no reconocido.")}
    
    def transferencia_soporte(self):
        return {"message": "Transferencia de información realizada. Se ha traspasado la información clave al equipo de Mentoring Ejecutivo."}

cedec_gpt = GPTCedec()

@app.post("/preparar_intervencion")
def preparar_intervencion(data: ProyectoInput):
    return cedec_gpt.preparar_intervencion(data.empresa, data.tipo_intervencion, data.analista_info)

@app.post("/conferencia_apertura")
def conferencia_apertura():
    return cedec_gpt.conferencia_apertura()

@app.post("/desarrollo_intervencion")
def desarrollo_intervencion():
    return cedec_gpt.desarrollo_intervencion()

@app.post("/interpretar_finanzas")
def interpretar_finanzas(data: FinanzasInput):
    return cedec_gpt.interpretar_finanzas(data.financial_data)

@app.get("/recomendar_kit_consultor")
def recomendar_kit_consultor():
    return cedec_gpt.recomendar_kit_consultor()

@app.post("/generar_informe")
def generar_informe(data: InformeInput):
    return cedec_gpt.generar_informe(data.tipo_informe)

@app.post("/transferencia_soporte")
def transferencia_soporte():
    return cedec_gpt.transferencia_soporte()

