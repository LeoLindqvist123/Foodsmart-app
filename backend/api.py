from fastapi import FastAPI, UploadFile, File
from data_models import ScanResponse
from agents import scan_image