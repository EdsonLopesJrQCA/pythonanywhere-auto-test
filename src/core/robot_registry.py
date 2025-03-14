from src.robots.finance.upload_documents import UploadDocuments
from src.robots.download.download_cases import DownloadCases
from src.robots.upload.upload_progress import UploadProgress
from src.robots.validate.data_comparison import DataComparison

ROBOTS = {
    "RPA105": UploadDocuments.execute,    # Finaceiro Upload de Documentos
    "RPA003": DownloadCases.execute,      # Download de Processos - INTER
    "RPA011": UploadProgress.execute,     # Upload de Andamentos - CVC
    "RPA015": DataComparison.execute,     # Confronto de Base - CETELEM
}
