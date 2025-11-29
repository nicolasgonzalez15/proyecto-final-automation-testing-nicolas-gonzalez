# Logger - Todo lo que pasa en selenium - vemos fallos internamente 
# Auditoría - Pasos ejecutados
import logging
import pathlib

# Creamos carpeta
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True) #Si la carpeta de logs existe

# Creamos archivo
log_file = audit_dir/ 'suite.log'

# Inicializar Logger
logger = logging.getLogger('TalentoTech')
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(log_file,mode='a',encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter) # Definiendo archivo
    logger.addHandler(file_handler)

# format='%(asctime)s %(levelname)s %(name)s – %(message)s', datefmt='%H:%M:%S'

# datetime.now().strftime("%Y-%m-%d")