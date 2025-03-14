import logging

class UploadDocuments:
    def execute(self):
        logging.info("Iniciando RPA105 - Upload de Documentos")
        try:
            # Simulação do processo do robô
            logging.info("Executando processo de upload de documentos...")
            
            # Se ocorrer um erro, ele será capturado corretamente
            # raise Exception("Falha no upload!")  # Simulação de erro

            logging.info("RPA105 executado com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao executar RPA105: {e}", exc_info=True)
