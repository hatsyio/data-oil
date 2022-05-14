import logging
import sys
from src.data_ingestion import main

if __name__ == "__main__":
    logging.basicConfig(
        filename="logs/ingestion.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    main()
