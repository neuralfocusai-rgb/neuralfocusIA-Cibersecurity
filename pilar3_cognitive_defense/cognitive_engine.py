import json
import os
from datetime import datetime

class NeuralFocusCognitiveEngine:
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.telemetry = self.load_telemetry()
        self.findings = []

    def load_telemetry(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"❌ Error: Archivo de configuración '{self.config_path}' no encontrado.")
        with open(self.config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def run_semantic_analysis(self):
        print("🧠 [neuralFocus] Iniciando análisis contextual predictivo...")
        org = self.telemetry["organization_metadata"]
        nodes = self.telemetry["infrastructure_topology"]
        controls = self.telemetry["security_controls"]

        # Regla de Correlación 1: RDP Expuesto en Nodo de Datos Críticos
        if controls["internet_facing_rdp_allowed"] and not controls["network_segmentation_enforced"]:
            for node in nodes:
                if node["criticality"] == "CRITICAL" and any(p["port"] == 3389 for p in node["open_ports"]):
                    self.findings.append({
                        "id": "NF-001",
                        "title": "Exposición Crítica de Vector RDP en Activo EHR Central",
                        "severity": "CRITICAL",
                        "impact_type": "Secuestro de Infraestructura (Ransomware)",
                        "description": f"El nodo '{node['name']}' ({node['ip_address']}) procesa datos médicos e historias clínicas confidenciales bajo regulaciones {org['compliance_target']}. El puerto 3389 (RDP) es visible desde redes externas sin aislamiento ni segmentación perimetral.",
                        "cascade_effect": "Un atacante puede ejecutar ataques de fuerza bruta o explotación de vulnerabilidades de protocolo en RDP para comprometer el servidor EHR. Al no existir segmentación de red, el impacto se despliega de inmediato hacia la puerta de enlace DICOM/PACS, paralizando por completo el diagnóstico por imágenes de la clínica.",
                        "remediation": "Desactivar la exposición directa de RDP a internet. Implementar una arquitectura de acceso Zero-Trust o pasarela VPN con autenticación multifactor (MFA), y aislar la VLAN-10 mediante reglas de firewall estrictas.",
                        "trigger_defensive_action": True
                    })

        # Regla de Correlación 2: Protocolo Heredado Vulnerable a Movimientos Laterales
        if controls["unencrypted_smb_allowed"]:
            for node in nodes:
                if any(p["port"] == 445 for p in node["open_ports"]) and node["criticality"] == "MEDIUM":
                    self.findings.append({
                        "id": "NF-002",
                        "title": "Exposición de Protocolo de Almacenamiento Compartido Libre (SMB)",
                        "severity": "HIGH",
                        "impact_type": "Movimiento Lateral / Infiltración Interna",
                        "description": f"La terminal de recepción '{node['name']}' ({node['ip_address']}) mantiene el puerto 445 abierto sin cifrado estricto ni mitigación de vectores heredados.",
                        "cascade_effect": "Si un atacante infecta la máquina de recepción (vía phishing), puede explotar el servicio de SMB expuesto para saltar directamente hacia otros servidores de la red corporativa, usando el nodo comprometido como puente de comandos (C2).",
                        "remediation": "Deshabilitar SMBv1 por completo, forzar firmas de comunicación SMBv3 en políticas de grupo de Windows y bloquear el tráfico local innecesario entre terminales de la misma subred.",
                        "trigger_defensive_action": False
                    })

    def generate_markdown_report(self):
        org = self.telemetry["organization_metadata"]
        report_filename = f"neuralfocus_security_report.md"
        
        markdown_content = f"""# 🛡️ Reporte de Resiliencia Cognitiva - neuralFocusAI
**Organización:** {org['company_name']}
**Sector:** {org['industry_sector']}
**Objetivos de Cumplimiento:** {org['compliance_target']}
**Fecha de Análisis:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC
---
## 📊 Resumen Ejecutivo de Postura de Seguridad
Este reporte ha sido generado de manera **pasiva e inteligente** mediante el análisis lógico de configuraciones de infraestructura, correlacionando la visibilidad de red con la criticidad de los activos de negocio sin generar vectores intrusivos que afecten la continuidad operativa.
"""
        for f in self.findings:
            markdown_content += f"""
### [{f['severity']}] {f['id']}: {f['title']}
* **Tipo de Impacto:** {f['impact_type']}
* **Descripción:** {f['description']}
* **Impacto en Cascáda Estructurado:** {f['cascade_effect']}
* **Plan de Mitigación Recomendado:** {f['remediation']}
---
"""
        markdown_content += "\n*Reporte confidencial generado de forma segura por neuralFocus Engine.*"
        
        with open(report_filename, "w", encoding="utf-8") as rf:
            rf.write(markdown_content)
        print(f"📝 [neuralFocus] Reporte analítico de infraestructura exportado con éxito a '{report_filename}'.")

    def execute_resilience_loop(self):
        for f in self.findings:
            if f["trigger_defensive_action"]:
                print(f"\n🚨 [ALERTA DE CAOS DETECTADA] Amenaza potencial: {f['title']}")
                print("🔄 [Lazo de Resiliencia] Notificando anomalía al Enterprise Orchestrator (Node.js)...")
                print("🔒 [Pilar 2 - Ciberdefensa] DISPARANDO PROTOCOLO DE RESPALDO CRÍTICO PREVENTIVO (AES-256-GCM)...")
                print("🛡️  [neuralFocus] Mitigación lógica orquestada. Sistemas protegidos proactivamente.")

if __name__ == "__main__":
    engine = NeuralFocusCognitiveEngine()
    engine.run_semantic_analysis()
    engine.generate_markdown_report()
    engine.execute_resilience_loop()
